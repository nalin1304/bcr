import pandas as pd

def get_all_biomarkers():
    return ['Ki-67', 'HER2', 'EGFR', 'TP53', 'CDH1', 'PTEN', 'BRCA1', 'RB1', 'ESR1']

def get_biomarker_details(marker):
    details = {
        'Ki-67': 'Proliferation marker - indicates cell division rate and tumor aggressiveness',
        'HER2': 'Human Epidermal Growth Factor Receptor 2 - target for specific therapies',
        'EGFR': 'Epidermal Growth Factor Receptor - associated with aggressive behavior',
        'TP53': 'Tumor suppressor gene - mutations common in aggressive cancers',
        'CDH1': 'E-cadherin adhesion protein - loss associated with invasive lobular carcinoma',
        'PTEN': 'Phosphatase tumor suppressor - regulates cell growth and survival',
        'BRCA1': 'DNA repair gene - mutations increase cancer susceptibility',
        'RB1': 'Retinoblastoma tumor suppressor - controls cell cycle progression',
        'ESR1': 'Estrogen receptor alpha - determines hormone sensitivity'
    }
    return details.get(marker, 'Important biomarker for cancer classification')

def get_biomarker_info():
    return {
        'Ki-67': {
            'full_name': 'Ki-67 Proliferation Marker',
            'function': 'Cell proliferation index',
            'clinical_significance': 'High Ki-67 indicates rapid tumor growth and poor prognosis',
            'normal_range': '< 14% (low), 14-30% (intermediate), > 30% (high)',
            'subtypes': {
                'IDC': 'Variable expression',
                'TNBC': 'Typically high (>30%)',
                'MBC': 'Often elevated',
                'ILC': 'Usually lower than IDC'
            }
        },
        'HER2': {
            'full_name': 'Human Epidermal Growth Factor Receptor 2',
            'function': 'Growth factor receptor',
            'clinical_significance': 'Target for trastuzumab and other HER2-targeted therapies',
            'normal_range': '0-1+ (negative), 2+ (equivocal), 3+ (positive)',
            'subtypes': {
                'IDC': '15-20% are HER2+',
                'TNBC': 'Negative by definition',
                'MBC': 'Rarely positive',
                'ILC': '5-10% are HER2+'
            }
        },
        'EGFR': {
            'full_name': 'Epidermal Growth Factor Receptor',
            'function': 'Cell growth and survival signaling',
            'clinical_significance': 'Associated with aggressive behavior and poor prognosis',
            'normal_range': 'Negative (0-1+), Positive (2-3+)',
            'subtypes': {
                'IDC': 'Variable expression',
                'TNBC': 'Frequently overexpressed',
                'MBC': 'Often highly expressed',
                'ILC': 'Usually negative'
            }
        }
    }

def encode_biomarker_data(biomarker_data):
    intensity_mapping = {'Weak': 1, 'Moderate': 2, 'Strong': 3}
    staining_mapping = {'Nuclear': 1, 'Cytoplasmic': 2, 'Membranous': 3}
    
    encoded_data = []
    
    for marker, data in biomarker_data.items():
        intensity_encoded = intensity_mapping[data['intensity']]
        staining_encoded = staining_mapping[data['staining']]
        
        encoded_data.extend([intensity_encoded, staining_encoded])
    
    return encoded_data

def get_biomarker_patterns():
    return {
        'IDC': {
            'Ki-67': 'Moderate to Strong',
            'HER2': 'Variable',
            'EGFR': 'Variable',
            'TP53': 'Variable',
            'ESR1': 'Often Positive'
        },
        'TNBC': {
            'Ki-67': 'Strong',
            'HER2': 'Negative',
            'EGFR': 'Strong',
            'TP53': 'Strong',
            'ESR1': 'Negative'
        },
        'MBC': {
            'Ki-67': 'Strong',
            'HER2': 'Usually Negative',
            'EGFR': 'Strong',
            'TP53': 'Strong',
            'ESR1': 'Variable'
        },
        'ILC': {
            'Ki-67': 'Weak to Moderate',
            'CDH1': 'Negative/Loss',
            'ESR1': 'Usually Positive',
            'PTEN': 'Variable',
            'HER2': 'Usually Negative'
        }
    }
