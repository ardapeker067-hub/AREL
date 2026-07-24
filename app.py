import streamlit as st
from datetime import datetime, timedelta

# 1. Sayfa Ayarları
st.set_page_config(page_title="Sonsuz Aşkımıza ❤️", page_icon="💖", layout="centered")

# 2. CSS: Arka Plan, Kalpler ve Yatay Bilet
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Playfair+Display:ital,wght@1&display=swap');

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

    /* Fotoğraf Kartları (150px boşluk) */
    .photo-card {
        margin-top: 150px;
        margin-bottom: 150px;
        padding: 20px;
        background: white;
        border-radius: 20px;
        box-shadow: 0 15px 50px rgba(0,0,0,0.1);
        text-align: center;
        z-index: 1;
        position: relative;
    }

    .romantic-text {
        font-family: 'Dancing Script', cursive;
        font-size: 35px;
        color: #ad1457;
        margin: 50px 0;
    }

    /* SAĞDA YATAY DURAN BİLET BUTONU */
    .ticket-fixed {
        position: fixed;
        right: 10px;
        top: 50%;
        z-index: 9999;
    }
    
    .stButton>button {
        background: #ff4081;
        color: white;
        border: 2px dashed white;
        border-radius: 10px;
        padding: 10px 20px;
        font-family: 'Dancing Script', cursive;
        font-size: 18px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    }
    </style>
    """, unsafe_allow_html=True)

# Kalp Yağmuru
for i in range(30):
    left = i * 3.3
    st.markdown(f'<div class="heart-bg" style="left:{left}%; animation-delay:{i*0.5}s; animation-duration:{6+i%4}s;">❤️</div>', unsafe_allow_html=True)

# 3. Müzik Bileti Mantığı
if 'music_open' not in st.session_state:
    st.session_state.music_open = False

# Sağ tarafta yatay bilet
st.markdown('<div class="ticket-fixed">', unsafe_allow_html=True)
if st.button("🎫 Müzik Bileti"):
    st.session_state.music_open = not st.session_state.music_open
st.markdown('</div>', unsafe_allow_html=True)

if st.session_state.music_open:
    st.markdown("🎵 **Nilüfer - Taa Uzak Yollardan** çalıyor...")
    # Yeni ve daha kararlı bir link deniyoruz (YouTube embed hatasını önlemek için)
    # Eğer bu da "Video unavailable" derse, YouTube o videonun dış sitelerde oynatılmasını yasaklamıştır.
    st.video("https://www.youtube.com/watch?v=R_pY_1D_wWw") 

# 4. Ana İçerik
st.markdown("<h1 style='text-align: center; font-family: Dancing Script; color: #ad1457; font-size: 60px;'>960 Günlük Hikayemiz</h1>", unsafe_allow_html=True)

# --- FOTO 1 ---
st.markdown('<div class="photo-card">', unsafe_allow_html=True)
try:
    st.image("foto1.jpg", use_column_width=True)
except:
    st.write("📸 foto1.jpg yüklenemedi")
st.markdown('</div>', unsafe_allow_html=True)
st.markdown('<div class="romantic-text">"Taa uzak yollardan koştum geldim..."</div>', unsafe_allow_html=True)

# --- FOTO 2 ---
st.markdown('<div class="photo-card">', unsafe_allow_html=True)
try:
    st.image("foto2.jpg", use_column_width=True)
except:
    st.write("📸 foto2.jpg yüklenemedi")
st.markdown('</div>', unsafe_allow_html=True)
st.markdown('<div class="romantic-text">"Her anımızda sen varsın."</div>', unsafe_allow_html=True)

# --- KENDİ VİDEONUZ (Önemli Bölüm) ---
st.markdown("<h2 style='text-align: center; font-family: Dancing Script; color: #ad1457;'>Bizim Hikayemiz</h2>", unsafe_allow_html=True)
st.markdown('<div class="photo-card">', unsafe_allow_html=True)
try:
    # GitHub'a yüklediğin video.mp4 burayı çalıştırır
    video_file = open('video.mp4', 'rb')
    st.video(video_file.read())
except:
    st.error("Kendi videon (video.mp4) henüz yüklenmemiş kanka.")
st.markdown('</div>', unsafe_allow_html=True)

# --- FOTO 3 ---
st.markdown('<div class="photo-card">', unsafe_allow_html=True)
try:
    st.image("foto3.jpg", use_column_width=True)
except:
    st.write("📸 foto3.jpg yüklenemedi")
st.markdown('</div>', unsafe_allow_html=True)

# Final
st.balloons()
st.markdown("<h1 style='text-align: center; font-family: Dancing Script; color: #ad1457; font-size: 70px;'>Seni Çok Seviyorum!</h1>", unsafe_allow_html=True)
st.markdown("<div style='height: 300px;'></div>", unsafe_allow_html=True)
