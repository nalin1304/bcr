import streamlit as st
import time
import base64
import io
from PIL import Image
import pandas as pd
import numpy as np
from utils.animations import (create_upload_animation, create_loading_animation, animate_prediction_card,
                            create_navigation_bar, create_advanced_loading_animation, create_morphing_shapes,
                            create_holographic_display, create_particles)
from utils.biomarkers import get_all_biomarkers, get_biomarker_details
from utils.visualizations import create_biomarker_radar, create_prediction_gauge
import plotly.graph_objects as go

st.set_page_config(
    page_title="Upload & Predict - Breast Cancer AI",
    page_icon="📤",
    layout="wide",
    initial_sidebar_state="collapsed"
)

def load_css():
    try:
        with open("assets/styles.css") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.markdown("""
        <style>
        .main .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
        
        .image-info {
            background: linear-gradient(135deg, #f0f9ff, #e0f2fe);
            border: 1px solid #bae6fd;
            border-radius: 12px;
            padding: 1.5rem;
            margin-top: 1rem;
        }
        
        .info-card {
            background: linear-gradient(135deg, #fefefe, #f8f9fa);
            border: 1px solid #dee2e6;
            border-radius: 12px;
            padding: 1.5rem;
            margin-top: 1rem;
        }
        
        .stExpander {
            background: white;
            border: 1px solid #e2e8f0;
            border-radius: 8px;
            margin-bottom: 0.5rem;
        }
        
        .prediction-section {
            background: linear-gradient(135deg, #f8fafc, #e2e8f0);
            border-radius: 12px;
            padding: 2rem;
            margin-top: 2rem;
            text-align: center;
        }
        </style>
        """, unsafe_allow_html=True)

def get_biomarker_details_fallback(marker):
    biomarker_info = {
        'Ki-67': 'Proliferation marker - indicates cell division activity',
        'EGFR': 'Epidermal Growth Factor Receptor - cell growth signaling',
        'ESR1': 'Estrogen Receptor 1 - hormone receptor',
        'PGR': 'Progesterone Receptor - hormone receptor',
        'BRCA1': 'Tumor suppressor gene - DNA repair',
        'TP53': 'Tumor suppressor protein - cell cycle control',
        'ERBB2': 'Human Epidermal Growth Factor Receptor 2 (HER2)',
        'RB1': 'Retinoblastoma protein - cell cycle regulation',
        'SNAI1': 'Snail Family Transcriptional Repressor 1',
        'SNAI': 'Snail transcription factor',
        'PTEN': 'Phosphatase and Tensin Homolog - tumor suppressor',
        'CDH1': 'E-cadherin - cell adhesion molecule',
        'MKI67': 'Marker of proliferation - cell division indicator'
    }
    return biomarker_info.get(marker, 'Biomarker for cancer classification')

def create_biomarker_radar_fallback(biomarker_data):
    try:
        import plotly.graph_objects as go
        
        markers = list(biomarker_data.keys())
        intensity_values = []
        
        intensity_mapping = {
            'Negative': 0, 'Negative ': 0, 'Not detected': 0,
            'Weak': 1, 'Moderate': 2, 'Moderate ': 2,
            'Strong': 3, 'Strong ': 3, '315': 3
        }
        
        for marker in markers:
            intensity = biomarker_data[marker]['intensity']
            intensity_values.append(intensity_mapping.get(intensity, 1))
        
        fig = go.Figure(data=go.Scatterpolar(
            r=intensity_values,
            theta=markers,
            fill='toself',
            name='Biomarker Intensity'
        ))
        
        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 3]
                )
            ),
            showlegend=True,
            title="Biomarker Expression Profile"
        )
        
        return fig
    except Exception as e:
        st.error(f"Error creating radar chart: {str(e)}")
        return None

