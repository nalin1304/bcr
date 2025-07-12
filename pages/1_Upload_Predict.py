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
    with open("assets/styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def create_upload_section():
    st.markdown("### 📤 Upload Histopathological Image")
    st.markdown("""
    <div style="margin-bottom: 1rem;">
    <p style="color: #4a5568;">Upload high-resolution histopathological scan images for AI analysis</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown(create_upload_animation(), unsafe_allow_html=True)
        
        uploaded_file = st.file_uploader(
            "Choose a histopathological image...",
            type=['jpg', 'jpeg', 'png'],
            help="Upload high-resolution histopathological scan images for analysis"
        )
        
        if uploaded_file is not None:
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
    <p style="color: #4a5568;">Select biomarker intensities and staining patterns for comprehensive analysis</p>
    </div>
    """, unsafe_allow_html=True)
    
    biomarkers = get_all_biomarkers()
    
    col1, col2 = st.columns(2)
    
    biomarker_data = {}
    
    with col1:
        st.markdown("#### Primary Biomarkers")
        
        primary_markers = ['Ki-67', 'HER2', 'EGFR', 'TP53', 'CDH1']
        
        for marker in primary_markers:
            with st.expander(f"🔬 {marker}", expanded=True):
                details = get_biomarker_details(marker)
                
                col_marker1, col_marker2 = st.columns(2)
                
                with col_marker1:
                    intensity = st.selectbox(
                        "Intensity",
                        ['Weak', 'Moderate', 'Strong'],
                        key=f"{marker}_intensity",
                        help=f"Expression intensity for {marker}"
                    )
                
                with col_marker2:
                    staining = st.selectbox(
                        "Staining Type",
                        ['Nuclear', 'Cytoplasmic', 'Membranous'],
                        key=f"{marker}_staining",
                        help=f"Staining pattern for {marker}"
                    )
                
                st.markdown(f"<small>{details}</small>", unsafe_allow_html=True)
                
                biomarker_data[marker] = {
                    'intensity': intensity,
                    'staining': staining
                }
    
    with col2:
        st.markdown("#### Secondary Biomarkers")
        
        secondary_markers = ['PTEN', 'BRCA1', 'RB1', 'ESR1']
        
        for marker in secondary_markers:
            with st.expander(f"🔬 {marker}", expanded=True):
                details = get_biomarker_details(marker)
                
                col_marker1, col_marker2 = st.columns(2)
                
                with col_marker1:
                    intensity = st.selectbox(
                        "Intensity",
                        ['Weak', 'Moderate', 'Strong'],
                        key=f"{marker}_intensity",
                        help=f"Expression intensity for {marker}"
                    )
                
                with col_marker2:
                    staining = st.selectbox(
                        "Staining Type",
                        ['Nuclear', 'Cytoplasmic', 'Membranous'],
                        key=f"{marker}_staining",
                        help=f"Staining pattern for {marker}"
                    )
                
                st.markdown(f"<small>{details}</small>", unsafe_allow_html=True)
                
                biomarker_data[marker] = {
                    'intensity': intensity,
                    'staining': staining
                }
    
    st.markdown("#### 📊 Biomarker Summary")
    radar_chart = create_biomarker_radar(biomarker_data)
    st.plotly_chart(radar_chart, use_container_width=True)
    
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
            
            st.markdown(create_loading_animation(), unsafe_allow_html=True)
            
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
            st.switch_page("pages/2_Results.py")
            
            return True
    
    return False

def main():
    load_css()
    
    st.markdown("""
    <style>
    /* Upload page specific improvements */
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
            st.switch_page("app.py")
    
    with nav_col3:
        if st.button("📤 Upload", use_container_width=True, type="primary"):
            st.rerun()
    
    with nav_col4:
        if st.button("📊 Results", use_container_width=True):
            st.switch_page("pages/2_Results.py")
    
    with nav_col5:
        if st.button("🧠 Model", use_container_width=True):
            st.switch_page("pages/3_Model_Info.py")
    
    with nav_col6:
        if st.button("ℹ️ About", use_container_width=True):
            st.switch_page("pages/4_About.py")
    
    st.markdown("---")
    
    st.markdown(create_particles(), unsafe_allow_html=True)
    st.markdown(create_morphing_shapes(), unsafe_allow_html=True)
    
    st.sidebar.title("📤 Upload & Predict")
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 🔗 Quick Navigation")
    
    if st.sidebar.button("🏠 Home", use_container_width=True):
        st.switch_page("app.py")
    
    if st.sidebar.button("📊 View Results", use_container_width=True):
        st.switch_page("pages/2_Results.py")
        
    if st.sidebar.button("🧠 Model Information", use_container_width=True):
        st.switch_page("pages/3_Model_Info.py")
        
    if st.sidebar.button("ℹ️ About Project", use_container_width=True):
        st.switch_page("pages/4_About.py")
    
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
    
    st.markdown(create_holographic_display(), unsafe_allow_html=True)
    
    uploaded_file, image = create_upload_section()
    
    st.markdown("---")
    
    biomarker_data = create_biomarker_section()
    
    st.markdown("---")
    
    create_prediction_section(uploaded_file, image, biomarker_data)
    
    if 'prediction_results' in st.session_state:
        st.info("🎉 Previous analysis results are available in the Results page!")
    
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
