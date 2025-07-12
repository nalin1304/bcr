import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from utils.animations import (create_team_animation, create_timeline_animation, create_navigation_bar,
                            create_particles, create_morphing_shapes, create_holographic_display,
                            create_pulsating_orb, create_advanced_loading_animation)

st.set_page_config(
    page_title="About - Breast Cancer AI",
    page_icon="ℹ️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

def load_css():
    with open("assets/styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def create_project_overview():
    st.markdown("### 🔬 Project Overview")
    st.markdown("""
    <div style="margin-bottom: 1.5rem;">
    <p style="color: #4a5568;">Learn about our innovative approach to breast cancer diagnosis using cutting-edge AI technology</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        <div class="project-overview">
        <h4>🎯 Mission Statement</h4>
        <p>To develop an advanced AI-powered diagnostic system that combines histopathological imaging with biomarker analysis for accurate breast cancer subtype classification, enabling earlier detection and personalized treatment strategies.</p>
        
        <h4>🔬 Scientific Approach</h4>
        <p>Our multimodal deep learning model integrates Computer Vision and Machine Learning techniques to analyze both visual morphological features and molecular biomarker profiles, providing comprehensive diagnostic insights that surpass traditional single-modality approaches.</p>
        
        <h4>🌍 Global Impact</h4>
        <p>With over 2.3 million new breast cancer cases worldwide annually, our system aims to democratize access to advanced diagnostic capabilities, particularly in underserved regions where specialized pathology expertise may be limited.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="impact-metrics">
        <h4>📊 Potential Impact</h4>
        <div class="metric-item">
        <div class="metric-number">91.2%</div>
        <div class="metric-label">Classification Accuracy</div>
        </div>
        <div class="metric-item">
        <div class="metric-number">4</div>
        <div class="metric-label">Cancer Subtypes</div>
        </div>
        <div class="metric-item">
        <div class="metric-number">15K+</div>
        <div class="metric-label">Training Samples</div>
        </div>
        <div class="metric-item">
        <div class="metric-number">9</div>
        <div class="metric-label">Key Biomarkers</div>
        </div>
        </div>
        """, unsafe_allow_html=True)

def create_team_section():
    st.markdown("### 👥 Development Team")
    
    team_members = [
        {
            "name": "Shaanvi Karri",
            "role": "Team Lead & AI/ML Developer",
            "uid": "1003578670",
            "expertise": "Deep Learning, Computer Vision, Project Management",
            "contribution": "Model architecture design, team coordination"
        },
        {
            "name": "Nalin Aggarwal",
            "role": "Frontend Developer",
            "uid": "1008244308",
            "expertise": "Web Development, UI/UX Design, User Experience",
            "contribution": "User interface design, frontend development"
        },
        {
            "name": "Aaryan Mulaye",
            "role": "AI/ML Developer",
            "uid": "1008205574",
            "expertise": "Machine Learning, Data Processing, Algorithm Optimization",
            "contribution": "Model training, performance optimization"
        },
        {
            "name": "Anjali Desai",
            "role": "AI/ML Developer",
            "uid": "1000512287",
            "expertise": "Neural Networks, Feature Engineering, Validation",
            "contribution": "Model validation, feature selection"
        },
        {
            "name": "Arnav Dhiman",
            "role": "AI/ML Developer",
            "uid": "1008255361",
            "expertise": "Deep Learning, Image Processing, Model Evaluation",
            "contribution": "Image preprocessing, model evaluation"
        },
        {
            "name": "Misty Raj",
            "role": "Research & Data Collection",
            "uid": "1008241231",
            "expertise": "Biomedical Research, Data Curation, Literature Review",
            "contribution": "Dataset collection, research documentation"
        },
        {
            "name": "Roumak Das",
            "role": "AI/ML Developer",
            "uid": "1008164407",
            "expertise": "Machine Learning, Statistical Analysis, Data Science",
            "contribution": "Statistical analysis, model interpretation"
        },
        {
            "name": "Rudra Narayan",
            "role": "Research & Data Collection",
            "uid": "1008204049",
            "expertise": "Biomarker Analysis, Medical Research, Data Validation",
            "contribution": "Biomarker research, data validation"
        },
        {
            "name": "Sarah Josephine",
            "role": "Research & Data Collection",
            "uid": "1008239080",
            "expertise": "Cancer Biology, Pathology Research, Clinical Data",
            "contribution": "Clinical research, pathology expertise"
        }
    ]
    
    st.markdown(create_team_animation(), unsafe_allow_html=True)
    
    for i in range(0, len(team_members), 3):
        cols = st.columns(3)
        for j, col in enumerate(cols):
            if i + j < len(team_members):
                member = team_members[i + j]
                with col:
                    st.markdown(f"""
                    <div class="team-card">
                    <div class="team-avatar">👤</div>
                    <h4>{member['name']}</h4>
                    <div class="team-role">{member['role']}</div>
                    <div class="team-uid">ID: {member['uid']}</div>
                    <div class="team-expertise">
                    <strong>Expertise:</strong><br>
                    {member['expertise']}
                    </div>
                    <div class="team-contribution">
                    <strong>Key Contribution:</strong><br>
                    {member['contribution']}
                    </div>
                    </div>
                    """, unsafe_allow_html=True)

def create_project_timeline():
    st.markdown("### 📅 Project Timeline")
    
    st.markdown(create_timeline_animation(), unsafe_allow_html=True)
    
    phases = [
        {
            "phase": "Phase 1",
            "title": "Background Research & Dataset Identification",
            "duration": "Weeks 1-2",
            "status": "✅ Completed",
            "details": "Literature review, dataset collection, project planning"
        },
        {
            "phase": "Phase 2",
            "title": "Data Preprocessing & Biomarker Mapping",
            "duration": "Weeks 3-4",
            "status": "✅ Completed",
            "details": "Data cleaning, biomarker analysis, preprocessing pipelines"
        },
        {
            "phase": "Phase 3",
            "title": "Model Development & Testing",
            "duration": "Weeks 5-7",
            "status": "✅ Completed",
            "details": "CNN architecture, multimodal fusion, validation testing"
        },
        {
            "phase": "Phase 4",
            "title": "UI Development & Integration",
            "duration": "Weeks 8-10",
            "status": "✅ Completed",
            "details": "Frontend development, model integration, user testing"
        },
        {
            "phase": "Phase 5",
            "title": "Final Report & Presentation",
            "duration": "Weeks 11-12",
            "status": "🔄 In Progress",
            "details": "Documentation, presentation preparation, final validation"
        }
    ]
    
    for phase in phases:
        st.markdown(f"""
        <div class="timeline-card">
        <div class="timeline-phase">{phase['phase']}</div>
        <div class="timeline-content">
        <h4>{phase['title']}</h4>
        <div class="timeline-duration">{phase['duration']}</div>
        <div class="timeline-status">{phase['status']}</div>
        <p>{phase['details']}</p>
        </div>
        </div>
        """, unsafe_allow_html=True)

def create_technical_achievements():
    st.markdown("### 🏆 Technical Achievements")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="achievement-section">
        <h4>🧠 AI/ML Innovations</h4>
        <ul>
        <li>✨ Novel multimodal fusion architecture</li>
        <li>🎯 91.2% classification accuracy</li>
        <li>🔍 Grad-CAM interpretability integration</li>
        <li>⚖️ Balanced handling of rare cancer subtypes</li>
        <li>🚀 Real-time inference capabilities</li>
        <li>📊 Comprehensive biomarker analysis</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="achievement-section">
        <h4>💻 Software Engineering</h4>
        <ul>
        <li>🌐 Responsive web application</li>
        <li>🎨 Interactive data visualizations</li>
        <li>📱 Mobile-friendly interface</li>
        <li>⚡ Optimized performance</li>
        <li>🔒 Secure data handling</li>
        <li>📄 Automated report generation</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

def create_research_contributions():
    st.markdown("### 📚 Research Contributions")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="research-card">
        <h4>🔬 Scientific Publications</h4>
        <div class="publication">
        <h5>"Multimodal Deep Learning for Breast Cancer Subtype Classification"</h5>
        <p><em>In preparation for Medical Image Analysis Journal</em></p>
        </div>
        
        <div class="publication">
        <h5>"Biomarker Integration in Histopathological AI Systems"</h5>
        <p><em>Conference paper submitted to MICCAI 2025</em></p>
        </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="research-card">
        <h4>🎓 Academic Impact</h4>
        <ul>
        <li>📖 Novel dataset compilation methodology</li>
        <li>🧬 Biomarker-image fusion techniques</li>
        <li>🎯 Rare subtype detection strategies</li>
        <li>🔍 Explainable AI in medical imaging</li>
        <li>📊 Clinical validation protocols</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

def create_future_directions():
    st.markdown("### 🚀 Future Directions")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="future-card">
        <h4>🔬 Research Extensions</h4>
        <ul>
        <li>Multi-institutional validation</li>
        <li>Genomic data integration</li>
        <li>Treatment response prediction</li>
        <li>Survival outcome modeling</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="future-card">
        <h4>💻 Technical Enhancements</h4>
        <ul>
        <li>3D histology analysis</li>
        <li>Real-time streaming</li>
        <li>Mobile app development</li>
        <li>Cloud deployment</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="future-card">
        <h4>🏥 Clinical Integration</h4>
        <ul>
        <li>Hospital system integration</li>
        <li>Regulatory approval process</li>
        <li>Clinical workflow optimization</li>
        <li>Healthcare partnerships</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

def main():
    load_css()
    
    st.markdown("""
    <style>
    /* About page specific improvements */
    .team-card {
        background: linear-gradient(135deg, #ffffff, #f8fafc);
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        padding: 1.5rem;
        text-align: center;
        margin-bottom: 1rem;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    
    .team-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.15);
    }
    
    .team-avatar {
        font-size: 3rem;
        margin-bottom: 1rem;
    }
    
    .team-role {
        color: #FF6B9D;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }
    
    .team-uid {
        color: #4a5568;
        font-size: 0.9rem;
        margin-bottom: 1rem;
    }
    
    .achievement-section, .research-card, .future-card {
        background: linear-gradient(135deg, #f8fafc, #e2e8f0);
        border: 1px solid #d1d5db;
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 1rem;
    }
    
    .timeline-card {
        background: white;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        border-left: 4px solid #FF6B9D;
    }
    </style>
    """, unsafe_allow_html=True)
    
    
    nav_col1, nav_col2, nav_col3, nav_col4, nav_col5, nav_col6 = st.columns([1.5, 1, 1, 1, 1, 1])
    
    with nav_col1:
        st.markdown("### ℹ️ **BreastCancer AI**")
    
    with nav_col2:
        if st.button("🏠 Home", use_container_width=True):
            st.switch_page("app.py")
    
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
        if st.button("ℹ️ About", use_container_width=True, type="primary"):
            st.rerun()
    
    st.markdown("---")
    
    st.markdown(create_particles(), unsafe_allow_html=True)
    st.markdown(create_morphing_shapes(), unsafe_allow_html=True)
    
    st.sidebar.title("ℹ️ About Project")
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 🔗 Quick Navigation")
    
    if st.sidebar.button("🏠 Home", use_container_width=True):
        st.switch_page("app.py")
    
    if st.sidebar.button("📤 Upload & Predict", use_container_width=True):
        st.switch_page("pages/1_Upload_Predict.py")
        
    if st.sidebar.button("📊 View Results", use_container_width=True):
        st.switch_page("pages/2_Results.py")
        
    if st.sidebar.button("🧠 Model Information", use_container_width=True):
        st.switch_page("pages/3_Model_Info.py")
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 📊 Project Stats")
    st.sidebar.metric("Team Members", "9")
    st.sidebar.metric("Development Time", "12 weeks")
    st.sidebar.metric("Model Accuracy", "91.2%")
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 🎯 Quick Facts")
    st.sidebar.info("**Lead:** Shaanvi Karri")
    st.sidebar.info("**Frontend:** Nalin Aggarwal")
    st.sidebar.info("**Technology:** Multimodal AI")
    st.sidebar.success("**Status:** Complete")
    
    st.title("ℹ️ About Our Project")
    st.markdown("Learn about our innovative approach to breast cancer subtype classification using AI")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        st.markdown(create_pulsating_orb(), unsafe_allow_html=True)
    with col2:
        st.markdown(create_holographic_display(), unsafe_allow_html=True)
    with col3:
        st.markdown(create_advanced_loading_animation(), unsafe_allow_html=True)
    
    create_project_overview()
    
    st.markdown("---")
    
    create_team_section()
    
    st.markdown("---")
    
    create_project_timeline()
    
    st.markdown("---")
    
    create_technical_achievements()
    
    st.markdown("---")
    
    create_research_contributions()
    
    st.markdown("---")
    
    create_future_directions()
    
    st.markdown("""
    <div class="footer-about">
    <p>🎓 This project represents the culmination of extensive research and development in AI-powered medical diagnostics, combining cutting-edge technology with clinical expertise to advance breast cancer care.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
