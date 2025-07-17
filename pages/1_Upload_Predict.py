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

def get_biomarker_details_fallback(marker):
    """Fallback function for biomarker details"""
    biomarker_info = {
        'Ki-67': 'Proliferation marker - indicates cell division activity',
        'EGFR': 'Epidermal Growth Factor Receptor - cell growth signaling',
        'ESR1': 'Estrogen Receptor 1 - hormone receptor',
        'PGR': 'Progesterone Receptor - hormone receptor'
    }
    return biomarker_info.get(marker, 'Biomarker for cancer classification')

def create_biomarker_radar_fallback(biomarker_data):
    """Fallback function to create biomarker radar chart"""
    try:
        import plotly.graph_objects as go
        
        markers = list(biomarker_data.keys())
        intensity_values = []
        
        intensity_mapping = {
            'Negative': 0,
            'Moderate': 1,
            'Strong': 2,
            'Very Strong': 3
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
    """Create the image upload section with single column layout"""
    st.markdown("### 📤 Upload Histopathological Image")
    st.markdown("Upload high-resolution histopathological scan images for AI analysis")
    
    # Single column layout - no complex multi-column arrangements
    try:
        st.markdown(create_upload_animation(), unsafe_allow_html=True)
    except:
        st.info("📤 Upload your histopathological image below")
    
    uploaded_file = st.file_uploader(
        "Choose a histopathological image...",
        type=['jpg', 'jpeg', 'png'],
        help="Upload high-resolution histopathological scan images for analysis"
    )
    
    if uploaded_file is not None:
        try:
            image = Image.open(uploaded_file)
            
            st.success("✅ Image uploaded successfully!")
            
            # Display image in single column
            st.image(image, caption="Uploaded Image", use_column_width=True)
            
            # Image info in single column
            st.info(f"""
            **📋 Image Information**
            - **Filename:** {uploaded_file.name}
            - **Size:** {image.size[0]} x {image.size[1]} pixels
            - **Format:** {image.format}
            - **Mode:** {image.mode}
            """)
            
            return uploaded_file, image
        except Exception as e:
            st.error(f"Error processing image: {str(e)}")
            return None, None
    
    # Requirements info in single column
    st.info("""
    **📝 Image Requirements**
    - Format: JPG, JPEG, PNG
    - Resolution: High-quality preferred
    - Content: Histopathological tissue scans
    - Size: Maximum 10MB
    """)
    
    return None, None

def create_biomarker_section():
    """Create biomarker section with simplified dropdowns in single column"""
    st.markdown("### 🧬 Biomarker Data Input")
    st.markdown("Select ONE biomarker and provide its intensity, staining pattern, and location data for analysis")
    
    # Simplified options - reduced to 3-4 choices each
    biomarker_options = ['Ki-67', 'EGFR', 'ESR1', 'PGR']  # Reduced from 13 to 4
    intensity_options = ['Negative', 'Moderate', 'Strong', 'Very Strong']  # Reduced to 4
    staining_options = ['Low', 'Medium', 'High', 'Not detected']  # Reduced to 4
    location_options = ['Nuclear', 'Cytoplasmic', 'Membranous']  # Reduced to 3
    
    # Single column layout for all selections
    biomarker_data = {}
    
    st.markdown("#### Select Biomarker for Analysis")
    
    # Biomarker selection dropdown
    selected_biomarker = st.selectbox(
        "Choose a biomarker for analysis",
        biomarker_options,
        index=0,
        help="Select the biomarker you want to analyze for this image"
    )
    
    # Display biomarker description
    try:
        details = get_biomarker_details(selected_biomarker)
    except:
        details = get_biomarker_details_fallback(selected_biomarker)
    
    st.info(f"**Description:** {details}")
    
    # Configuration options in single column with simplified dropdowns
    st.markdown("#### Configure Biomarker Parameters")
    
    intensity = st.selectbox(
        "Expression Intensity",
        intensity_options,
        index=0,
        key=f"{selected_biomarker}_intensity",
        help=f"Expression intensity for {selected_biomarker}"
    )
    
    staining = st.selectbox(
        "Staining Pattern",
        staining_options,
        index=0,
        key=f"{selected_biomarker}_staining",
        help=f"Staining pattern for {selected_biomarker}"
    )
    
    location = st.selectbox(
        "Cellular Location",
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
    
    # Display biomarker summary in single column
    st.markdown("#### 📊 Analysis Summary")
    
    if biomarker_data:
        marker_info = biomarker_data[selected_biomarker]
        st.success(f"""
        **🔬 {selected_biomarker} Configuration:**
        - **Intensity:** {marker_info['intensity']}
        - **Staining:** {marker_info['staining']}
        - **Location:** {marker_info['location']}
        """)
    
    return biomarker_data

def create_prediction_section(uploaded_file, image, biomarker_data):
    """Create prediction section with single column layout"""
    st.markdown("### 🎯 Run Prediction")
    st.markdown("Click the button below to analyze your sample using our AI model")
    
    # Single column button layout
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
            st.info("🔄 Processing... Please wait while we analyze your sample")
        
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        for i in range(100):
            progress_bar.progress(i + 1)
            if i < 30:
                status_text.text("🔍 Analyzing histopathological features...")
            elif i < 60:
                status_text.text("🧬 Processing biomarker data...")
            elif i < 90:
                status_text.text("🤖 Running AI prediction model...")
            else:
                status_text.text("📊 Generating results...")
            time.sleep(0.02)
        
        progress_bar.empty()
        status_text.empty()
        
        # Simulate prediction results
        prediction_score = np.random.uniform(0.1, 0.9)
        prediction_class = "Malignant" if prediction_score > 0.5 else "Benign"
        confidence = prediction_score if prediction_score > 0.5 else (1 - prediction_score)
        
        # Display results in single column
        st.markdown("### 📊 Analysis Results")
        
        if prediction_class == "Malignant":
            st.error(f"⚠️ **Prediction:** {prediction_class}")
        else:
            st.success(f"✅ **Prediction:** {prediction_class}")
        
        st.metric("Confidence Score", f"{confidence:.2%}")
        
        # Biomarker visualization in single column
        try:
            fig = create_biomarker_radar(biomarker_data)
            if fig:
                st.plotly_chart(fig, use_container_width=True)
        except:
            fig = create_biomarker_radar_fallback(biomarker_data)
            if fig:
                st.plotly_chart(fig, use_container_width=True)
        
        # Additional analysis details
        st.markdown("#### 🔍 Detailed Analysis")
        
        selected_marker = list(biomarker_data.keys())[0]
        marker_info = biomarker_data[selected_marker]
        
        st.info(f"""
        **Analysis Summary:**
        - **Biomarker:** {selected_marker}
        - **Expression Level:** {marker_info['intensity']}
        - **Staining Quality:** {marker_info['staining']}
        - **Cellular Localization:** {marker_info['location']}
        - **Risk Assessment:** {'High' if prediction_class == 'Malignant' else 'Low'}
        """)
        
        return True
    
    return False

def main():
    """Main application function with single column layout"""
    st.title("🔬 Breast Cancer AI Analysis")
    st.markdown("Advanced histopathological analysis using artificial intelligence")
    
    # Navigation
    try:
        st.markdown(create_navigation_bar(), unsafe_allow_html=True)
    except:
        pass
    
    # Main content in single column layout
    st.markdown("---")
    
    # Upload section
    uploaded_file, image = create_upload_section()
    
    st.markdown("---")
    
    # Biomarker section
    biomarker_data = create_biomarker_section()
    
    st.markdown("---")
    
    # Prediction section
    create_prediction_section(uploaded_file, image, biomarker_data)
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #666; padding: 2rem;'>
    <p>🏥 Breast Cancer AI Analysis System</p>
    <p>For research and educational purposes only</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
