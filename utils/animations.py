import streamlit as st

def create_enhanced_particles():
    return """
    <div class="enhanced-particles">
        <div class="particle-system">
            <div class="particle dna-particle"></div>
            <div class="particle cell-particle"></div>
            <div class="particle molecule-particle"></div>
            <div class="particle protein-particle"></div>
            <div class="particle antibody-particle"></div>
            <div class="particle virus-particle"></div>
            <div class="particle bacteria-particle"></div>
            <div class="particle chromosome-particle"></div>
            <div class="particle enzyme-particle"></div>
            <div class="particle hormone-particle"></div>
            <div class="particle neuron-particle"></div>
            <div class="particle blood-cell-particle"></div>
        </div>
        <div class="floating-medical-icons">
            <div class="medical-icon stethoscope">🩺</div>
            <div class="medical-icon microscope">🔬</div>
            <div class="medical-icon dna">🧬</div>
            <div class="medical-icon pill">💊</div>
            <div class="medical-icon syringe">💉</div>
            <div class="medical-icon heart">🫀</div>
            <div class="medical-icon brain">🧠</div>
            <div class="medical-icon test-tube">🧪</div>
        </div>
        <div class="energy-waves">
            <div class="wave wave-1"></div>
            <div class="wave wave-2"></div>
            <div class="wave wave-3"></div>
            <div class="wave wave-4"></div>
        </div>
    </div>
    """

def create_particles():
    return create_enhanced_particles()

def animate_title(title):
    return f"""
    <div class="animated-title">
    <h1>{title}</h1>
    </div>
    """

def create_medical_background():
    return """
    <div class="medical-background">
    <div class="dna-helix"></div>
    <div class="cell-structure"></div>
    <div class="molecular-bonds"></div>
    </div>
    """

def create_upload_animation():
    return """
    <div class="upload-animation">
    <div class="upload-cloud">
    <svg width="60" height="40" viewBox="0 0 60 40">
    <path d="M15 25 L45 25 L45 35 L15 35 Z" fill="#e0e0e0"/>
    <path d="M25 15 L35 15 L35 25 L25 25 Z" fill="#4CAF50"/>
    <path d="M29 10 L31 10 L31 20 L29 20 Z" fill="#4CAF50"/>
    <path d="M27 12 L29 10 L31 10 L33 12" stroke="#4CAF50" fill="none"/>
    </svg>
    </div>
    </div>
    """

def create_loading_animation():
    return """
    <div class="loading-container">
    <div class="dna-loader">
    <div class="strand strand1"></div>
    <div class="strand strand2"></div>
    </div>
    <p class="loading-text">Analyzing sample...</p>
    </div>
    """

def animate_prediction_card():
    return """
    <div class="prediction-animation">
    <div class="pulse-ring"></div>
    <div class="prediction-icon">🎯</div>
    </div>
    """

def create_confetti_animation():
    return """
    <div class="confetti-container">
    <div class="confetti"></div>
    <div class="confetti"></div>
    <div class="confetti"></div>
    <div class="confetti"></div>
    <div class="confetti"></div>
    </div>
    """

def create_model_animation():
    return """
    <div class="model-animation">
    <div class="network-node input"></div>
    <div class="network-connection"></div>
    <div class="network-node hidden"></div>
    <div class="network-connection"></div>
    <div class="network-node output"></div>
    </div>
    """

def animate_architecture_diagram():
    return """
    <div class="architecture-animation">
    <div class="data-flow">
    <div class="flow-arrow"></div>
    <div class="flow-arrow"></div>
    <div class="flow-arrow"></div>
    </div>
    </div>
    """

def create_team_animation():
    return """
    <div class="team-animation">
    <div class="collaboration-rings">
    <div class="ring ring1"></div>
    <div class="ring ring2"></div>
    <div class="ring ring3"></div>
    </div>
    </div>
    """

def create_timeline_animation():
    return """
    <div class="timeline-animation">
    <div class="timeline-progress"></div>
    <div class="timeline-markers">
    <div class="marker completed"></div>
    <div class="marker completed"></div>
    <div class="marker completed"></div>
    <div class="marker completed"></div>
    <div class="marker current"></div>
    </div>
    </div>
    """

