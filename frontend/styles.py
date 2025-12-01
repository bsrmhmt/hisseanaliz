# frontend/styles.py
import streamlit as st

def load_css():
    st.markdown("""
        <style>
        /* Genel Ayarlar */
        .stApp {background-color: #ffffff; color: #333;}
        
        /* Başlıklar */
        .main-title {
            font-size: 3.5rem;
            font-weight: 800;
            background: linear-gradient(120deg, #2980b9, #8e44ad);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-align: center;
            margin-bottom: 10px;
        }
        .sub-title {
            font-size: 1.2rem;
            color: #666;
            text-align: center;
            margin-bottom: 40px;
        }
        
        /* Kart Tasarımı */
        .feature-card {
            background: #f8f9fa;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.05);
            text-align: center;
            border: 1px solid #eee;
            height: 220px;
            transition: transform 0.3s;
        }
        .feature-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 25px rgba(0,0,0,0.1);
        }
        .card-icon { font-size: 2.5rem; margin-bottom: 10px; }
        .card-title { font-weight: bold; font-size: 1.1rem; margin-bottom: 5px; color: #333; }
        .card-desc { font-size: 0.9rem; color: #666; }
        
        /* Metrik Kartları */
        .metric-card {
            background-color: white;
            border: 1px solid #e0e0e0;
            border-radius: 10px;
            padding: 15px;
            text-align: center;
            box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        }
        
        /* Butonlar */
        .stButton button {
            width: 100%;
            border-radius: 50px;
            height: 50px;
            font-weight: bold;
            border: none;
            transition: all 0.3s;
        }
        /* Özel Buton Renkleri için inline style kullanacağız */
        </style>
    """, unsafe_allow_html=True)
