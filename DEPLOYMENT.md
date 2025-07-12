# Deployment Instructions

## 🚀 GitHub Repository Setup

### Step 1: Create GitHub Repository

1. Go to [GitHub.com](https://github.com) and sign in
2. Click the "+" icon → "New repository"
3. Repository name: `breast-cancer-ai-diagnostics`
4. Description: `Advanced Multimodal Deep Learning for Breast Cancer Subtype Classification`
5. Make it **Public** (required for Streamlit Cloud free tier)
6. Initialize with README: **No** (we already have one)
7. Click "Create repository"

### Step 2: Upload Code to GitHub

**Option A: Using Git Command Line**
```bash
# Navigate to your project directory
cd /path/to/BreastCancerInsight

# Initialize git repository
git init

# Add all files
git add .

# Commit files
git commit -m "Initial commit: Breast Cancer AI Diagnostics"

# Add remote repository (replace 'username' with your GitHub username)
git remote add origin https://github.com/username/breast-cancer-ai-diagnostics.git

# Push to GitHub
git branch -M main
git push -u origin main
```

**Option B: Using GitHub Web Interface**
1. On your new repository page, click "uploading an existing file"
2. Drag and drop all your project files
3. Commit the files with message "Initial commit"

## 🌟 Streamlit Cloud Deployment

### Step 1: Access Streamlit Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Sign in with your GitHub account
3. Click "New app"

### Step 2: Deploy Your App

1. **Repository**: Select `username/breast-cancer-ai-diagnostics`
2. **Branch**: `main`
3. **Main file path**: `app.py`
4. **App URL**: Choose a custom URL like `breastcancer-ai-diagnostics`

### Step 3: Configure Advanced Settings (Optional)

```toml
[theme]
primaryColor = "#FF6B9D"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0F2F6"
textColor = "#262730"
font = "sans serif"

[server]
headless = true
port = 8501
enableCORS = false
```

### Step 4: Deploy

1. Click "Deploy!"
2. Wait for deployment (usually 2-5 minutes)
3. Your app will be available at: `https://breastcancer-ai-diagnostics.streamlit.app`

## 🔧 Local Development

### Prerequisites
- Python 3.11+
- pip package manager

### Installation
```bash
# Clone the repository
git clone https://github.com/username/breast-cancer-ai-diagnostics.git
cd breast-cancer-ai-diagnostics

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
```

### Access
- Open your browser and go to `http://localhost:8501`

## 📊 Project Structure
```
breast-cancer-ai-diagnostics/
├── app.py                          # Main Streamlit application
├── requirements.txt                # Python dependencies
├── README.md                       # Project documentation
├── LICENSE                         # MIT License
├── .streamlit/
│   └── config.toml                # Streamlit configuration
├── assets/
│   └── styles.css                 # Custom CSS styles
├── pages/
│   ├── 1_Upload_Predict.py        # Upload and prediction page
│   ├── 2_Results.py               # Results visualization page
│   ├── 3_Model_Info.py            # Model information page
│   └── 4_About.py                 # About and team page
└── utils/
    ├── animations.py              # UI animations and effects
    ├── biomarkers.py              # Biomarker data processing
    └── visualizations.py          # Data visualization functions
```

## 🌐 Live Demo Links

After deployment, your application will be available at:
- **Streamlit Cloud**: `https://breastcancer-ai-diagnostics.streamlit.app`
- **GitHub Repository**: `https://github.com/username/breast-cancer-ai-diagnostics`

## 🔄 Updates and Maintenance

### Updating the Application
1. Make changes to your local code
2. Commit and push to GitHub:
   ```bash
   git add .
   git commit -m "Description of changes"
   git push origin main
   ```
3. Streamlit Cloud will automatically redeploy your app

### Managing Dependencies
- Update `requirements.txt` when adding new packages
- Streamlit Cloud will automatically install dependencies on deployment

## 📱 Sharing Your Application

Share these links:
- **Live App**: `https://breastcancer-ai-diagnostics.streamlit.app`
- **Source Code**: `https://github.com/username/breast-cancer-ai-diagnostics`
- **Documentation**: Include this in your README.md

## ⚠️ Important Notes

1. **Free Tier Limitations**:
   - Repository must be public
   - 1GB of resources per app
   - Apps sleep after 7 days of inactivity

2. **File Size Limits**:
   - Individual files: 100MB max
   - Total repository: 1GB max

3. **Security**:
   - Never commit API keys or sensitive data
   - Use Streamlit secrets for sensitive configuration

## 🆘 Troubleshooting

### Common Issues:

1. **App won't start**: Check requirements.txt and Python version compatibility
2. **Import errors**: Ensure all dependencies are in requirements.txt
3. **Slow loading**: Optimize large files or use caching with `@st.cache_data`

### Getting Help:
- Streamlit Documentation: [docs.streamlit.io](https://docs.streamlit.io)
- Community Forum: [discuss.streamlit.io](https://discuss.streamlit.io)
- GitHub Issues: Report bugs in your repository's Issues tab
