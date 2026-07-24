import streamlit as st
import random

# 1. Sayfa Ayarları
st.set_page_config(page_title="Sonsuz Aşkımıza ❤️", page_icon="💖", layout="centered")

# 2. CSS: Tasarım, Boyutlar ve Yeni Alt Bölüm
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

    /* FOTOĞRAF KARTLARI - Boyutu biraz daha küçülttük (320px) */
    .photo-card {
        max-width: 320px; 
        margin: 40px auto 10px auto; 
        padding: 10px;
        background: white;
        border-radius: 8px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.08);
        text-align: center;
        border: 8px solid white;
    }

    /* Romantik Sözler (Fotoğraf Araları) */
    .romantic-text {
        font-family: 'Dancing Script', cursive;
        font-size: 24px;
        color: #ad1457;
        text-align: center;
        padding: 40px 10px;
        line-height: 1.3;
    }

    /* EN ALTTAKİ ÖZEL MESAJ (Satır Satır) */
    .final-poem {
        font-family: 'Playfair Display', serif;
        font-size: 22px;
        font-style: italic;
        color: #880e4f;
        text-align: center;
        margin-top: 100px;
        margin-bottom: 50px;
        line-height: 2;
        padding: 30px;
        border-top: 1px solid #ffc1e3;
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
    </style>
    """, unsafe_allow_html=True)

# --- 3. VERİLER ---
dosyalar_2023 = ["2023_1.jpg", "2023_2.jpg", "2023_3.jpg", "2023_4.jpg"] 
dosyalar_2024 = ["2024_1.jpg", "2024_2.jpg", "2024_3.jpg", "2024_4.jpg", "2024_5.jpg"]
dosyalar_2025 = ["2025_1.jpg", "2025_2.jpg"]

sozler = [
    "Seninle her an bir başka güzel...",
    "Gülüşün kalbimdeki en güzel manzara.",
    "İyi ki hayatımdasın sevgilim.",
    "960 gün değil, bir ömür yetmez sana.",
    "Ellerini hiç bırakmayacağım.",
    "Gözlerin, kaybolmak istediğim tek yer."
]

# --- 4. NAVİGASYON ---
if 'page' not in st.session_state:
    st.session_state.page = "Ana Sayfa"

with st.sidebar:
    st.markdown("<h1 style='text-align:center; font-family:Dancing Script; color:#ad1457;'>🗓️ Menü</h1>", unsafe_allow_html=True)
    if st.button("🏠 Ana Sayfa"): st.session_state.page = "Ana Sayfa"
    if st.button("📅 2023"): st.session_state.page = "2023"
    if st.button("📅 2024"): st.session_state.page = "2024"
    if st.button("📅 2025"): st.session_state.page = "2025"
    
    st.sidebar.markdown("---")
    if st.sidebar.button("🎫 Müzik Aç/Kapat"):
        if 'm' not in st.session_state: st.session_state.m = False
        st.session_state.m = not st.session_state.m

    if st.session_state.get('m', False):
        try: st.sidebar.audio("sarki.mp3")
        except: st.sidebar.error("Müzik yüklenemedi.")

# --- 5. İÇERİK FONKSİYONU ---

def final_mesaji():
    st.markdown("""
        <div class="final-poem">
            Birlikte geçen tam 960 gün...<br>
            Her sabah seninle uyandığım hayallere,<br>
            Her akşam sesinle bulduğum huzura şükrediyorum.<br>
            Sen benim hayatımın en güzel şiiri,<br>
            Hiç bitmeyecek en mutlu hikayemsin.<br>
            Seni her geçen gün, bir öncekinden daha çok...<br>
            Sonsuza kadar seviyorum. ❤️
        </div>
    """, unsafe_allow_html=True)

def album_olustur(yıl, liste):
    st.markdown(f"<h1 style='text-align:center; font-family:Dancing Script; color:#ad1457;'>✨ {yıl} Yılı</h1>", unsafe_allow_html=True)
    for i, foto in enumerate(liste):
        st.markdown(f"<div class='romantic-text'>“ {random.choice(sozler)} ”</div>", unsafe_allow_html=True)
        st.markdown('<div class="photo-card">', unsafe_allow_html=True)
        try:
            st.image(foto, use_column_width=True)
        except:
            st.write(f"🖼️ {foto} (Fotoğraf buraya gelecek)")
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Her sayfanın altına o romantik finali ekleyelim
    final_mesaji()

# --- 6. SAYFALAR ---

if st.session_state.page == "Ana Sayfa":
    st.markdown("<h1 style='text-align:center; font-family:Dancing Script; color:#ad1457; font-size:45px;'>Seni Çok Seviyorum...</h1>", unsafe_allow_html=True)
    st.markdown('<div class="photo-card">', unsafe_allow_html=True)
    try: st.image("foto1.jpg", use_column_width=True)
    except: st.write("Ana Sayfa Fotoğrafı")
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; font-family:Dancing Script; font-size:22px;'>960 gündür yazdığımız bu hikayeye hoş geldin sevgilim.</p>", unsafe_allow_html=True)
    final_mesaji()

elif st.session_state.page == "2023":
    album_olustur("2023", dosyalar_2023)
    st.balloons()

elif st.session_state.page == "2024":
    album_olustur("2024", dosyalar_2024)
    st.balloons()

elif st.session_state.page == "2025":
    album_olustur("2025", dosyalar_2025)
    st.balloons()

# Arkaplan Kalpleri
for i in range(15):
    st.markdown(f'<div class="heart-bg" style="left:{i*7}%; animation-delay:{i*0.5}s; animation-duration:{8+i%3}s;">❤️</div>', unsafe_allow_html=True)
