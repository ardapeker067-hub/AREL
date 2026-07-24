import streamlit as st
import random

# 1. Sayfa Ayarları
st.set_page_config(page_title="Sonsuz Aşkımıza ❤️", page_icon="💖", layout="centered")

# 2. CSS: Fotoğraf Boyutu, Boşluklar ve Tasarım
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

    /* FOTOĞRAF KARTLARI - Boyutu buradan küçülttük */
    .photo-card {
        max-width: 380px; /* Fotoğraflar daha kibar ve küçük oldu */
        margin: 50px auto 20px auto; /* Üstten 50px boşluk bırakarak birbirinden uzaklaştırdık */
        padding: 12px;
        background: white;
        border-radius: 10px;
        box-shadow: 0 15px 35px rgba(0,0,0,0.1);
        text-align: center;
        border: 10px solid white; /* Polaroid çerçevesini kalınlaştırdık */
    }

    /* ROMANTİK SÖZLER - Boşlukları artırdık */
    .romantic-text {
        font-family: 'Dancing Script', cursive;
        font-size: 28px;
        color: #ad1457;
        text-align: center;
        padding: 60px 20px; /* Üstten ve alttan 60px boşluk (Fotoğraflar arası mesafe) */
        line-height: 1.4;
        font-weight: bold;
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

# --- 3. FOTOĞRAF LİSTELERİ ---
dosyalar_2023 = ["2023_1.jpg", "2023_2.jpg", "2023_3.jpg", "2023_4.jpg"] 
dosyalar_2024 = ["2024_1.jpg", "2024_2.jpg", "2024_3.jpg", "2024_4.jpg", "2024_5.jpg"]
dosyalar_2025 = ["2025_1.jpg", "2025_2.jpg"]

# GENİŞLETİLMİŞ ROMANTİK SÖZLER
sozler = [
    "Seninle geçen her saniye, hayatımın en değerli hazinesi...",
    "Gözlerine her baktığımda, geleceğimi görüyorum.",
    "Dünyadaki en güvenli yer, senin yanın sevgilim.",
    "960 gündür kalbim sadece senin için çarpıyor.",
    "Sen benim gökyüzündeki en parlak yıldızımsın.",
    "İyi ki varsın, iyi ki benimlesin. Seni her şeyden çok seviyorum.",
    "Seninle yaşlanmak, hayallerimin tek gerçeği.",
    "Gülüşün kalbimdeki tüm kışı bahara çeviriyor.",
    "Ellerini tuttuğumda dünya duruyor sanki...",
    "Sen benim hayatımın en güzel 'iyi ki'sisin.",
    "Aşk seninle anlam buldu kalbimde.",
    "Ömrümün geri kalanı seninle olsun, başka bir şey istemem.",
    "Her yeni güne seninle uyanmak, hayata yeniden başlamak gibi.",
    "Sana olan sevgim kelimelere sığmayacak kadar büyük.",
    "Sen benim evimsin, huzurumsun, her şeyimsin.",
    "Gönlümün sultanı, ömrümün baharı...",
    "Seninle geçen 960 gün, binlerce ömre bedel.",
    "Kalbimdeki en güzel ritim senin adın.",
    "Ruhum ruhuna sarılınca çiçek açıyor her yer.",
    "Seni sevmek, nefes almak kadar doğal ve vazgeçilmez.",
    "Hayatımın en güzel manzarasını senin gözlerinde izliyorum.",
    "Varlığın dünyadaki tüm renkleri canlandırıyor.",
    "Sen benim imkansızım değil, mucizemsin.",
    "Bin yıl yaşasam, bin yıl seni severdim.",
    "Yanında çocuk gibi mutlu, seninle dev gibi güçlüyüm."
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

# --- 5. İÇERİK DÖNGÜSÜ ---

def album_olustur(yıl, liste):
    st.markdown(f"<h1 style='text-align:center; font-family:Dancing Script; color:#ad1457; padding-bottom:30px;'>✨ {yıl} Hatıralarımız</h1>", unsafe_allow_html=True)
    
    # Her yıl sayfası için sözleri karıştır ki her seferinde farklı gelsin
    secilen_sozler = random.sample(sozler, min(len(sozler), len(liste) + 1))

    for i, foto in enumerate(liste):
        # Önce söz (İlk fotoğraftan önce de bir söz çıksın diye)
        st.markdown(f"<div class='romantic-text'>“ {secilen_sozler[i]} ”</div>", unsafe_allow_html=True)
        
        # Sonra fotoğraf kartı
        st.markdown('<div class="photo-card">', unsafe_allow_html=True)
        try:
            st.image(foto, use_column_width=True)
        except:
            st.write(f"⚠️ {foto} yüklenemedi.")
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Ayırıcı simge
        st.markdown("<div style='text-align:center; opacity:0.6; font-size:20px; margin-top:20px;'>🌸 ❤️ 🌸</div>", unsafe_allow_html=True)

# Sayfa gösterimi
if st.session_state.page == "Ana Sayfa":
    st.markdown("<h1 style='text-align:center; font-family:Dancing Script; color:#ad1457; font-size:55px; margin-top:50px;'>960 Günlük Hikayemiz</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; font-family:Dancing Script; font-size:26px; color:#ad1457;'>Zaman geçiyor ama sana olan aşkım her gün daha da büyüyor...</p>", unsafe_allow_html=True)
    
    st.markdown('<div class="photo-card">', unsafe_allow_html=True)
    try:
        st.image("foto1.jpg", use_column_width=True)
    except:
        st.write("Ana sayfa fotoğrafı (foto1.jpg) bulunamadı.")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("<p style='text-align:center; font-family:Dancing Script; font-size:22px; padding:30px;'>Yandaki menüden yıllara tıklayarak geçmişimize yolculuk yapabilirsin aşkım. ❤️</p>", unsafe_allow_html=True)

elif st.session_state.page == "2023":
    album_olustur("2023", dosyalar_2023)
    st.balloons()

elif st.session_state.page == "2024":
    album_olustur("2024", dosyalar_2024)
    st.balloons()

elif st.session_state.page == "2025":
    album_olustur("2025", dosyalar_2025)
    st.balloons()

# Arkaplan Kalpleri (25 adet)
for i in range(25):
    st.markdown(f'<div class="heart-bg" style="left:{i*4}%; animation-delay:{i*0.3}s; animation-duration:{7+i%4}s;">❤️</div>', unsafe_allow_html=True)
