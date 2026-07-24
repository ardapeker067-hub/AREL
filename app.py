import streamlit as st
from datetime import datetime, timedelta

# 1. Sayfa Ayarları
st.set_page_config(page_title="Sonsuz Aşkımıza ❤️", page_icon="💖", layout="centered")

# 2. CSS: Yan Panel, Arkaplan ve Kalpler
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Playfair+Display:ital,wght@1&display=swap');

    /* Arkaplan */
    [data-testid="stAppViewContainer"] {
        background: #fff5f7;
    }
    
    /* Yan Panel (Sidebar) Rengi */
    [data-testid="stSidebar"] {
        background-color: #ffebee;
        border-right: 2px solid #ffc1e3;
    }

    /* Kalpler */
    .heart-bg {
        position: fixed;
        top: -10%;
        color: #ff4081;
        font-size: 20px;
        user-select: none;
        z-index: 0;
        animation: fall linear infinite;
    }
    @keyframes fall {
        to { transform: translateY(110vh) rotate(360deg); }
    }

    /* Fotoğraf Kartları */
    .photo-card {
        margin-top: 50px;
        margin-bottom: 50px;
        padding: 15px;
        background: white;
        border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        text-align: center;
    }

    .romantic-text {
        font-family: 'Dancing Script', cursive;
        font-size: 30px;
        color: #ad1457;
    }

    /* SAĞDAKİ BİLET */
    .ticket-fixed {
        position: fixed;
        right: 10px;
        top: 20px;
        z-index: 9999;
    }
    .stButton>button {
        background: #ff4081;
        color: white;
        border: 2px dashed white;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# Kalp Yağmuru
for i in range(25):
    left = i * 4
    st.markdown(f'<div class="heart-bg" style="left:{left}%; animation-delay:{i*0.6}s; animation-duration:{7+i%3}s;">❤️</div>', unsafe_allow_html=True)

# --- 3. YAN PANEL (SOL TARAF) ---
st.sidebar.markdown("<h1 style='font-family: Dancing Script; color: #ad1457;'>📅 Anı Takvimi</h1>", unsafe_allow_html=True)
secim = st.sidebar.radio("Bir Yıl Seç Sevgilim:", ["Ana Sayfa", "2023", "2024", "2025"])

# --- 4. MÜZİK BİLETİ (Sağ Üstte) ---
if 'music_on' not in st.session_state:
    st.session_state.music_on = False

st.markdown('<div class="ticket-fixed">', unsafe_allow_html=True)
if st.button("🎫 Müzik"):
    st.session_state.music_on = not st.session_state.music_on
st.markdown('</div>', unsafe_allow_html=True)

if st.session_state.music_on:
    try:
        audio_file = open('sarki.mp3', 'rb')
        st.audio(audio_file.read(), format='audio/mp3')
    except:
        st.sidebar.warning("sarki.mp3 yüklenmemiş!")

# --- 5. İÇERİK YÖNETİMİ ---

if secim == "Ana Sayfa":
    st.markdown("<h1 style='text-align: center; font-family: Dancing Script; color: #ad1457; font-size: 55px;'>960 Günlük Hikayemiz</h1>", unsafe_allow_html=True)
    st.markdown('<div class="photo-card">', unsafe_allow_html=True)
    try:
        st.image("foto1.jpg", use_column_width=True, caption="Her şeyin başladığı o an...")
    except: st.write("foto1.jpg bekleniyor...")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("<h2 style='text-align:center; font-family: Dancing Script;'>Sol taraftaki menüden yıllara göz atabilirsin... ❤️</h2>", unsafe_allow_html=True)

elif secim == "2023":
    st.markdown("<h1 style='text-align: center; font-family: Dancing Script; color: #ad1457;'>✨ 2023 Anılarımız</h1>", unsafe_allow_html=True)
    # 2023 Fotoğrafları
    try:
        st.markdown('<div class="photo-card">', unsafe_allow_html=True)
        st.image("2023_1.jpg", use_column_width=True)
        st.write("2023'ün en güzel günü...")
        st.markdown('</div>', unsafe_allow_html=True)
    except: st.info("Bu yıla ait fotoğraf (2023_1.jpg) henüz yüklenmedi.")

elif secim == "2024":
    st.markdown("<h1 style='text-align: center; font-family: Dancing Script; color: #ad1457;'>🌟 2024 Anılarımız</h1>", unsafe_allow_html=True)
    try:
        st.markdown('<div class="photo-card">', unsafe_allow_html=True)
        st.image("2024_1.jpg", use_column_width=True)
        st.write("Birlikte ne kadar da eğlenmiştik!")
        st.markdown('</div>', unsafe_allow_html=True)
    except: st.info("Bu yıla ait fotoğraf (2024_1.jpg) henüz yüklenmedi.")

elif secim == "2025":
    st.markdown("<h1 style='text-align: center; font-family: Dancing Script; color: #ad1457;'>🚀 2025 ve Geleceğimiz</h1>", unsafe_allow_html=True)
    try:
        st.markdown('<div class="photo-card">', unsafe_allow_html=True)
        st.image("2025_1.jpg", use_column_width=True)
        st.write("Yeni yıl, yeni umutlar, hep seninle...")
        st.markdown('</div>', unsafe_allow_html=True)
    except: st.info("Bu yıla ait fotoğraf (2025_1.jpg) henüz yüklenmedi.")

# Final Balonları
if secim != "Ana Sayfa":
    st.balloons()
