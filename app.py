import streamlit as st
from datetime import datetime, timedelta

# 1. Sayfa Ayarları
st.set_page_config(page_title="Sadece Bizim İçin ❤️", page_icon="💖", layout="centered")

# 2. CSS: Full Hareketli Arkaplan ve Romantik Efektler
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Playfair+Display:ital,wght@1,600&display=swap');

    /* Hareketli Kalp Arkaplanı */
    [data-testid="stAppViewContainer"] {
        background: #ffebee;
        background-image: 
            radial-gradient(circle at 20% 30%, rgba(255, 182, 193, 0.4) 0%, transparent 20%),
            radial-gradient(circle at 80% 70%, rgba(255, 105, 180, 0.3) 0%, transparent 20%);
        overflow-x: hidden;
    }

    /* Kalp Yağmuru Animasyonu */
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

    /* Kart ve Yazı Tasarımları */
    .main-title {
        font-family: 'Dancing Script', cursive;
        font-size: 60px;
        color: #ad1457;
        text-align: center;
        margin-top: 50px;
    }

    .romantic-card {
        background: rgba(255, 255, 255, 0.6);
        backdrop-filter: blur(10px);
        padding: 30px;
        border-radius: 20px;
        border: 2px solid rgba(255, 192, 203, 0.5);
        box-shadow: 0 10px 30px rgba(0,0,0,0.05);
        margin: 80px 0;
        text-align: center;
        z-index: 1;
        position: relative;
    }

    .quote-text {
        font-family: 'Playfair Display', serif;
        font-size: 24px;
        color: #880e4f;
        font-style: italic;
        line-height: 1.6;
    }

    .divider {
        height: 2px;
        background: linear-gradient(to right, transparent, #ff4081, transparent);
        margin: 40px 0;
    }

    /* Başlat Butonu */
    .stButton>button {
        width: 100%;
        background: #ff4081;
        color: white;
        border-radius: 50px;
        height: 4em;
        font-size: 22px;
        font-weight: bold;
        border: none;
        box-shadow: 0 5px 20px rgba(255, 64, 129, 0.4);
    }
    </style>
    """, unsafe_allow_html=True)

# Arkaplana hareket eden 30 tane kalp ekleyelim
hearts = ""
for i in range(30):
    left = i * 3.3
    delay = i * 0.7
    duration = 5 + (i % 5)
    size = 15 + (i % 20)
    hearts += f'<div class="heart-bg" style="left:{left}%; animation-delay:{delay}s; animation-duration:{duration}s; font-size:{size}px;">❤️</div>'
st.markdown(hearts, unsafe_allow_html=True)

# 3. Müzik ve Başlatma Mantığı
if 'started' not in st.session_state:
    st.session_state.started = False

if not st.session_state.started:
    st.markdown("<br><br><br><br>", unsafe_allow_html=True)
    st.markdown("<h1 class='main-title'>Senin İçin Küçük Bir Masal...</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;'>Hazırsan kalbine dokunmaya geliyorum.</p>", unsafe_allow_html=True)
    if st.button("🎁 Sürprizi Başlat"):
        st.session_state.started = True
        st.rerun()
else:
    # Müzik: Taa Uzak Yollardan (Otomatik çalması için YouTube Embed)
    st.markdown("""
        <iframe width="0" height="0" src="https://www.youtube.com/embed/S2C9X-98b-E?autoplay=1" 
        frameborder="0" allow="autoplay; encrypted-media"></iframe>
        """, unsafe_allow_html=True)

    # 4. Giriş Ekranı
    st.markdown("<h1 class='main-title'>960 Gün, Tek Bir Aşk...</h1>", unsafe_allow_html=True)
    
    # --- BÖLÜM 1: Giriş Sözü ---
    st.markdown("""
    <div class='romantic-card'>
        <p class='quote-text'>"Taa uzak yollardan koştum geldim senin kollarına... <br> 
        Hayatımın en güzel 960 gününü seninle devirdim sevgilim."</p>
    </div>
    """, unsafe_allow_html=True)

    # --- BÖLÜM 2: FOTOĞRAF 1 ---
    st.markdown('<div class="romantic-card">', unsafe_allow_html=True)
    try:
        st.image("foto1.jpg", use_column_width=True)
    except:
        st.write("📷 Fotoğraf Yükleniyor...")
    st.markdown("<p class='quote-text'>Seninle her şey daha renkli, her şey daha anlamlı.</p>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # --- BÖLÜM 3: Romantik Bir Söz ---
    st.markdown("<h2 style='text-align:center; font-family:Dancing Script; color:#ad1457;'>Zaman seninle duruyor...</h2>", unsafe_allow_html=True)

    # --- BÖLÜM 4: FOTOĞRAF 2 ---
    st.markdown('<div class="romantic-card">', unsafe_allow_html=True)
    try:
        st.image("foto2.jpg", use_column_width=True)
    except:
        st.write("📷 Fotoğraf Yükleniyor...")
    st.markdown("<p class='quote-text'>Gözlerindeki o huzuru hiçbir şeye değişmem.</p>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # --- BÖLÜM 5: VİDEO (EN ÖZEL AN) ---
    st.markdown("<h2 style='text-align:center; font-family:Dancing Script; color:#ad1457;'>Bizim Hikayemiz</h2>", unsafe_allow_html=True)
    st.markdown('<div class="romantic-card">', unsafe_allow_html=True)
    try:
        video_file = open('video.mp4', 'rb')
        st.video(video_file.read())
        st.write("Her karesinde aşkımız saklı...")
    except:
        st.error("video.mp4 bulunamadı, ama kalbimde her anın kayıtlı! ❤️")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- BÖLÜM 6: FOTOĞRAF 3 ---
    st.markdown('<div class="romantic-card">', unsafe_allow_html=True)
    try:
        st.image("foto3.jpg", use_column_width=True)
    except:
        st.write("📷 Fotoğraf Yükleniyor...")
    st.markdown("<p class='quote-text'>Sonsuza kadar sadece sen ve ben...</p>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # --- FİNAL ---
    st.balloons()
    st.markdown("<h1 class='main-title'>Seni Çok Seviyorum!</h1>", unsafe_allow_html=True)
    st.markdown("<div style='height: 200px;'></div>", unsafe_allow_html=True) # Sayfayı uzatmak için boşluk
