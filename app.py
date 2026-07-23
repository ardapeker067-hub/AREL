import streamlit as st
from datetime import datetime, timedelta

# 1. Sayfa Ayarları
st.set_page_config(page_title="Sonsuz Aşkımıza ❤️", page_icon="💖", layout="centered")

# 2. CSS: Arkaplan, Kalpler ve Zarif Yazı Tipleri
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Playfair+Display:ital,wght@1,600&display=swap');

    /* Hareketli Arkaplan */
    [data-testid="stAppViewContainer"] {
        background: #fff5f7;
    }

    /* Uçuşan Kalp Efekti */
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

    /* Romantik Kart Tasarımı */
    .card {
        background: rgba(255, 255, 255, 0.8);
        backdrop-filter: blur(8px);
        padding: 40px;
        border-radius: 25px;
        border: 1px solid #ffc1e3;
        box-shadow: 0 10px 30px rgba(255, 182, 193, 0.3);
        margin: 100px 0;
        text-align: center;
        position: relative;
        z-index: 1;
    }

    .romantic-text {
        font-family: 'Dancing Script', cursive;
        font-size: 32px;
        color: #ad1457;
        margin-bottom: 20px;
    }

    .quote {
        font-family: 'Playfair Display', serif;
        font-size: 22px;
        color: #880e4f;
        font-style: italic;
        line-height: 1.8;
    }

    /* Dev Başlat Butonu */
    .stButton>button {
        width: 100%;
        height: 100px;
        background: linear-gradient(45deg, #ff4081, #ec407a);
        color: white;
        font-size: 30px !important;
        font-family: 'Dancing Script', cursive;
        border-radius: 50px;
        border: none;
        box-shadow: 0 10px 20px rgba(255, 64, 129, 0.4);
        cursor: pointer;
    }
    </style>
    """, unsafe_allow_html=True)

# Arkaplana 40 tane hareketli kalp ekle
hearts_html = ""
for i in range(40):
    left = i * 2.5
    delay = i * 0.5
    duration = 6 + (i % 4)
    hearts_html += f'<div class="heart-bg" style="left:{left}%; animation-delay:{delay}s; animation-duration:{duration}s;">❤️</div>'
st.markdown(hearts_html, unsafe_allow_html=True)

# 3. Müzik ve İçerik Kontrolü
if 'start' not in st.session_state:
    st.session_state.start = False

if not st.session_state.start:
    # GİRİŞ EKRANI (Müziği 'tetiklemek' için şart)
    st.markdown("<br><br><br><br>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align:center; font-family:Dancing Script; color:#ad1457; font-size:50px;'>Seni Bekleyen Bir Sürpriz Var...</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; font-size:18px;'>Lütfen aşağıdaki hediye kutusuna dokun.</p>", unsafe_allow_html=True)
    
    if st.button("🎁 Buraya Dokun ve Müziği Dinle"):
        st.session_state.start = True
        st.rerun()
else:
    # --- MÜZİK: Taa Uzak Yollardan ---
    # YouTube üzerinden otomatik başlatmalı gizli player
    st.markdown("""
        <iframe width="0" height="0" src="https://www.youtube.com/embed/S2C9X-98b-E?autoplay=1&loop=1&playlist=S2C9X-98b-E" 
        frameborder="0" allow="autoplay; encrypted-media"></iframe>
        """, unsafe_allow_html=True)

    # 4. Ana İçerik
    st.markdown("<h1 style='text-align:center; font-family:Dancing Script; color:#ad1457; font-size:60px;'>960 Günlük Masalımız</h1>", unsafe_allow_html=True)

    # BÖLÜM 1
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("<p class='romantic-text'>Her Şey Seninle Başladı...</p>", unsafe_allow_html=True)
    try:
        st.image("foto1.jpg", use_column_width=True)
    except:
        st.write("📸 (Fotoğraf 1)")
    st.markdown("<p class='quote'>'Taa uzak yollardan koştum geldim senin kollarına... Hayatımın en güzel kararı sendin.'</p>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # BÖLÜM 2
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("<p class='romantic-text'>960 Gündür Bitmeyen Huzur</p>", unsafe_allow_html=True)
    st.markdown("<p class='quote'>Seninle geçen her gün, bir öncekinden daha güzel. Sesin dünyadaki en huzurlu melodi.</p>", unsafe_allow_html=True)
    try:
        st.image("foto2.jpg", use_column_width=True)
    except:
        st.write("📸 (Fotoğraf 2)")
    st.markdown('</div>', unsafe_allow_html=True)

    # BÖLÜM 3 (VİDEO)
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("<p class='romantic-text'>Bizim En Özel Anımız</p>", unsafe_allow_html=True)
    try:
        video_file = open('video.mp4', 'rb')
        st.video(video_file.read())
    except:
        st.error("Kanka video.mp4 dosyasını GitHub'a yüklemeyi unutma!")
    st.markdown('</div>', unsafe_allow_html=True)

    # BÖLÜM 4
    st.markdown('<div class="card">', unsafe_allow_html=True)
    try:
        st.image("foto3.jpg", use_column_width=True)
    except:
        st.write("📸 (Fotoğraf 3)")
    st.markdown("<p class='romantic-text'>Sonsuza Kadar...</p>", unsafe_allow_html=True)
    st.markdown("<p class='quote'>Seni her gün, her saat, her saniye daha çok seveceğime söz veriyorum.</p>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # FİNAL
    st.balloons()
    st.markdown("<h1 style='text-align:center; font-family:Dancing Script; color:#ad1457; font-size:70px;'>Seni Çok Seviyorum!</h1>", unsafe_allow_html=True)
    st.markdown("<div style='height: 300px;'></div>", unsafe_allow_html=True)
