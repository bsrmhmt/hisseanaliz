import streamlit as st

# --- Modülleri İçe Aktar ---
from backend.data_loader import DataLoader
from backend.indicators import TechnicalEngine
from ai_engine.predictor import AIPredictor
from ai_engine.risk import RiskManager
from frontend.styles import load_css
from frontend.interface import render_sidebar, render_landing_page, render_dashboard, render_risk_page

# --- Sayfa Ayarı ---
st.set_page_config(page_title="AI Finans Pro Modular", layout="wide")

def main():
    # 1. Stilleri Yükle
    load_css()
    
    # 2. Menüyü Çiz ve Seçimi Al
    page, vade_gun = render_sidebar()
    
    # 3. Sayfa Yönlendirmesi
    if page == "Ana Sayfa":
        render_landing_page()
        
    elif page == "Analiz Terminali":
        st.title("📊 Piyasa Analiz Terminali")
        
        c1, c2 = st.columns([3, 1])
        with c1: sembol = st.text_input("Hisse Kodu:", "THYAO")
        with c2: 
            st.write(""); st.write("")
            btn = st.button("🔍 ANALİZ ET", use_container_width=True)
            
        if btn:
            full_symbol = sembol.upper() + ".IS" if not sembol.endswith(".IS") else sembol.upper()
            
            with st.spinner("AI Motorları Çalışıyor..."):
                # A. Veri Çek (Backend)
                loader = DataLoader()
                hist, info = loader.get_data(full_symbol)
                
                if hist is None:
                    st.error("Veri bulunamadı!")
                    return
                
                # B. İndikatör Ekle (Backend)
                tech = TechnicalEngine()
                df = tech.add_all_indicators(hist)
                
                # C. Tahmin Yap (AI Engine)
                brain = AIPredictor()
                pred, conf = brain.predict(df, horizon=vade_gun)
                
                # D. Ekrana Bas (Frontend)
                render_dashboard(df, pred, conf, full_symbol)

    elif page == "Risk Merkezi":
        st.title("🛡️ Risk Analiz Merkezi")
        
        c1, c2 = st.columns([3, 1])
        with c1: sembol = st.text_input("Risk Analizi İçin Hisse:", "ASELS")
        with c2: 
            st.write(""); st.write("")
            btn = st.button("HESAPLA", use_container_width=True)
            
        if btn:
            full_symbol = sembol.upper() + ".IS" if not sembol.endswith(".IS") else sembol.upper()
            
            with st.spinner("Risk Metrikleri Hesaplanıyor..."):
                # A. Veri Çek
                loader = DataLoader()
                hist, _ = loader.get_data(full_symbol)
                
                if hist is not None:
                    # B. Riski Hesapla (AI Engine)
                    risk_mgr = RiskManager()
                    metrics = risk_mgr.calculate_metrics(hist)
                    
                    # C. Ekrana Bas (Frontend)
                    render_risk_page(metrics)
                else:
                    st.error("Veri yok.")

if __name__ == "__main__":
    main()
