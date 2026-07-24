import streamlit as st
from datetime import datetime, timedelta

# 1. Sayfa Ayarları
st.set_page_config(page_title="Sonsuz Aşkımıza ❤️", page_icon="💖", layout="centered")

# 2. CSS: Araları açma ve Romantik Süslemeler
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Playfair+Display:ital,wght@1@display=swap');

    /* Arkaplan */
    [data-testid="stAppViewContainer"] {
        background: #fff5f7;
    }

    /* Kalp Yağmuru */
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

    /* Fotoğraflar Arası Boşluk ve Çerçeve */
    .photo-container {
        margin-top: 100px;
        margin-bottom: 100px;
        padding: 20px;
        background: white;
        border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        z-index: 1;
        position: relative;
    }

    /* Romantik Ara Ayraç (Süsleme) */
    .divider {
        text-align: center;
        margin: 80px 0;
        font-size: 40px;
        color: #ff4081;
        position: relative;
    }
    .divider::before, .divider::after {
        content: "————————";
        font-size: 15px;
        vertical-align: middle;
        opacity: 0.3;
        margin: 0 20px;
    }

    .romantic-text {
        font-family: 'Dancing Script', cursive;
        font-size: 35px;
        color: #ad1457;
        text-align: center;
        margin: 40px 0;
    }

    /* Müzik Butonu */
    .stButton>button {
        width: 100%;
        background: #ff4081;
        color: white;
        border-radius: 50px;
        height: 4em;
        font-size: 24px;
        font-weight: bold;
        border: none;
        box-shadow: 0 5px 20px rgba(255, 64, 129, 0.4);
    }
    </style>
    """, unsafe_allow_html=True)

# Arkaplan Kalpleri
for i in range(30):
    left = i * 3.3
    delay = i * 0.5
    st.markdown(f'<div class="heart-bg" style="left:{left}%; animation-delay:{delay}s; animation-duration:{6+i%4}s;">❤️</div>', unsafe_allow_html=True)

# 3. Müzik ve Başlatma
if 'playing' not in st.session_state:
    st.session_state.playing = False

if not st.session_state.playing:
    st.markdown("<br><br><br><h1 style='text-align: center; font-family: Dancing Script; color: #ad1457;'>Sana Bir Sürprizim Var...</h1>", unsafe_allow_html=True)
    st.write("<p style='text-align: center;'>Lütfen hediye kutusuna dokun.</p>", unsafe_allow_html=True)
    if st.button("🎁 Sürprizi Ve Müziği Başlat"):
        st.session_state.playing = True
        st.rerun()
else:
    # MÜZİK: Nilüfer - Taa Uzak Yollardan (Bu yöntem en sağlamıdır)
    # YouTube ID: S2C9X-98b-E
    st.markdown("""
        <iframe width="0" height="0" src="https://www.youtube.com/embed/S2C9X-98b-E?autoplay=1" 
        frameborder="0" allow="autoplay; encrypted-media"></iframe>
        """, unsafe_allow_html=True)

    # 4. Ana İçerik
    st.markdown("<h1 style='text-align: center; font-family: Dancing Script; color: #ad1457; font-size: 60px;'>960 Günlük Masalımız</h1>", unsafe_allow_html=True)

    # BÖLÜM 1
    st.markdown('<div class="photo-container">', unsafe_allow_html=True)
    try:
        st.image("foto1.jpg", use_column_width=True)
    except:
        st.write("📷 Fotoğraf 1")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="romantic-text">"Taa uzak yollardan koştum geldim senin kollarına... Hayatımın en güzel kararı sendin."</div>', unsafe_allow_html=True)

    # --- SÜSLEME (FOTOĞRAFLAR ARASI DETAY) ---
    st.markdown('<div class="divider">🌹 ❤️ 🌹</div>', unsafe_allow_html=True)
    
    st.markdown('<div style="text-align:center; color:#ad1457; font-style:italic;">Seninle geçen her saniye bir ömre bedel...</div>', unsafe_allow_html=True)

    # BÖLÜM 2
    st.markdown('<div class="photo-container">', unsafe_allow_html=True)
    try:
        st.image("foto2.jpg", use_column_width=True)
    except:
        st.write("📸 Fotoğraf 2")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="romantic-text">"960 gündür kalbimde çalan en güzel melodi senin sesin."</div>', unsafe_allow_html=True)

    # --- SÜSLEME 2 ---
    st.markdown('<div class="divider">✨ 💖 ✨</div>', unsafe_allow_html=True)

    # BÖLÜM 3 (VİDEO)
    st.markdown("<h2 style='text-align: center; font-family: Dancing Script; color: #ad1457;'>Bizim En Özel Anımız</h2>", unsafe_allow_html=True)
    st.markdown('<div class="photo-container">', unsafe_allow_html=True)
    try:
        video_file = open('video.mp4', 'rb')
        st.video(video_file.read())
    except:
        st.error("video.mp4 bulunamadı, GitHub'a yüklemeyi unutma kanka!")
    st.markdown('</div>', unsafe_allow_html=True)

    # BÖLÜM 4 (SON FOTO)
    st.markdown('<div class="divider">💍 ❤️ 💍</div>', unsafe_allow_html=True)
    st.markdown('<div class="photo-container">', unsafe_allow_html=True)
    try:
        st.image("foto3.jpg", use_column_width=True)
    except:
        st.write("📸 Fotoğraf 3")
    st.markdown('</div>', unsafe_allow_html=True)

    st.balloons()
    st.markdown("<h1 style='text-align: center; font-family: Dancing Script; color: #ad1457; font-size: 70px;'>Seni Çok Seviyorum!</h1>", unsafe_allow_html=True)
    st.markdown("<div style='height: 300px;'></div>", unsafe_allow_html=True)
