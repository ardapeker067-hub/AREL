import streamlit as st
from datetime import datetime

# 1. Sayfa Ayarları
st.set_page_config(page_title="Sonsuz Aşkımıza ❤️", page_icon="💖", layout="centered")

# 2. CSS: Yan Panel ve Fotoğraf Kartları
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Playfair+Display:ital,wght@1&display=swap');

    /* Arkaplan */
    [data-testid="stAppViewContainer"] {
        background: #fff5f7;
    }
    
    /* Yan Panel (Sidebar) Tasarımı */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #ffebee 0%, #fce4ec 100%);
        border-right: 3px solid #ffc1e3;
    }
    
    /* Yan Paneldeki Yazılar */
    .st-emotion-cache-17fal0n { 
        font-family: 'Dancing Script', cursive;
        color: #ad1457;
        font-size: 20px;
    }

    /* Fotoğraf Kartları (Geniş aralıklar ve şık çerçeve) */
    .photo-card {
        margin-top: 60px;
        margin-bottom: 60px;
        padding: 20px;
        background: white;
        border-radius: 20px;
        box-shadow: 0 12px 40px rgba(0,0,0,0.12);
        text-align: center;
        border: 1px solid #fce4ec;
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

    /* Müzik Bileti */
    .ticket-fixed {
        position: fixed;
        right: 15px;
        top: 20px;
        z-index: 9999;
    }
    </style>
    """, unsafe_allow_html=True)

# Arkaplan Kalpleri
for i in range(25):
    left = i * 4
    st.markdown(f'<div class="heart-bg" style="left:{left}%; animation-delay:{i*0.5}s; animation-duration:{8+i%3}s;">❤️</div>', unsafe_allow_html=True)

# --- 3. FOTOĞRAF LİSTELERİ (Buraya tüm fotoğraflarını ekle) ---
# Kanka buradaki tırnakların içine GitHub'a yüklediğin tüm fotoğrafların adını yaz.
fotos_2023 = ["2023_1.jpg", "2023_2.jpg", "2023_3.jpg", "2023_4.jpg"] # Burayı istediğin kadar uzat
fotos_2024 = ["2024_1.jpg", "2024_2.jpg", "2024_3.jpg", "2024_4.jpg"]
fotos_2025 = ["2025_1.jpg", "2025_2.jpg"]

# --- 4. YAN PANEL (SOL) ---
with st.sidebar:
    st.markdown("<h1 style='font-family: Dancing Script; color: #ad1457;'>🗓️ Anı Takvimi</h1>", unsafe_allow_html=True)
    st.markdown("---")
    secim = st.radio(
        "Gezinmek istediğin yılı seç sevgilim:",
        ["🏠 Ana Sayfa", "📅 2023", "📅 2024", "📅 2025"],
        index=0
    )
    st.markdown("---")
    st.write("Her yılın içinde bize ait bambaşka hikayeler saklı...")

# --- 5. MÜZİK BİLETİ (Sağ Üst) ---
if 'music' not in st.session_state: st.session_state.music = False

st.markdown('<div class="ticket-fixed">', unsafe_allow_html=True)
if st.button("🎫 Müzik"):
    st.session_state.music = not st.session_state.music
st.markdown('</div>', unsafe_allow_html=True)

if st.session_state.music:
    try:
        audio_file = open('sarki.mp3', 'rb')
        st.audio(audio_file.read(), format='audio/mp3')
    except: st.sidebar.error("sarki.mp3 yüklenmemiş!")

# --- 6. İÇERİK GÖSTERİMİ ---

if "🏠 Ana Sayfa" in secim:
    st.markdown("<h1 style='text-align: center; font-family: Dancing Script; color: #ad1457; font-size: 55px;'>960 Günlük Hikayemiz</h1>", unsafe_allow_html=True)
    st.markdown('<div class="photo-card">', unsafe_allow_html=True)
    try:
        st.image("foto1.jpg", use_column_width=True, caption="İyi ki varsın sevgilim...")
    except: st.write("foto1.jpg yükleniyor...")
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-family: Dancing Script; font-size: 25px;'>Sol taraftaki takvimden yıllara tıklayarak tüm anılarımıza bakabilirsin ❤️</p>", unsafe_allow_html=True)

else:
    # Hangi yılın listesini kullanacağımızı seçiyoruz
    yıl = secim.split(" ")[1] # "📅 2023" -> "2023"
    st.markdown(f"<h1 style='text-align: center; font-family: Dancing Script; color: #ad1457;'>✨ {yıl} Anılarımız</h1>", unsafe_allow_html=True)
    
    # Fotoğraf listesini seçme
    if yıl == "2023": hedef_liste = fotos_2023
    elif yıl == "2024": hedef_liste = fotos_2024
    else: hedef_liste = fotos_2025
    
    # Listedeki TÜM FOTOĞRAFLARI ekrana basma
    for foto in hedef_liste:
        st.markdown('<div class="photo-card">', unsafe_allow_html=True)
        try:
            st.image(foto, use_column_width=True)
        except:
            st.write(f"⚠️ {foto} dosyası GitHub'da bulunamadı!")
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.balloons()
