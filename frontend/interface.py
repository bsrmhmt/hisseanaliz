# frontend/interface.py
import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def render_sidebar():
    with st.sidebar:
        st.title("🎛️ Kontrol Paneli")
        page = st.radio("Menü", ["Ana Sayfa", "Analiz Terminali", "Risk Merkezi"])
        st.markdown("---")
        if page == "Analiz Terminali":
            st.subheader("⚙️ Ayarlar")
            vade = st.slider("Tahmin Vadesi (Gün)", 1, 30, 5)
            return page, vade
        return page, 5

def render_landing_page():
    st.markdown('<div class="main-title">AI Finans Pro</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">Yapay Zeka Destekli Modüler Borsa Asistanı</div>', unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="feature-card"><div class="card-icon">🧠</div><div class="card-title">Yapay Zeka</div><div class="card-desc">Random Forest ve ML algoritmaları ile fiyat tahmini.</div></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="feature-card"><div class="card-icon">🛡️</div><div class="card-title">Risk Analizi</div><div class="card-desc">VaR, Volatilite ve Drawdown hesaplamaları.</div></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="feature-card"><div class="card-icon">📊</div><div class="card-title">Teknik Analiz</div><div class="card-desc">Otomatik indikatör yorumlama ve sinyaller.</div></div>', unsafe_allow_html=True)

def render_dashboard(df, prediction, confidence, sembol):
    # Metrikler
    current_price = df['Close'].iloc[-1]
    prev_price = df['Close'].iloc[-2]
    degisim = ((current_price - prev_price) / prev_price) * 100
    
    st.markdown(f"### 🏆 {sembol} Analiz Raporu")
    
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Fiyat", f"{current_price:.2f} TL", f"%{degisim:.2f}")
    c2.metric("RSI", f"{df['RSI'].iloc[-1]:.1f}")
    c3.metric("AI Hedef (T+5)", f"{prediction:.2f} TL")
    c4.metric("Güven Aralığı", f"±{confidence:.2f}")
    
    # Grafik
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, row_heights=[0.7, 0.3], vertical_spacing=0.05)
    fig.add_trace(go.Candlestick(x=df.index, open=df['Open'], high=df['High'], low=df['Low'], close=df['Close'], name='Fiyat'), row=1, col=1)
    fig.add_trace(go.Scatter(x=df.index, y=df['SMA_50'], name='SMA 50', line=dict(color='orange')), row=1, col=1)
    fig.add_trace(go.Scatter(x=df.index, y=df['SMA_200'], name='SMA 200', line=dict(color='blue')), row=1, col=1)
    fig.add_trace(go.Bar(x=df.index, y=df['Volume'], name='Hacim'), row=2, col=1)
    
    fig.update_layout(height=600, xaxis_rangeslider_visible=False, template="plotly_white")
    st.plotly_chart(fig, use_container_width=True)

def render_risk_page(metrics):
    st.title("🛡️ Risk Raporu")
    k1, k2, k3 = st.columns(3)
    k1.metric("Yıllık Volatilite", f"%{metrics['volatility']:.2f}")
    k2.metric("VaR (%95 Güven)", f"%{metrics['var_95']:.2f}", "En Kötü Gün")
    k3.metric("Max Drawdown", f"%{metrics['max_drawdown']:.2f}", "Zirveden Düşüş")
    
    st.subheader("📉 Drawdown (Zirveden Kayıp) Grafiği")
    st.line_chart(metrics['drawdown_series'])
