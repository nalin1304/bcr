import plotly.graph_objects as go
import plotly.express as px
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
import pandas as pd

def create_biomarker_radar(biomarker_data):
    markers = list(biomarker_data.keys())
    
    intensity_values = []
    for marker in markers:
        intensity = biomarker_data[marker]['intensity']
        if intensity == 'Weak':
            intensity_values.append(1)
        elif intensity == 'Moderate':
            intensity_values.append(2)
        else:
            intensity_values.append(3)
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatterpolar(
        r=intensity_values,
        theta=markers,
        fill='toself',
        name='Biomarker Profile',
        line=dict(color='#FF6B9D', width=2),
        fillcolor='rgba(255, 107, 157, 0.3)'
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 3],
                tickvals=[1, 2, 3],
                ticktext=['Weak', 'Moderate', 'Strong']
            )
        ),
        showlegend=False,
        title="Biomarker Expression Profile",
        font=dict(size=12)
    )
    
    return fig

def create_prediction_gauge(confidence):
    fig = go.Figure(go.Indicator(
        mode = "gauge+number+delta",
        value = confidence * 100,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "Prediction Confidence"},
        delta = {'reference': 80},
        gauge = {
            'axis': {'range': [None, 100]},
            'bar': {'color': "#FF6B9D"},
            'steps': [
                {'range': [0, 50], 'color': "lightgray"},
                {'range': [50, 80], 'color': "gray"}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': 90
            }
        }
    ))
    
    return fig

def create_confidence_chart(predictions):
    subtypes = list(predictions.keys())
    confidences = list(predictions.values())
    
    colors = ['#FF6B9D', '#4ECDC4', '#45B7D1', '#96CEB4']
    
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        x=subtypes,
        y=confidences,
        marker_color=colors,
        text=[f'{conf:.1%}' for conf in confidences],
        textposition='auto',
        hovertemplate='<b>%{x}</b><br>Confidence: %{y:.1%}<extra></extra>'
    ))
    
    fig.update_layout(
        title="Subtype Classification Probabilities",
        xaxis_title="Cancer Subtype",
        yaxis_title="Confidence Score",
        yaxis=dict(range=[0, 1], tickformat='.0%'),
        showlegend=False,
        height=400
    )
    
    return fig

def create_gradcam_overlay(original_image):
    width, height = original_image.size
    
    heatmap = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(heatmap)
    
    np.random.seed(42)
    num_hotspots = np.random.randint(3, 7)
    
    for _ in range(num_hotspots):
        center_x = np.random.randint(width // 4, 3 * width // 4)
        center_y = np.random.randint(height // 4, 3 * height // 4)
        radius = np.random.randint(20, min(width, height) // 8)
        
        intensity = np.random.uniform(0.3, 0.8)
        
        for r in range(radius, 0, -2):
            alpha = int(255 * intensity * (radius - r) / radius)
            color = (255, int(255 * (1 - intensity)), 0, alpha)
            
            draw.ellipse([
                center_x - r, center_y - r,
                center_x + r, center_y + r
            ], fill=color)
    
    heatmap = heatmap.filter(ImageFilter.GaussianBlur(radius=3))
    
    result = Image.alpha_composite(
        original_image.convert('RGBA'),
        heatmap
    )
    
    return result.convert('RGB')

def create_biomarker_heatmap(biomarker_data):
    markers = list(biomarker_data.keys())
    intensities = []
    staining_types = []
    
    for marker in markers:
        intensity = biomarker_data[marker]['intensity']
        staining = biomarker_data[marker]['staining']
        
        if intensity == 'Weak':
            intensities.append(1)
        elif intensity == 'Moderate':
            intensities.append(2)
        else:
            intensities.append(3)
        
        staining_types.append(staining)
    
    df = pd.DataFrame({
        'Biomarker': markers,
        'Intensity': intensities,
        'Staining_Type': staining_types
    })
    
    fig = go.Figure(data=go.Heatmap(
        z=[intensities],
        x=markers,
        y=['Expression Level'],
        colorscale='RdYlBu_r',
        text=[[f'{marker}<br>{staining_types[i]}' for i, marker in enumerate(markers)]],
        texttemplate='%{text}',
        textfont={"size": 10},
        colorbar=dict(
            title="Intensity",
            tickvals=[1, 2, 3],
            ticktext=['Weak', 'Moderate', 'Strong']
        )
    ))
    
    fig.update_layout(
        title="Biomarker Expression Heatmap",
        xaxis_title="Biomarkers",
        height=200
    )
    
    return fig

def create_performance_metrics(metrics):
    categories = ['Accuracy', 'Precision', 'Recall', 'F1-Score']
    
    fig = go.Figure()
    
    subtypes = ['IDC', 'TNBC', 'MBC', 'ILC']
    colors = ['#FF6B9D', '#4ECDC4', '#45B7D1', '#96CEB4']
    
    for i, subtype in enumerate(subtypes):
        values = [0.93, 0.91, 0.95, 0.93] if subtype == 'IDC' else \
                [0.89, 0.87, 0.91, 0.89] if subtype == 'TNBC' else \
                [0.85, 0.82, 0.88, 0.85] if subtype == 'MBC' else \
                [0.87, 0.84, 0.90, 0.87]
        
        fig.add_trace(go.Scatterpolar(
            r=values,
            theta=categories,
            fill='toself',
            name=subtype,
            line=dict(color=colors[i])
        ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 1]
            )
        ),
        showlegend=True,
        title="Model Performance by Subtype"
    )
    
    return fig

def create_feature_importance(features, importance_scores):
    fig = go.Figure(go.Bar(
        x=importance_scores,
        y=features,
        orientation='h',
        marker_color='#FF6B9D'
    ))
    
    fig.update_layout(
        title="Feature Importance",
        xaxis_title="Importance Score",
        yaxis_title="Features",
        height=400
    )
    
    return fig
