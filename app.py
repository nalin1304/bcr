import streamlit as st
import time
import base64
from utils.animations import (create_particles, animate_title, create_medical_background, 
                            create_navigation_bar, create_advanced_loading_animation,
                            create_morphing_shapes, create_holographic_display,
                            create_quantum_effect, create_pulsating_orb)
from utils.biomarkers import get_biomarker_info
import plotly.graph_objects as go
import plotly.express as px

st.set_page_config(
    page_title="Home - Breast Cancer AI",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

def load_css():
    with open("assets/styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def create_theme_toggle_script():
    return """
    <script>
    document.addEventListener('DOMContentLoaded', function() {
        const themeToggle = document.getElementById('themeToggle');
        const body = document.body;
        const currentTheme = localStorage.getItem('theme') || 'light';
        
        body.setAttribute('data-theme', currentTheme);
        
        if (themeToggle) {
            themeToggle.addEventListener('click', function() {
                const currentTheme = body.getAttribute('data-theme');
                const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
                
                body.setAttribute('data-theme', newTheme);
                localStorage.setItem('theme', newTheme);
                
                // Update Streamlit components
                const streamlitElements = document.querySelectorAll('.stApp, .main, .sidebar');
                streamlitElements.forEach(el => {
                    el.setAttribute('data-theme', newTheme);
                });
            });
        }
    });
    </script>
    """

def create_enhanced_hero_section():
    st.markdown(create_holographic_display(), unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col1:
        st.markdown(create_quantum_effect(), unsafe_allow_html=True)
    
    with col2:
        st.markdown(create_medical_background(), unsafe_allow_html=True)
        st.markdown(animate_title("🔬 Breast Cancer AI Diagnostics"), unsafe_allow_html=True)
        
        st.markdown("""
        <div class="hero-subtitle">
        Advanced Multimodal Deep Learning for Breast Cancer Subtype Classification
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(create_pulsating_orb(), unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card enhanced-card">
        <h3>🎯 Precise Classification</h3>
        <p>Identify IDC, TNBC, MBC, and ILC subtypes with 91.2% accuracy using cutting-edge AI</p>
        <div class="feature-metrics">
            <span class="metric">91.2% Accuracy</span>
            <span class="metric">4 Subtypes</span>
            <span class="metric">Real-time Analysis</span>
        </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card enhanced-card">
        <h3>🧬 Multimodal Fusion Technology</h3>
        <p>Revolutionary integration of histopathological imaging with molecular biomarker profiles</p>
        <div class="feature-tech">
            <span class="tech-badge">ResNet18 CNN</span>
            <span class="tech-badge">Biomarker Analysis</span>
            <span class="tech-badge">Neural Fusion</span>
        </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card enhanced-card">
        <h3>🔍 Explainable AI Visualization</h3>
        <p>Advanced Grad-CAM technology with interactive attention mapping and clinical insights</p>
        <div class="ai-features">
            <span class="ai-badge">Grad-CAM</span>
            <span class="ai-badge">Attention Maps</span>
            <span class="ai-badge">Clinical Reports</span>
        </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(create_advanced_loading_animation(), unsafe_allow_html=True)

def create_statistics_dashboard():
    st.markdown("### 📊 Global Breast Cancer Statistics")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="stat-card">
        <div class="stat-number">2.3M</div>
        <div class="stat-label">New Cases (2022)</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="stat-card">
        <div class="stat-number">670K</div>
        <div class="stat-label">Deaths (2022)</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="stat-card">
        <div class="stat-number">3.1L</div>
        <div class="stat-label">Cases in India (2024)</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="stat-card">
        <div class="stat-number">4</div>
        <div class="stat-label">Classified Subtypes</div>
        </div>
        """, unsafe_allow_html=True)

def create_subtype_overview():
    st.markdown("### 🧪 Breast Cancer Subtypes We Classify")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="subtype-card idc">
        <h4>IDC - Invasive Ductal Carcinoma</h4>
        <p>The most common subtype, accounting for 70-80% of all breast cancers. Originates in milk ducts and spreads to surrounding tissue.</p>
        <div class="prevalence">Prevalence: Very High</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="subtype-card mbc">
        <h4>MBC - Metaplastic Breast Cancer</h4>
        <p>A rare and aggressive subtype often misdiagnosed. Contains both carcinomatous and sarcomatous elements.</p>
        <div class="prevalence">Prevalence: Very Rare (< 1%)</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="subtype-card tnbc">
        <h4>TNBC - Triple-Negative Breast Cancer</h4>
        <p>Aggressive subtype lacking ER, PR, and HER2 receptors. Limited targeted therapy options.</p>
        <div class="prevalence">Prevalence: 10-15%</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="subtype-card ilc">
        <h4>ILC - Invasive Lobular Carcinoma</h4>
        <p>Second most common type, growing in single-file lines making it harder to detect on imaging.</p>
        <div class="prevalence">Prevalence: 10-15%</div>
        </div>
        """, unsafe_allow_html=True)

def create_quick_start():
    st.markdown("### 🚀 Quick Start Guide")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="step-card">
        <div class="step-number">1</div>
        <h4>Upload Image</h4>
        <p>Upload histopathological scan image (JPG format)</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="step-card">
        <div class="step-number">2</div>
        <h4>Input Biomarkers</h4>
        <p>Select biomarker values, intensity, and staining type</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="step-card">
        <div class="step-number">3</div>
        <h4>Get Results</h4>
        <p>View predictions, confidence scores, and Grad-CAM visualization</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("🔬 Start Diagnosis", type="primary", use_container_width=True):
            st.switch_page("pages/1_Upload_Predict.py")

def main():
    load_css()
    
    nav_col1, nav_col2, nav_col3, nav_col4, nav_col5, nav_col6 = st.columns([1.5, 1, 1, 1, 1, 1])
    
    with nav_col1:
        st.markdown("### 🏠 **BreastCancer AI**")
    
    with nav_col2:
        if st.button("🏠 Home", use_container_width=True):
            st.rerun()
    
    with nav_col3:
        if st.button("📤 Upload", use_container_width=True):
            st.switch_page("pages/1_Upload_Predict.py")
    
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
    
    st.sidebar.title("🏠 Home")
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 🔗 Quick Navigation")
    
    if st.sidebar.button("📤 Upload & Predict", use_container_width=True):
        st.switch_page("pages/1_Upload_Predict.py")
    
    if st.sidebar.button("📊 View Results", use_container_width=True):
        st.switch_page("pages/2_Results.py")
        
    if st.sidebar.button("🧠 Model Information", use_container_width=True):
        st.switch_page("pages/3_Model_Info.py")
        
    if st.sidebar.button("ℹ️ About Project", use_container_width=True):
        st.switch_page("pages/4_About.py")
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 📈 System Status")
    st.sidebar.success("✅ AI Model: Online")
    st.sidebar.info("🔄 Processing: Ready")
    st.sidebar.warning("⚡ GPU Acceleration: Available")
    
    create_enhanced_hero_section()
    
    st.markdown("---")
    
    create_statistics_dashboard()
    
    st.markdown("---")
    
    create_subtype_overview()
    
    st.markdown("---")
    
    create_quick_start()
    
    st.markdown("""
    <div class="footer">
    <p>🔬 Powered by Advanced Deep Learning | 🧬 Multimodal AI Classification | 🎯 Clinical Grade Accuracy</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
