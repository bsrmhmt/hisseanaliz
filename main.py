# main.py
import streamlit as st
# İleride buraya frontend modüllerini import edeceğiz

# Sayfa Ayarı (Tüm uygulama için tek seferlik)
st.set_page_config(
    page_title="AI Finans Pro V2", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

def main():
    st.title("🚧 Sistem İnşa Aşamasında...")
    st.info("Backend servisleri bağlanıyor.")

if __name__ == "__main__":
    main()