def animate_result_card():
    return """
    <div class="result-animation">
    <div class="success-checkmark">
    <svg width="40" height="40" viewBox="0 0 40 40">
    <circle cx="20" cy="20" r="18" fill="none" stroke="#4CAF50" stroke-width="2"/>
    <path d="M12 20 L18 26 L28 14" stroke="#4CAF50" stroke-width="3" fill="none"/>
    </svg>
    </div>
    </div>
    """

def create_navigation_bar():
    return """
    <div class="professional-navbar">
        <div class="navbar-container">
            <div class="navbar-brand">
                <div class="brand-logo">
                    <svg width="40" height="40" viewBox="0 0 40 40" class="logo-svg">
                        <circle cx="20" cy="20" r="18" fill="none" stroke="url(#logoGradient)" stroke-width="2"/>
                        <path d="M15 18 L18 21 L25 14" stroke="url(#logoGradient)" stroke-width="2" fill="none"/>
                        <circle cx="20" cy="20" r="8" fill="none" stroke="url(#logoGradient)" stroke-width="1" opacity="0.5"/>
                        <defs>
                            <linearGradient id="logoGradient" x1="0%" y1="0%" x2="100%" y2="100%">
                                <stop offset="0%" style="stop-color:var(--primary-color);stop-opacity:1" />
                                <stop offset="100%" style="stop-color:var(--accent-color);stop-opacity:1" />
                            </linearGradient>
                        </defs>
                    </svg>
                </div>
                <div class="brand-text">
                    <span class="brand-main">BreastCancer AI</span>
                    <span class="brand-sub">Clinical Diagnostics Platform</span>
                </div>
            </div>
            
            <nav class="navbar-navigation">
                <div class="nav-links">
                    <a href="/" class="nav-link active" data-page="home">
                        <span class="nav-icon">🏠</span>
                        <span class="nav-text">Home</span>
                        <div class="nav-indicator"></div>
                    </a>
                    <a href="/Upload_Predict" class="nav-link" data-page="upload">
                        <span class="nav-icon">📤</span>
                        <span class="nav-text">Upload & Predict</span>
                        <div class="nav-indicator"></div>
                    </a>
                    <a href="/Results" class="nav-link" data-page="results">
                        <span class="nav-icon">📊</span>
                        <span class="nav-text">Results</span>
                        <div class="nav-indicator"></div>
                    </a>
                    <a href="/Model_Info" class="nav-link" data-page="model">
                        <span class="nav-icon">🧠</span>
                        <span class="nav-text">Model Information</span>
                        <div class="nav-indicator"></div>
                    </a>
                    <a href="/About" class="nav-link" data-page="about">
                        <span class="nav-icon">ℹ️</span>
                        <span class="nav-text">About</span>
                        <div class="nav-indicator"></div>
                    </a>
                </div>
            </nav>
            
            <div class="navbar-controls">
                <div class="system-status">
                    <div class="status-indicator online"></div>
                    <span class="status-text">System Online</span>
                </div>
                <button class="theme-toggle-btn" onclick="toggleTheme()">
                    <div class="toggle-icon">
                        <span class="light-mode">☀️</span>
                        <span class="dark-mode">🌙</span>
                    </div>
                </button>
            </div>
        </div>
        
        <div class="navbar-progress-bar">
            <div class="progress-indicator"></div>
        </div>
    </div>
    
    <script>
    function toggleTheme() {
        const body = document.body;
        const currentTheme = body.getAttribute('data-theme') || 'light';
        const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
        
        body.setAttribute('data-theme', newTheme);
        localStorage.setItem('theme', newTheme);
        
        // Update all Streamlit elements
        const streamlitApp = document.querySelector('.stApp');
        if (streamlitApp) {
            streamlitApp.setAttribute('data-theme', newTheme);
        }
        
        // Update other elements
        document.querySelectorAll('.main, .sidebar, [data-testid="stSidebar"]').forEach(el => {
            el.setAttribute('data-theme', newTheme);
        });
        
        // Animate theme transition
        document.body.style.transition = 'all 0.3s ease';
        setTimeout(() => {
            document.body.style.transition = '';
        }, 300);
    }
    
    // Initialize theme on page load
    document.addEventListener('DOMContentLoaded', function() {
        const savedTheme = localStorage.getItem('theme') || 'light';
        document.body.setAttribute('data-theme', savedTheme);
        
        const streamlitApp = document.querySelector('.stApp');
        if (streamlitApp) {
            streamlitApp.setAttribute('data-theme', savedTheme);
        }
        
        // Set active nav link based on current page
        const currentPath = window.location.pathname;
        document.querySelectorAll('.nav-link').forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href') === currentPath || 
                (currentPath === '/' && link.getAttribute('data-page') === 'home')) {
                link.classList.add('active');
            }
        });
    });
    </script>
    """

