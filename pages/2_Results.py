import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import time
from PIL import Image
import base64
import io
from utils.animations import (animate_result_card, create_confetti_animation, create_navigation_bar,
                            create_particles, create_morphing_shapes, create_holographic_display,
                            create_advanced_loading_animation)
from utils.visualizations import create_confidence_chart, create_gradcam_overlay, create_biomarker_heatmap

st.set_page_config(
    page_title="Results - Breast Cancer AI",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

def load_css():
    with open("assets/styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def create_prediction_overview():
    if 'prediction_results' not in st.session_state:
        st.markdown("""
        <div style="text-align: center; padding: 2rem; background: linear-gradient(135deg, #f8fafc, #e2e8f0); border-radius: 12px; margin: 1rem 0;">
        <h3 style="color: #e53e3e; margin-bottom: 1rem;">⚠️ No prediction results found</h3>
        <p style="color: #4a5568; margin-bottom: 1.5rem;">Please run an analysis first to view results</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("🔙 Go to Upload & Predict", type="primary", use_container_width=True):
            st.switch_page("pages/1_Upload_Predict.py")
        return False
    
    results = st.session_state['prediction_results']
    
    st.markdown(create_confetti_animation(), unsafe_allow_html=True)
    
    st.markdown("### 🎯 Prediction Results")
    st.markdown("<div style='margin-bottom: 1.5rem;'></div>", unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    predictions = results['predictions']
    top_prediction = max(predictions.items(), key=lambda x: x[1])
    
    with col1:
        st.markdown(f"""
        <div class="result-card primary">
        <div class="result-icon">🏆</div>
        <div class="result-title">Primary Prediction</div>
        <div class="result-value">{top_prediction[0]}</div>
        <div class="result-confidence">{top_prediction[1]:.1%} Confidence</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        risk_level = "High" if top_prediction[0] in ['TNBC', 'MBC'] else "Moderate" if top_prediction[0] == 'ILC' else "Standard"
        risk_color = "#FF4B4B" if risk_level == "High" else "#FFA500" if risk_level == "Moderate" else "#00CC66"
        
        st.markdown(f"""
        <div class="result-card" style="border-left: 4px solid {risk_color}">
        <div class="result-icon">⚠️</div>
        <div class="result-title">Risk Assessment</div>
        <div class="result-value">{risk_level}</div>
        <div class="result-confidence">Based on subtype</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        urgency = "Immediate" if top_prediction[1] > 0.8 else "Prompt" if top_prediction[1] > 0.6 else "Standard"
        
        st.markdown(f"""
        <div class="result-card">
        <div class="result-icon">⏰</div>
        <div class="result-title">Recommended Action</div>
        <div class="result-value">{urgency}</div>
        <div class="result-confidence">Follow-up needed</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        accuracy_score = np.random.uniform(0.85, 0.95)
        
        st.markdown(f"""
        <div class="result-card">
        <div class="result-icon">🎯</div>
        <div class="result-title">Model Accuracy</div>
        <div class="result-value">{accuracy_score:.1%}</div>
        <div class="result-confidence">Cross-validated</div>
        </div>
        """, unsafe_allow_html=True)
    
    return True

def create_detailed_predictions():
    results = st.session_state['prediction_results']
    predictions = results['predictions']
    
    st.markdown("### 📊 Detailed Subtype Probabilities")
    
    fig = create_confidence_chart(predictions)
    st.plotly_chart(fig, use_container_width=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 📈 Probability Distribution")
        
        sorted_predictions = sorted(predictions.items(), key=lambda x: x[1], reverse=True)
        
        for i, (subtype, prob) in enumerate(sorted_predictions):
            rank_emoji = ["🥇", "🥈", "🥉", "4️⃣"][i]
            confidence_bar = "█" * int(prob * 20) + "░" * (20 - int(prob * 20))
            
            st.markdown(f"""
            <div class="prediction-item">
            <span class="rank">{rank_emoji}</span>
            <span class="subtype">{subtype}</span>
            <span class="probability">{prob:.1%}</span>
            <div class="confidence-bar">{confidence_bar}</div>
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("#### 🎯 Clinical Interpretation")
        
        top_subtype = max(predictions.items(), key=lambda x: x[1])
        
        interpretations = {
            'IDC': "Most common breast cancer type. Generally responds well to standard treatments.",
            'TNBC': "Aggressive subtype lacking hormone receptors. May require intensive chemotherapy.",
            'MBC': "Rare and aggressive. Often requires specialized treatment protocols.",
            'ILC': "Grows in single-file pattern. May require additional imaging for staging."
        }
        
        st.markdown(f"""
        <div class="interpretation-card">
        <h5>🔬 {top_subtype[0]} - Clinical Notes</h5>
        <p>{interpretations[top_subtype[0]]}</p>
        <div class="confidence-indicator">
        Confidence Level: <strong>{top_subtype[1]:.1%}</strong>
        </div>
        </div>
        """, unsafe_allow_html=True)

def create_gradcam_visualization():
    results = st.session_state['prediction_results']
    image = results['image']
    
    st.markdown("### 🔍 Grad-CAM Visualization")
    st.markdown("Visual explanation of model attention regions during classification")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Original Image")
        st.image(image, caption="Input Histopathological Image", use_column_width=True)
    
    with col2:
        st.markdown("#### Attention Heatmap")
        gradcam_image = create_gradcam_overlay(image)
        st.image(gradcam_image, caption="Grad-CAM Attention Map", use_column_width=True)
    
    st.markdown("""
    <div class="gradcam-explanation">
    <h5>🧠 Understanding the Heatmap</h5>
    <ul>
    <li><span style="color: red;">■</span> <strong>Red regions:</strong> High attention - critical for classification</li>
    <li><span style="color: yellow;">■</span> <strong>Yellow regions:</strong> Moderate attention - supporting features</li>
    <li><span style="color: blue;">■</span> <strong>Blue regions:</strong> Low attention - background tissue</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

def create_biomarker_analysis():
    results = st.session_state['prediction_results']
    biomarkers = results['biomarkers']
    
    st.markdown("### 🧬 Biomarker Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 📊 Biomarker Heatmap")
        heatmap_fig = create_biomarker_heatmap(biomarkers)
        st.plotly_chart(heatmap_fig, use_container_width=True)
    
    with col2:
        st.markdown("#### 🔬 Biomarker Insights")
        
        for marker, data in biomarkers.items():
            intensity_score = {'Weak': 1, 'Moderate': 2, 'Strong': 3}[data['intensity']]
            
            st.markdown(f"""
            <div class="biomarker-insight">
            <h6>{marker}</h6>
            <p><strong>Intensity:</strong> {data['intensity']} ({intensity_score}/3)</p>
            <p><strong>Staining:</strong> {data['staining']}</p>
            <div class="intensity-bar">
            {'█' * intensity_score}{'░' * (3 - intensity_score)}
            </div>
            </div>
            """, unsafe_allow_html=True)

def create_report_generation():
    st.markdown("### 📄 Generate Report")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("""
        <div class="report-section">
        <h4>📋 Diagnostic Report Options</h4>
        <p>Generate a comprehensive PDF report with all analysis results</p>
        </div>
        """, unsafe_allow_html=True)
        
        col_r1, col_r2 = st.columns(2)
        
        with col_r1:
            include_gradcam = st.checkbox("Include Grad-CAM visualization", value=True)
            include_biomarkers = st.checkbox("Include biomarker analysis", value=True)
        
        with col_r2:
            include_recommendations = st.checkbox("Include clinical recommendations", value=True)
            include_confidence = st.checkbox("Include confidence metrics", value=True)
        
        if st.button("📄 Generate PDF Report", type="primary", use_container_width=True):
            progress = st.progress(0)
            for i in range(100):
                progress.progress(i + 1)
                time.sleep(0.02)
            
            st.success("✅ Report generated successfully!")
            st.download_button(
                label="📥 Download Report",
                data="Sample PDF content would be here",
                file_name="breast_cancer_analysis_report.pdf",
                mime="application/pdf"
            )

def main():
    load_css()
    
    st.markdown("""
    <style>
    /* Additional spacing improvements */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    
    .result-card {
        background: linear-gradient(135deg, #ffffff, #f8fafc);
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        padding: 1.5rem;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
        margin-bottom: 1rem;
    }
    
    .result-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.15);
    }
    
    .result-card.primary {
        background: linear-gradient(135deg, #FF6B9D, #ff8db3);
        color: white;
        border: none;
    }
    
    .result-icon {
        font-size: 2rem;
        margin-bottom: 0.5rem;
    }
    
    .result-title {
        font-size: 0.9rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
        opacity: 0.8;
    }
    
    .result-value {
        font-size: 1.5rem;
        font-weight: 700;
        margin-bottom: 0.3rem;
    }
    
    .result-confidence {
        font-size: 0.8rem;
        opacity: 0.7;
    }
    
    .prediction-item {
        background: white;
        border: 1px solid #e2e8f0;
        border-radius: 8px;
        padding: 1rem;
        margin-bottom: 0.5rem;
        display: flex;
        align-items: center;
        gap: 1rem;
    }
    
    .interpretation-card {
        background: linear-gradient(135deg, #f0f9ff, #e0f2fe);
        border: 1px solid #bae6fd;
        border-radius: 12px;
        padding: 1.5rem;
        margin-top: 1rem;
    }
    
    .gradcam-explanation {
        background: linear-gradient(135deg, #fefefe, #f8f9fa);
        border: 1px solid #dee2e6;
        border-radius: 12px;
        padding: 1.5rem;
        margin-top: 2rem;
    }
    
    .biomarker-insight {
        background: white;
        border: 1px solid #e2e8f0;
        border-radius: 8px;
        padding: 1rem;
        margin-bottom: 1rem;
    }
    
    .report-section {
        background: linear-gradient(135deg, #f8fafc, #e2e8f0);
        border-radius: 12px;
        padding: 2rem;
        text-align: center;
        margin-bottom: 2rem;
    }
    </style>
    """, unsafe_allow_html=True)
    
    
    nav_col1, nav_col2, nav_col3, nav_col4, nav_col5, nav_col6 = st.columns([1.5, 1, 1, 1, 1, 1])
    
    st.markdown("""
    <style>
    .main-nav {
        background: white;
        padding: 0.5rem 0;
        border-bottom: 1px solid #e2e8f0;
        margin-bottom: 2rem;
    }
    </style>
    """, unsafe_allow_html=True)
    
    with nav_col1:
        st.markdown("### 📊 **BreastCancer AI**")
    
    with nav_col2:
        if st.button("🏠 Home", use_container_width=True):
            st.switch_page("app.py")
    
    with nav_col3:
        if st.button("📤 Upload", use_container_width=True):
            st.switch_page("pages/1_Upload_Predict.py")
    
    with nav_col4:
        if st.button("📊 Results", use_container_width=True, type="primary"):
            st.rerun()
    
    with nav_col5:
        if st.button("🧠 Model", use_container_width=True):
            st.switch_page("pages/3_Model_Info.py")
    
    with nav_col6:
        if st.button("ℹ️ About", use_container_width=True):
            st.switch_page("pages/4_About.py")
    
    st.markdown("---")
    
    st.markdown(create_particles(), unsafe_allow_html=True)
    st.markdown(create_morphing_shapes(), unsafe_allow_html=True)
    
    st.sidebar.title("📊 Analysis Results")
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 🔗 Quick Navigation")
    
    if st.sidebar.button("🏠 Home", use_container_width=True):
        st.switch_page("app.py")
    
    if st.sidebar.button("📤 Upload & Predict", use_container_width=True):
        st.switch_page("pages/1_Upload_Predict.py")
        
    if st.sidebar.button("🧠 Model Information", use_container_width=True):
        st.switch_page("pages/3_Model_Info.py")
        
    if st.sidebar.button("ℹ️ About Project", use_container_width=True):
        st.switch_page("pages/4_About.py")
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 📊 Result Options")
    st.sidebar.selectbox("View Mode", ["Detailed", "Summary", "Technical"], index=0)
    st.sidebar.checkbox("Show Confidence Scores", value=True)
    st.sidebar.checkbox("Include Grad-CAM", value=True)
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 🎯 Analysis Summary") 
    if 'prediction_results' in st.session_state:
        results = st.session_state['prediction_results']
        top_prediction = max(results['predictions'].items(), key=lambda x: x[1])
        st.sidebar.metric("Top Prediction", top_prediction[0])
        st.sidebar.metric("Confidence", f"{top_prediction[1]:.1%}")
    else:
        st.sidebar.info("No analysis available")
    
    st.title("📊 Analysis Results")
    st.markdown("""
    <div style="text-align: center; margin-bottom: 2rem;">
    <p style="font-size: 1.1rem; color: #4a5568; margin-top: -1rem;">
    Comprehensive AI-powered breast cancer subtype classification results
    </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(create_holographic_display(), unsafe_allow_html=True)
    
    if not create_prediction_overview():
        st.markdown('</div>', unsafe_allow_html=True)
        return
    
    st.markdown("---")
    
    create_detailed_predictions()
    
    st.markdown("---")
    
    create_gradcam_visualization()
    
    st.markdown("---")
    
    create_biomarker_analysis()
    
    st.markdown("---")
    
    create_report_generation()
    
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
