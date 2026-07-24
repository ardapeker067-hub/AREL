import streamlit as st
from datetime import datetime, timedelta

# 1. Sayfa Ayarları
st.set_page_config(page_title="Sonsuz Aşkımıza ❤️", page_icon="💖", layout="centered")

# 2. CSS: Bilet Efekti, Arka Plan ve Kalpler
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Playfair+Display:ital,wght@1&display=swap');

    /* Arkaplan */
    [data-testid="stAppViewContainer"] {
        background: #fff5f7;
    }

    /* Uçuşan Kalpler */
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

    /* FOTOĞRAF ÇERÇEVELERİ */
    .photo-container {
        margin-top: 120px;
        margin-bottom: 120px;
        padding: 15px;
        background: white;
        border-radius: 10px;
        box-shadow: 0 15px 40px rgba(0,0,0,0.1);
        z-index: 1;
        position: relative;
    }

    .romantic-text {
        font-family: 'Dancing Script', cursive;
        font-size: 32px;
        color: #ad1457;
        text-align: center;
        margin: 50px 0;
    }

    .divider {
        text-align: center;
        margin: 100px 0;
        font-size: 45px;
        color: #ff4081;
        opacity: 0.6;
    }

    /* SAĞDAKİ BİLET (TICKET) TASARIMI */
    .ticket-container {
        position: fixed;
        right: -20px;
        top: 40%;
        transform: translateY(-50%);
        z-index: 9999;
    }
    
    .stButton>button {
        /* Bilet Görünümü */
        background: #ff4081;
        color: white;
        border: 2px dashed white;
        border-radius: 10px 0 0 10px;
        padding: 20px 10px;
        writing-mode: vertical-rl;
        text-orientation: mixed;
        font-family: 'Dancing Script', cursive;
        font-size: 20px;
        box-shadow: -5px 5px 15px rgba(0,0,0,0.2);
        transition: 0.3s;
    }
    .stButton>button:hover {
        right: 0px;
        background: #ad1457;
    }
    </style>
    """, unsafe_allow_html=True)

# Arkaplan Kalpleri
for i in range(35):
    left = i * 2.8
    delay = i * 0.4
    st.markdown(f'<div class="heart-bg" style="left:{left}%; animation-delay:{delay}s; animation-duration:{7+i%3}s;">❤️</div>', unsafe_allow_html=True)

# 3. Müzik Bileti Mantığı
if 'music_on' not in st.session_state:
    st.session_state.music_on = False

# Sağ taraftaki bilet butonu
with st.sidebar: # Bileti sidebar'da veya direkt ekranda tutabiliriz ama bilet efekti için özel alan:
    pass # CSS ile sağa sabitledik

# Ekranın sağında duran bilet butonu
st.markdown('<div class="ticket-container">', unsafe_allow_html=True)
if st.button("🎫 AŞK BİLETİNİ ÇEK"):
    st.session_state.music_on = True
st.markdown('</div>', unsafe_allow_html=True)

# Müzik Açıldıysa
if st.session_state.music_on:
    # Gizli YouTube Player (Taa Uzak Yollardan)
    st.markdown("""
        <iframe width="0" height="0" src="https://www.youtube.com/embed/S2C9X-98b-E?autoplay=1" 
        frameborder="0" allow="autoplay; encrypted-media"></iframe>
        """, unsafe_allow_html=True)
    st.toast("Müzik başladı... ❤️", icon="🎵")

# 4. Ana İçerik
st.markdown("<h1 style='text-align: center; font-family: Dancing Script; color: #ad1457; font-size: 55px;'>960 Günlük Masalımız</h1>", unsafe_allow_html=True)

# BÖLÜM 1
st.markdown('<div class="photo-container">', unsafe_allow_html=True)
try:
    st.image("foto1.jpg", use_column_width=True)
except:
    st.write("📷 Fotoğraf 1")
st.markdown('</div>', unsafe_allow_html=True)
st.markdown('<div class="romantic-text">"Taa uzak yollardan koştum geldim senin kollarına..."</div>', unsafe_allow_html=True)

st.markdown('<div class="divider">🌹 ❤️ 🌹</div>', unsafe_allow_html=True)

# BÖLÜM 2
st.markdown('<div class="photo-container">', unsafe_allow_html=True)
try:
    st.image("foto2.jpg", use_column_width=True)
except:
    st.write("📸 Fotoğraf 2")
st.markdown('</div>', unsafe_allow_html=True)
st.markdown('<div class="romantic-text">"960 gündür her nefesim seninle anlam buluyor."</div>', unsafe_allow_html=True)

st.markdown('<div class="divider">✨ 💖 ✨</div>', unsafe_allow_html=True)

# BÖLÜM 3 (VİDEO)
st.markdown("<h2 style='text-align: center; font-family: Dancing Script; color: #ad1457;'>Bizim En Özel Anımız</h2>", unsafe_allow_html=True)
st.markdown('<div class="photo-container">', unsafe_allow_html=True)
try:
    video_file = open('video.mp4', 'rb')
    st.video(video_file.read())
except:
    st.error("Kanka video.mp4 dosyasını GitHub'a yüklemeyi unutma!")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="divider">💍 ❤️ 💍</div>', unsafe_allow_html=True)

# BÖLÜM 4 (SON FOTO)
st.markdown('<div class="photo-container">', unsafe_allow_html=True)
try:
    st.image("foto3.jpg", use_column_width=True)
except:
    st.write("📸 Fotoğraf 3")
st.markdown('</div>', unsafe_allow_html=True)

# Final
st.balloons()
st.markdown("<h1 style='text-align: center; font-family: Dancing Script; color: #ad1457; font-size: 65px;'>Seni Çok Seviyorum!</h1>", unsafe_allow_html=True)
st.markdown("<div style='height: 300px;'></div>", unsafe_allow_html=True)