def create_advanced_loading_animation():
    return """
    <div class="advanced-loading-container">
        <div class="loading-brain">
            <div class="brain-hemisphere left">
                <div class="neural-network">
                    <div class="neuron n1"></div>
                    <div class="neuron n2"></div>
                    <div class="neuron n3"></div>
                    <div class="neuron n4"></div>
                    <div class="connection c1"></div>
                    <div class="connection c2"></div>
                    <div class="connection c3"></div>
                </div>
            </div>
            <div class="brain-hemisphere right">
                <div class="neural-network">
                    <div class="neuron n1"></div>
                    <div class="neuron n2"></div>
                    <div class="neuron n3"></div>
                    <div class="neuron n4"></div>
                    <div class="connection c1"></div>
                    <div class="connection c2"></div>
                    <div class="connection c3"></div>
                </div>
            </div>
            <div class="brain-waves">
                <div class="wave-line w1"></div>
                <div class="wave-line w2"></div>
                <div class="wave-line w3"></div>
            </div>
        </div>
        <div class="loading-text-advanced">
            <div class="text-cycle">
                <span class="cycle-text">Analyzing Neural Patterns...</span>
                <span class="cycle-text">Processing Image Features...</span>
                <span class="cycle-text">Evaluating Biomarkers...</span>
                <span class="cycle-text">Computing Predictions...</span>
                <span class="cycle-text">Generating Results...</span>
            </div>
        </div>
        <div class="data-stream">
            <div class="data-bit"></div>
            <div class="data-bit"></div>
            <div class="data-bit"></div>
            <div class="data-bit"></div>
            <div class="data-bit"></div>
        </div>
    </div>
    """

def create_morphing_shapes():
    return """
    <div class="morphing-shapes">
        <div class="shape shape-1"></div>
        <div class="shape shape-2"></div>
        <div class="shape shape-3"></div>
        <div class="shape shape-4"></div>
    </div>
    """

def create_holographic_display():
    return """
    <div class="holographic-display">
        <div class="holo-grid">
            <div class="grid-line horizontal"></div>
            <div class="grid-line horizontal"></div>
            <div class="grid-line horizontal"></div>
            <div class="grid-line vertical"></div>
            <div class="grid-line vertical"></div>
            <div class="grid-line vertical"></div>
        </div>
        <div class="holo-elements">
            <div class="holo-icon">🔬</div>
            <div class="holo-text">AI ANALYSIS</div>
            <div class="holo-indicator"></div>
        </div>
        <div class="scan-line"></div>
    </div>
    """

def create_quantum_effect():
    return """
    <div class="quantum-effect">
        <div class="quantum-particles">
            <div class="q-particle q1"></div>
            <div class="q-particle q2"></div>
            <div class="q-particle q3"></div>
            <div class="q-particle q4"></div>
            <div class="q-particle q5"></div>
        </div>
        <div class="quantum-field"></div>
    </div>
    """

def create_pulsating_orb():
    return """
    <div class="pulsating-orb-container">
        <div class="orb">
            <div class="orb-core"></div>
            <div class="orb-ring ring-1"></div>
            <div class="orb-ring ring-2"></div>
            <div class="orb-ring ring-3"></div>
        </div>
    </div>
    """