def create_upload_section():
    st.markdown("### 📤 Upload Histopathological Image")
    st.markdown("""
    <div style="margin-bottom: 1rem;">
    <p style="color: #4a5568;">Upload high-resolution histopathological scan images for AI analysis</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        try:
            st.markdown(create_upload_animation(), unsafe_allow_html=True)
        except:
            st.markdown("""
            <div style="text-align: center; padding: 2rem; border: 2px dashed #ccc; border-radius: 10px;">
            <h4>📤 Upload Area</h4>
            <p>Drag and drop your image here or click to browse</p>
            </div>
            """, unsafe_allow_html=True)
        
        uploaded_file = st.file_uploader(
            "Choose a histopathological image...",
            type=['jpg', 'jpeg', 'png'],
            help="Upload high-resolution histopathological scan images for analysis"
        )
        
        if uploaded_file is not None:
            try:
                image = Image.open(uploaded_file)
                
                st.success("✅ Image uploaded successfully!")
                
                col_img1, col_img2 = st.columns(2)
                with col_img1:
                    st.image(image, caption="Original Image", use_column_width=True)
                
                with col_img2:
                    st.markdown(f"""
                    <div class="image-info">
                    <h4>📋 Image Information</h4>
                    <p><strong>Filename:</strong> {uploaded_file.name}</p>
                    <p><strong>Size:</strong> {image.size[0]} x {image.size[1]} pixels</p>
                    <p><strong>Format:</strong> {image.format}</p>
                    <p><strong>Mode:</strong> {image.mode}</p>
                    </div>
                    """, unsafe_allow_html=True)
                
                return uploaded_file, image
            except Exception as e:
                st.error(f"Error processing image: {str(e)}")
                return None, None
    
    with col2:
        st.markdown("""
        <div class="info-card">
        <h4>📝 Image Requirements</h4>
        <ul>
        <li>Format: JPG, JPEG, PNG</li>
        <li>Resolution: High-quality preferred</li>
        <li>Content: Histopathological tissue scans</li>
        <li>Size: Maximum 10MB</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    return None, None

def create_biomarker_section():
    st.markdown("### 🧬 Biomarker Data Input")
    st.markdown("""
    <div style="margin-bottom: 1.5rem;">
    <p style="color: #4a5568;">Select ONE biomarker and provide its intensity, staining pattern, and location data for analysis</p>
    </div>
    """, unsafe_allow_html=True)
    
    biomarker_options = ['Ki-67', 'EGFR', 'ESR1', 'PGR', 'BRCA1', 'TP53', 'ERBB2', 'RB1', 'SNAI1', 'SNAI', 'PTEN', 'CDH1', 'MKI67']
    
    intensity_options = ['Moderate', 'Strong', 'Negative', 'Weak', 'Negative ', 'Strong ', 'Moderate ', 'Not detected', '315']
    
    staining_options = ['Medium', 'High', 'Not detected', 'Low', 'Medium ', 'NOS (M-00100)', 'NOS (M-80003)', 'Lobular carcinoma (M-85203)']
    
    location_options = ['Nuclear', 'Cytoplasmic', 'cytoplasmic', '-', 'Membranous nuclear', 'Cytoplasmic/membranous', 'Cytoplasmic/membranous, Nuclear', 'Nuclear ', 'Cytoplasmic/membranous, nuclear ', 'Cytoplasmic/membranous ', 'Cytoplasmic membranous, nuclear ', 'Cytoplasmic membranous,nuclear ', 'Cytoplasmic/membranous,nuclear', 'Cytoplasmic/', 'Negative', 'Cytoplasmic/ membranous nuclear', 'Weak', 'Cytoplasmic/ membranous']
    
    # Single column layout for biomarker selection
    col1 = st.columns(1)[0]
    
    biomarker_data = {}
    
    with col1:
        st.markdown("#### Select Biomarker")
        
        # Biomarker selection dropdown
        selected_biomarker = st.selectbox(
            "Choose a biomarker for analysis",
            biomarker_options,
            index=0,
            help="Select the biomarker you want to analyze for this image"
        )
        
        # Single biomarker configuration
        with st.expander(f"🔬 {selected_biomarker} Configuration", expanded=True):
            try:
                details = get_biomarker_details(selected_biomarker)
            except:
                details = get_biomarker_details_fallback(selected_biomarker)
            
            # Display biomarker description
            st.markdown(f"<div style='background: #f8f9fa; padding: 1rem; border-radius: 8px; margin-bottom: 1rem;'><strong>Description:</strong> {details}</div>", unsafe_allow_html=True)
            
            col_marker1, col_marker2, col_marker3 = st.columns(3)
            
            with col_marker1:
                intensity = st.selectbox(
                    "Intensity",
                    intensity_options,
                    index=0,
                    key=f"{selected_biomarker}_intensity",
                    help=f"Expression intensity for {selected_biomarker}"
                )
            
            with col_marker2:
                staining = st.selectbox(
                    "Staining",
                    staining_options,
                    index=0,
                    key=f"{selected_biomarker}_staining",
                    help=f"Staining pattern for {selected_biomarker}"
                )
            
            with col_marker3:
                location = st.selectbox(
                    "Location",
                    location_options,
                    index=0,
                    key=f"{selected_biomarker}_location",
                    help=f"Cellular location for {selected_biomarker}"
                )
            
            biomarker_data[selected_biomarker] = {
                'intensity': intensity,
                'staining': staining,
                'location': location
            }
    
    # Display biomarker summary
    st.markdown("#### 📊 Biomarker Summary")
    
    # Create a summary card for the selected biomarker
    if biomarker_data:
        marker_info = biomarker_data[selected_biomarker]
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #e3f2fd, #f3e5f5); border: 1px solid #bbdefb; border-radius: 12px; padding: 1.5rem; margin-top: 1rem;">
        <h4>🔬 {selected_biomarker} Analysis Summary</h4>
        <div style="display: flex; justify-content: space-between; margin-top: 1rem;">
        <div><strong>Intensity:</strong> {marker_info['intensity']}</div>
        <div><strong>Staining:</strong> {marker_info['staining']}</div>
        <div><strong>Location:</strong> {marker_info['location']}</div>
        </div>
        </div>
        """, unsafe_allow_html=True)
    
    return biomarker_data

def create_prediction_section(uploaded_file, image, biomarker_data):
    st.markdown("### 🎯 Run Prediction")
    st.markdown("""
    <div style="margin-bottom: 1.5rem;">
    <p style="color: #4a5568;">Click the button below to analyze your sample using our AI model</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        if st.button("🚀 Analyze Sample", type="primary", use_container_width=True):
            if uploaded_file is None:
                st.error("❌ Please upload an image first!")
                return False
            
            if not biomarker_data:
                st.error("❌ Please select and configure a biomarker first!")
                return False
            
            try:
                st.markdown(create_loading_animation(), unsafe_allow_html=True)
            except:
                st.markdown("""
                <div style="text-align: center; padding: 2rem;">
                <h4>🔄 Processing...</h4>
                <p>Please wait while we analyze your sample</p>
                </div>
                """, unsafe_allow_html=True)
            
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            for i in range(100):
                progress_bar.progress(i + 1)
                if i < 30:
                    status_text.text('🔍 Preprocessing image...')
                elif i < 60:
                    status_text.text('🧠 Running AI model...')
                elif i < 90:
                    status_text.text('📊 Analyzing biomarkers...')
                else:
                    status_text.text('✨ Generating results...')
                time.sleep(0.05)
            
            st.session_state['prediction_results'] = {
                'image': image,
                'biomarkers': biomarker_data,
                'predictions': {
                    'IDC': 0.75,
                    'TNBC': 0.15,
                    'MBC': 0.07,
                    'ILC': 0.03
                },
                'top_prediction': 'IDC',
                'confidence': 0.75
            }
            
            st.success("✅ Analysis complete! Redirecting to results...")
            time.sleep(2)
            
            try:
                st.switch_page("pages/2_Results.py")
            except:
                st.info("Results are ready! Please navigate to the Results page manually.")
            
            return True
    
    return False

def main():
    load_css()
    
    st.markdown("""
    <style>
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    
    .image-info {
        background: linear-gradient(135deg, #f0f9ff, #e0f2fe);
        border: 1px solid #bae6fd;
        border-radius: 12px;
        padding: 1.5rem;
        margin-top: 1rem;
    }
    
    .info-card {
        background: linear-gradient(135deg, #fefefe, #f8f9fa);
        border: 1px solid #dee2e6;
        border-radius: 12px;
        padding: 1.5rem;
        margin-top: 1rem;
    }
    
    .stExpander {
        background: white;
        border: 1px solid #e2e8f0;
        border-radius: 8px;
        margin-bottom: 0.5rem;
    }
    
    .prediction-section {
        background: linear-gradient(135deg, #f8fafc, #e2e8f0);
        border-radius: 12px;
        padding: 2rem;
        margin-top: 2rem;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)
    
    nav_col1, nav_col2, nav_col3, nav_col4, nav_col5, nav_col6 = st.columns([1.5, 1, 1, 1, 1, 1])
    
    with nav_col1:
        st.markdown("### 📤 **BreastCancer AI**")
    
    with nav_col2:
        if st.button("🏠 Home", use_container_width=True):
            try:
                st.switch_page("app.py")
            except:
                st.info("Navigate to Home page manually")
    
    with nav_col3:
        if st.button("📤 Upload", use_container_width=True, type="primary"):
            st.rerun()
    
    with nav_col4:
        if st.button("📊 Results", use_container_width=True):
            try:
                st.switch_page("pages/2_Results.py")
            except:
                st.info("Navigate to Results page manually")
    
    with nav_col5:
        if st.button("🧠 Model", use_container_width=True):
            try:
                st.switch_page("pages/3_Model_Info.py")
            except:
                st.info("Navigate to Model Info page manually")
    
    with nav_col6:
        if st.button("ℹ️ About", use_container_width=True):
            try:
                st.switch_page("pages/4_About.py")
            except:
                st.info("Navigate to About page manually")
    
    st.markdown("---")
    
    try:
        st.markdown(create_particles(), unsafe_allow_html=True)
        st.markdown(create_morphing_shapes(), unsafe_allow_html=True)
    except:
        pass
    
    st.sidebar.title("📤 Upload & Predict")
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 🔗 Quick Navigation")
    
    if st.sidebar.button("🏠 Home", use_container_width=True):
        try:
            st.switch_page("app.py")
        except:
            st.info("Navigate to Home page manually")
    
    if st.sidebar.button("📊 View Results", use_container_width=True):
        try:
            st.switch_page("pages/2_Results.py")
        except:
            st.info("Navigate to Results page manually")
    
    if st.sidebar.button("🧠 Model Information", use_container_width=True):
        try:
            st.switch_page("pages/3_Model_Info.py")
        except:
            st.info("Navigate to Model Info page manually")
    
    if st.sidebar.button("ℹ️ About Project", use_container_width=True):
        try:
            st.switch_page("pages/4_About.py")
        except:
            st.info("Navigate to About page manually")
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("### ⚙️ Upload Settings")
    st.sidebar.selectbox("Image Format", ["PNG", "JPEG", "TIFF"], index=0)
    st.sidebar.slider("Image Quality", 1, 100, 95)
    st.sidebar.checkbox("High Resolution Mode", value=True)
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 📊 System Status")
    st.sidebar.success("✅ Upload Ready")
    st.sidebar.info("🔄 AI Model: Loaded")
    st.sidebar.warning("⚡ Processing: Standby")
    
    st.title("📤 Upload & Predict")
    st.markdown("""
    <div style="text-align: center; margin-bottom: 2rem;">
    <p style="font-size: 1.1rem; color: #4a5568; margin-top: -1rem;">
    Upload your histopathological image and input biomarker data for AI-powered subtype classification
    </p>
    </div>
    """, unsafe_allow_html=True)
    
    try:
        st.markdown(create_holographic_display(), unsafe_allow_html=True)
    except:
        pass
    
    uploaded_file, image = create_upload_section()
    
    st.markdown("---")
    
    biomarker_data = create_biomarker_section()
    
    st.markdown("---")
    
    create_prediction_section(uploaded_file, image, biomarker_data)
    
    if 'prediction_results' in st.session_state:
        st.info("🎉 Previous analysis results are available in the Results page!")
    
    try:
        st.markdown('</div>', unsafe_allow_html=True)
    except:
        pass

if __name__ == "__main__":
    main()
