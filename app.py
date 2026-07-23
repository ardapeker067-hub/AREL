import streamlit as st
from datetime import datetime, timedelta
import base64

# 1. Sayfa Ayarları
st.set_page_config(page_title="Sadece Bizim İçin", page_icon="❤️", layout="centered")

# 2. Gelişmiş CSS: Uçuşan Kalpler ve Romantik Tasarım
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&display=swap');

    /* Arkaplan ve Kalp Animasyonu */
    [data-testid="stAppViewContainer"] {
        background: #fce4ec;
        overflow: hidden;
    }

    .heart {
        position: absolute;
        top: -10%;
        user-select: none;
        display: inline-block;
        animation: heartFloat 10s linear infinite;
        font-size: 24px;
        color: #ff4081;
        opacity: 0.6;
        z-index: 0;
    }

    @keyframes heartFloat {
        0% { transform: translateY(110vh) rotate(0deg); opacity: 1; }
        100% { transform: translateY(-10vh) rotate(360deg); opacity: 0; }
    }

    /* Kart Tasarımları */
    .photo-frame {
        background: white;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 15px 35px rgba(0,0,0,0.1);
        margin: 60px 0;
        z-index: 1;
        position: relative;
    }

    .romantic-text {
        font-family: 'Dancing Script', cursive;
        font-size: 28px;
        color: #ad1457;
        text-align: center;
        margin: 40px 0;
        z-index: 1;
        position: relative;
    }

    .stButton>button {
        width: 100%;
        background: #ff4081;
        color: white;
        border-radius: 30px;
        height: 3.5em;
        font-size: 20px;
        font-weight: bold;
        border: none;
        box-shadow: 0 4px 15px rgba(255, 64, 129, 0.4);
    }
    </style>
    """, unsafe_allow_html=True)

# Arkaplana 15 tane uçuşan kalp ekleyelim
hearts_html = "".join([f'<div class="heart" style="left: {i*7}%; animation-delay: {i*0.5}s;">❤️</div>' for i in range(15)])
st.markdown(hearts_html, unsafe_allow_html=True)

# 3. Giriş Kontrolü (Müzik ve Başlatma)
if 'baslatildi' not in st.session_state:
    st.session_state.baslatildi = False

if not st.session_state.baslatildi:
    st.markdown("<br><br><br><h1 style='text-align: center; color: #ad1457; font-family: Dancing Script;'>Sana Bir Sürprizim Var Sevgilim...</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Devam etmek için aşağıdaki kutuya dokun.</p>", unsafe_allow_html=True)
    if st.button("🎁 Hediyeni Aç"):
        st.session_state.baslatildi = True
        st.rerun()
else:
    # --- MÜZİK BÖLÜMÜ ---
    # YouTube üzerinden "Taa Uzak Yollardan" (Otomatik çalması için hileli embed)
    st.markdown("""
        <iframe width="0" height="0" src="https://www.youtube.com/embed/S2C9X-98b-E?autoplay=1" 
        frameborder="0" allow="autoplay"></iframe>
        """, unsafe_allow_html=True)

    # 4. Sayaç Bölümü
    st.markdown("<div style='text-align: center; margin-top: 20px;'>", unsafe_allow_html=True)
    st.markdown(f"<h1 style='font-family: Dancing Script; color: #ad1457; font-size: 50px;'>Tam 960 Gündür...</h1>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # 5. Fotoğraflar ve Aralıklı Romantik Sözler
    
    # 1. Fotoğraf
    st.markdown('<div class="photo-frame">', unsafe_allow_html=True)
    st.image("foto1.jpg", use_column_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('<div class="romantic-text">"Taa uzak yollardan koştum geldim senin kollarına... Hayatımın en güzel kararı seninle bu yolu yürümekti."</div>', unsafe_allow_html=True)

    # 2. Fotoğraf
    st.markdown('<div class="photo-frame">', unsafe_allow_html=True)
    st.image("foto2.jpg", use_column_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('<div class="romantic-text">"960 günün her bir saniyesinde seni daha çok sevdim. Seninle her an bir başka güzel."</div>', unsafe_allow_html=True)

    # --- VİDEO BÖLÜMÜ ---
    st.markdown("<h2 style='text-align: center; color: #ad1457; font-family: Dancing Script;'>Bizim En Özel Anımız</h2>", unsafe_allow_html=True)
    st.markdown('<div class="photo-frame">', unsafe_allow_html=True)
    try:
        # Videoyu GitHub'dan okuma
        video_file = open('video.mp4', 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes)
        st.write("Seninle geçen her an, en sevdiğim film karesi...")
    except FileNotFoundError:
        st.error("Kanka 'video.mp4' dosyasını GitHub'a yüklemeyi unutma! İsim birebir aynı olmalı.")
    st.markdown('</div>', unsafe_allow_html=True)

    # 3. Fotoğraf (Kapanıştan önce)
    st.markdown('<div class="photo-frame">', unsafe_allow_html=True)
    st.image("foto3.jpg", use_column_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('<div class="romantic-text">"Sonsuza kadar sadece biz... Seni çok seviyorum sevgilim."</div>', unsafe_allow_html=True)

    st.balloons()
