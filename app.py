import streamlit as st
import random

# 1. Sayfa Ayarları
st.set_page_config(page_title="Sonsuz Aşkımıza ❤️", page_icon="💖", layout="centered")

# 2. CSS: Fotoğraf Boyutu Kontrolü ve Tasarım
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Playfair+Display:ital,wght@1&display=swap');

    [data-testid="stAppViewContainer"] {
        background: #fff5f7;
    }
    
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #ffebee 0%, #fce4ec 100%);
        border-right: 3px solid #ffc1e3;
    }

    /* FOTOĞRAF KARTLARI - Boyutu buradan kontrol ediyoruz */
    .photo-card {
        max-width: 450px; /* Fotoğrafların maksimum genişliği */
        margin: 30px auto; /* Ortalamak için */
        padding: 15px;
        background: white;
        border-radius: 15px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.1);
        text-align: center;
        border: 5px solid white; /* Polaroid havası */
    }

    .romantic-text {
        font-family: 'Dancing Script', cursive;
        font-size: 26px;
        color: #ad1457;
        text-align: center;
        padding: 15px;
    }

    /* Kalp Efekti */
    .heart-bg {
        position: fixed;
        top: -10%;
        color: #ff4081;
        font-size: 20px;
        z-index: 0;
        animation: fall linear infinite;
    }
    @keyframes fall {
        to { transform: translateY(110vh) rotate(360deg); }
    }

    /* Sidebar Butonları */
    div.stButton > button {
        width: 100%;
        background-color: white;
        color: #ad1457;
        border: 2px solid #ffc1e3;
        border-radius: 12px;
        font-family: 'Dancing Script', cursive;
        font-size: 18px;
        margin-bottom: 8px;
    }
    div.stButton > button:hover {
        background-color: #ff4081; color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. FOTOĞRAF LİSTELERİ (BURAYA TÜM FOTOĞRAFLARI EKLE) ---
# Kanka buradaki tırnakların içine GitHub'daki TÜM fotoğraflarının adını ekle.
# Ne kadar eklersen kod o kadar fotoğrafı otomatik dizecek.
dosyalar_2023 = ["2023_1.jpg", "2023_2.jpg", "2023_3.jpg", "2023_4.jpg"] 
dosyalar_2024 = ["2024_1.jpg", "2024_2.jpg", "2024_3.jpg", "2024_4.jpg", "2024_5.jpg"]
dosyalar_2025 = ["2025_1.jpg", "2025_2.jpg"]

# Rastgele Romantik Sözler (Fotoğraflar arasına serpiştirmek için)
sozler = [
    "Seninle her an bir başka güzel...",
    "Gülüşün kalbimdeki en güzel manzara.",
    "İyi ki hayatımdasın sevgilim.",
    "960 gün değil, bir ömür yetmez sana.",
    "Ellerini hiç bırakmayacağım.",
    "Taa uzak yollardan koştum geldim..."
]

# --- 4. YAN PANEL VE SAYFA TAKİBİ ---
if 'page' not in st.session_state:
    st.session_state.page = "Ana Sayfa"

with st.sidebar:
    st.markdown("<h1 style='text-align:center; font-family:Dancing Script; color:#ad1457;'>🗓️ Anı Takvimi</h1>", unsafe_allow_html=True)
    if st.button("🏠 Ana Sayfa"): st.session_state.page = "Ana Sayfa"
    if st.button("📅 2023"): st.session_state.page = "2023"
    if st.button("📅 2024"): st.session_state.page = "2024"
    if st.button("📅 2025"): st.session_state.page = "2025"

# Müzik Bileti
if 'm' not in st.session_state: st.session_state.m = False
st.sidebar.markdown("---")
if st.sidebar.button("🎫 Müzik Aç/Kapat"):
    st.session_state.m = not st.session_state.m

if st.session_state.m:
    try:
        st.sidebar.audio("sarki.mp3")
    except: st.sidebar.error("Müzik dosyası bulunamadı.")

# --- 5. İÇERİK DÖNGÜSÜ (OTOMATİK DİZİCİ) ---

def album_olustur(yıl, liste):
    st.markdown(f"<h1 style='text-align:center; font-family:Dancing Script; color:#ad1457;'>✨ {yıl} Hatıralarımız</h1>", unsafe_allow_html=True)
    
    for i, foto in enumerate(liste):
        # Her fotoğrafı bir kart içine alıyoruz
        st.markdown('<div class="photo-card">', unsafe_allow_html=True)
        try:
            st.image(foto, use_column_width=True)
        except:
            st.write(f"⚠️ {foto} yüklenemedi.")
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Her fotoğraftan sonra romantik bir süs ve söz ekle
        if i < len(liste) - 1: # Son fotoğraftan sonra söz koyma
            st.markdown(f"<div class='romantic-text'>✨ {random.choice(sozler)} ✨</div>", unsafe_allow_html=True)
            st.markdown("<div style='text-align:center; opacity:0.5;'>🌸 ❤️ 🌸</div>", unsafe_allow_html=True)

# Sayfa gösterimi
if st.session_state.page == "Ana Sayfa":
    st.markdown("<h1 style='text-align:center; font-family:Dancing Script; color:#ad1457; font-size:50px;'>960 Günlük Hikayemiz</h1>", unsafe_allow_html=True)
    st.markdown('<div class="photo-card">', unsafe_allow_html=True)
    st.image("foto1.jpg", use_column_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; font-family:Dancing Script; font-size:24px;'>Sol taraftaki menüden yıllara göre tüm anılarımızı izleyebilirsin sevgilim... ❤️</p>", unsafe_allow_html=True)

elif st.session_state.page == "2023":
    album_olustur("2023", dosyalar_2023)
    st.balloons()

elif st.session_state.page == "2024":
    album_olustur("2024", dosyalar_2024)
    st.balloons()

elif st.session_state.page == "2025":
    album_olustur("2025", dosyalar_2025)
    st.balloons()

# Arkaplan Kalpleri (20 adet)
for i in range(20):
    st.markdown(f'<div class="heart-bg" style="left:{i*5}%; animation-delay:{i*0.4}s; animation-duration:{6+i%3}s;">❤️</div>', unsafe_allow_html=True)
