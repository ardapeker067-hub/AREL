import streamlit as st
from datetime import datetime

# 1. Sayfa Ayarları
st.set_page_config(page_title="Sonsuz Aşkımıza ❤️", page_icon="💖", layout="centered")

# 2. CSS: Buton Tasarımı, Arka Plan, Kalpler ve Efektler
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Playfair+Display:ital,wght@1&display=swap');

    /* Arkaplan */
    [data-testid="stAppViewContainer"] {
        background: #fff5f7;
    }
    
    /* Yan Panel Tasarımı */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #ffebee 0%, #fce4ec 100%);
        border-right: 3px solid #ffc1e3;
    }

    /* FOTOĞRAF KARTLARI */
    .photo-card {
        margin: 40px 0;
        padding: 20px;
        background: white;
        border-radius: 20px;
        box-shadow: 0 12px 40px rgba(0,0,0,0.1);
        text-align: center;
        border: 1px solid #fce4ec;
        transition: 0.5s;
    }
    .photo-card:hover {
        transform: scale(1.02);
    }

    /* ROMANTİK AYRAÇLAR (DİVİDER) */
    .love-divider {
        text-align: center;
        margin: 60px 0;
        font-size: 35px;
        color: #ff4081;
        opacity: 0.7;
    }

    /* ROMANTİK SÖZLER */
    .quote-box {
        font-family: 'Dancing Script', cursive;
        font-size: 28px;
        color: #ad1457;
        text-align: center;
        padding: 20px;
        line-height: 1.4;
    }

    /* KALPLER */
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

    /* YAN PANEL BUTONLARI İÇİN ÖZEL STİL */
    div.stButton > button {
        width: 100%;
        background-color: #ffffff;
        color: #ad1457;
        border: 2px solid #ffc1e3;
        border-radius: 15px;
        font-family: 'Dancing Script', cursive;
        font-size: 20px;
        margin-bottom: 10px;
        transition: 0.3s;
    }
    div.stButton > button:hover {
        background-color: #ff4081;
        color: white;
        border-color: #ff4081;
    }
    </style>
    """, unsafe_allow_html=True)

# Arkaplan Kalpleri
for i in range(25):
    left = i * 4
    st.markdown(f'<div class="heart-bg" style="left:{left}%; animation-delay:{i*0.5}s; animation-duration:{8+i%3}s;">❤️</div>', unsafe_allow_html=True)

# --- 3. SESSION STATE (Sayfa Takibi İçerik) ---
if 'sayfa' not in st.session_state:
    st.session_state.sayfa = "Ana Sayfa"

# --- 4. YAN PANEL (SOL) - BUTONLAR ---
with st.sidebar:
    st.markdown("<h1 style='font-family: Dancing Script; color: #ad1457; text-align: center;'>🗓️ Anı Takvimi</h1>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    if st.button("🏠 Ana Sayfa"):
        st.session_state.sayfa = "Ana Sayfa"
    if st.button("📅 2023 Yılı"):
        st.session_state.sayfa = "2023"
    if st.button("📅 2024 Yılı"):
        st.session_state.sayfa = "2024"
    if st.button("📅 2025 Yılı"):
        st.session_state.sayfa = "2025"
    
    st.markdown("<br><hr>", unsafe_allow_html=True)
    st.write("Her buton, kalbimden bir yıla açılan kapıdır... ❤️")

# --- 5. MÜZİK BİLETİ (Sağ Üst) ---
if 'music' not in st.session_state: st.session_state.music = False
st.markdown('<div style="position: fixed; right: 15px; top: 20px; z-index: 9999;">', unsafe_allow_html=True)
if st.button("🎫 Müzik"):
    st.session_state.music = not st.session_state.music
st.markdown('</div>', unsafe_allow_html=True)

if st.session_state.music:
    try:
        audio_file = open('sarki.mp3', 'rb')
        st.audio(audio_file.read(), format='audio/mp3')
    except: st.sidebar.error("sarki.mp3 yüklenmemiş!")

# --- 6. İÇERİK GÖSTERİMİ VE ROMANTİK DETAYLAR ---

def romantic_divider(icon="🌹"):
    st.markdown(f'<div class="love-divider">✨ {icon} ✨</div>', unsafe_allow_html=True)

def romantic_quote(text):
    st.markdown(f'<div class="quote-box">"{text}"</div>', unsafe_allow_html=True)

if st.session_state.sayfa == "Ana Sayfa":
    st.markdown("<h1 style='text-align: center; font-family: Dancing Script; color: #ad1457; font-size: 55px;'>960 Günlük Masalımız</h1>", unsafe_allow_html=True)
    st.markdown('<div class="photo-card">', unsafe_allow_html=True)
    try: st.image("foto1.jpg", use_column_width=True)
    except: st.write("foto1.jpg bekleniyor...")
    st.markdown('</div>', unsafe_allow_html=True)
    romantic_quote("Taa uzak yollardan koştum geldim senin kollarına... İyi ki varsın sevgilim.")

elif st.session_state.sayfa == "2023":
    st.markdown("<h1 style='text-align: center; font-family: Dancing Script; color: #ad1457;'>✨ 2023: Başlangıcımız</h1>", unsafe_allow_html=True)
    
    # Fotoğraf 1
    st.markdown('<div class="photo-card">', unsafe_allow_html=True)
    try: st.image("2023_1.jpg", use_column_width=True)
    except: st.write("Fotoğraf bekleniyor...")
    st.markdown('</div>', unsafe_allow_html=True)
    
    romantic_divider("❤️")
    romantic_quote("Seninle geçen her saniye, ömrüme ömür katıyor.")
    
    # Fotoğraf 2
    st.markdown('<div class="photo-card">', unsafe_allow_html=True)
    try: st.image("2023_2.jpg", use_column_width=True)
    except: st.write("Fotoğraf bekleniyor...")
    st.markdown('</div>', unsafe_allow_html=True)
    
    romantic_divider("🌹")
    st.balloons()

elif st.session_state.sayfa == "2024":
    st.markdown("<h1 style='text-align: center; font-family: Dancing Script; color: #ad1457;'>🌟 2024: Büyüyen Aşkımız</h1>", unsafe_allow_html=True)
    
    # Fotoğrafları bu şekilde alt alta ekleyebilirsin kanka
    try:
        st.markdown('<div class="photo-card">', unsafe_allow_html=True)
        st.image("2024_1.jpg", use_column_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        romantic_divider("💖")
        romantic_quote("Gülüşünde saklı olan o huzuru başka hiçbir yerde bulamadım.")
        
        st.markdown('<div class="photo-card">', unsafe_allow_html=True)
        st.image("2024_2.jpg", use_column_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    except: st.info("Fotoğraflar yükleniyor...")
    st.balloons()

elif st.session_state.sayfa == "2025":
    st.markdown("<h1 style='text-align: center; font-family: Dancing Script; color: #ad1457;'>🚀 2025: Geleceğimiz</h1>", unsafe_allow_html=True)
    romantic_quote("Seninle daha nice yıllara, nice 960 günlere... Seni çok seviyorum.")
    try:
        st.markdown('<div class="photo-card">', unsafe_allow_html=True)
        st.image("2025_1.jpg", use_column_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    except: st.write("Hazırlanıyor...")
    st.balloons()

# Sayfa Altı Boşluğu
st.markdown("<div style='height: 150px;'></div>", unsafe_allow_html=True)
