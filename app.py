import streamlit as st
from datetime import datetime, timedelta

# 1. Sayfa Ayarları
st.set_page_config(page_title="Sonsuz Aşkımıza ❤️", page_icon="💖", layout="centered")

# 2. CSS: Arka Plan, Kalpler, Bilet ve Fotoğraf Araları
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

    /* FOTOĞRAF ÇERÇEVELERİ VE ARALIKLAR */
    .photo-wrapper {
        margin-top: 150px;
        margin-bottom: 150px;
        padding: 15px;
        background: white;
        border-radius: 15px;
        box-shadow: 0 15px 45px rgba(0,0,0,0.1);
        position: relative;
        z-index: 1;
    }

    .romantic-quote {
        font-family: 'Dancing Script', cursive;
        font-size: 34px;
        color: #ad1457;
        text-align: center;
        margin: 60px 0;
    }

    /* SAĞDAKİ YAN DURAN BİLET BUTONU */
    .ticket-trigger {
        position: fixed;
        right: -15px;
        top: 50%;
        transform: translateY(-50%);
        z-index: 9999;
    }
    
    .stButton>button {
        background: #ff4081;
        color: white;
        border: 2px dashed white;
        border-radius: 15px 0 0 15px;
        padding: 30px 15px;
        writing-mode: vertical-rl;
        text-orientation: mixed;
        font-family: 'Dancing Script', cursive;
        font-size: 20px;
        box-shadow: -5px 5px 20px rgba(0,0,0,0.3);
        cursor: pointer;
    }

    /* MÜZİK PANELİ */
    .music-box {
        background: white;
        border-radius: 20px;
        padding: 20px;
        border: 2px solid #ff4081;
        text-align: center;
        margin-bottom: 50px;
        box-shadow: 0 10px 25px rgba(255, 64, 129, 0.2);
    }
    </style>
    """, unsafe_allow_html=True)

# Hareketli Kalpleri Ekleme
for i in range(35):
    left = i * 2.8
    delay = i * 0.5
    st.markdown(f'<div class="heart-bg" style="left:{left}%; animation-delay:{delay}s; animation-duration:{7+i%3}s;">❤️</div>', unsafe_allow_html=True)

# 3. Müzik ve Bilet Mantığı
if 'music_ready' not in st.session_state:
    st.session_state.music_ready = False

# Sağdaki Bilet
st.markdown('<div class="ticket-trigger">', unsafe_allow_html=True)
if st.button("🎫 MÜZİK BİLETİ"):
    st.session_state.music_ready = True
st.markdown('</div>', unsafe_allow_html=True)

# Bilet Çekilince Açılan Müzik Paneli
if st.session_state.music_ready:
    st.markdown('<div class="music-box">', unsafe_allow_html=True)
    st.markdown("<h3 style='color: #ad1457; font-family: Dancing Script;'>🎵 Bizim Şarkımız Çalsın mı?</h3>", unsafe_allow_html=True)
    
    # Kanka buraya şarkının internet üzerindeki bir MP3 linkini koydum (Nilüfer - Taa Uzak Yollardan)
    # Eğer elinde mp3 dosyası varsa GitHub'a yukleyip 'sarki.mp3' yazarak da kullanabilirsin.
    audio_url = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3" # TEST İÇİN (Burayı değiştir)
    # Kendi MP3 dosyan varsa GitHub'a at ve alttaki satırı kullan:
    # st.audio("sarki.mp3") 
    
    # Gerçek YouTube müziğini en sağlam şekilde buraya koyuyoruz:
    st.video("https://www.youtube.com/watch?v=S2C9X-98b-E")
    st.write("Yukarıdaki videodan müziği başlatıp anılarımıza kaydırabilirsin... ❤️")
    st.markdown('</div>', unsafe_allow_html=True)

# 4. Ana İçerik
st.markdown("<h1 style='text-align: center; font-family: Dancing Script; color: #ad1457; font-size: 60px;'>960 Günlük Masalımız</h1>", unsafe_allow_html=True)

# --- FOTO 1 ---
st.markdown('<div class="photo-wrapper">', unsafe_allow_html=True)
try:
    st.image("foto1.jpg", use_column_width=True)
except:
    st.write("📸 Fotoğraf 1 Yükleniyor...")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="romantic-quote">"Taa uzak yollardan koştum geldim senin kollarına..."</div>', unsafe_allow_html=True)

# --- FOTO 2 ---
st.markdown('<div class="photo-wrapper">', unsafe_allow_html=True)
try:
    st.image("foto2.jpg", use_column_width=True)
except:
    st.write("📸 Fotoğraf 2 Yükleniyor...")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="romantic-quote">"960 gündür her sabah seninle olduğum için şükrediyorum."</div>', unsafe_allow_html=True)

# --- VİDEO BÖLÜMÜ ---
st.markdown("<h2 style='text-align: center; font-family: Dancing Script; color: #ad1457;'>Bizim Hikayemiz</h2>", unsafe_allow_html=True)
st.markdown('<div class="photo-wrapper">', unsafe_allow_html=True)
try:
    video_file = open('video.mp4', 'rb')
    st.video(video_file.read())
except:
    st.error("video.mp4 GitHub'da bulunamadı!")
st.markdown('</div>', unsafe_allow_html=True)

# --- FOTO 3 ---
st.markdown('<div class="photo-wrapper">', unsafe_allow_html=True)
try:
    st.image("foto3.jpg", use_column_width=True)
except:
    st.write("📸 Fotoğraf 3 Yükleniyor...")
st.markdown('</div>', unsafe_allow_html=True)

# FİNAL
st.balloons()
st.markdown("<h1 style='text-align: center; font-family: Dancing Script; color: #ad1457; font-size: 70px;'>Seni Çok Seviyorum!</h1>", unsafe_allow_html=True)
st.markdown("<div style='height: 300px;'></div>", unsafe_allow_html=True)
