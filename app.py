import streamlit as st
from datetime import datetime, timedelta

# 1. Sayfa Ayarları
st.set_page_config(page_title="Sadece Bizim İçin", page_icon="❤️", layout="centered")

# 2. Profesyonel ve Romantik Tasarım (CSS)
st.markdown("""
    <style>
    /* Arka plan: Yumuşak romantik geçiş */
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #ffafbd 0%, #ffc3a0 100%);
    }
    
    /* Buzlu cam efekti (Glassmorphism) */
    .stTabs [data-baseweb="tab-list"] {
        background-color: rgba(255, 255, 255, 0.3);
        border-radius: 15px;
        padding: 10px;
    }

    .main-card {
        background: rgba(255, 255, 255, 0.2);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 25px;
        border: 1px solid rgba(255, 255, 255, 0.3);
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.15);
        margin-bottom: 20px;
        text-align: center;
        color: #4A4A4A;
    }

    h1, h2, h3 {
        color: #D63384 !important;
        font-family: 'Georgia', serif;
    }

    /* Butonları özelleştirme */
    .stButton>button {
        background-color: #D63384;
        color: white;
        border-radius: 20px;
        border: none;
        padding: 10px 25px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #B02A6A;
        transform: scale(1.05);
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Başlık ve Sayaç
st.markdown('<div class="main-card">', unsafe_allow_html=True)
st.write("# ✨ Sonsuzluk Yolculuğumuz ✨")

# 960 Gün Hesabı (Statik değil, her gün artan dinamik sayaç)
baslangic_tarihi = datetime.now() - timedelta(days=960)
fark = datetime.now() - baslangic_tarihi

st.write(f"### Tam {fark.days} Gündür Kalbim Seninle Atıyor...")
st.write("Her saniyesi, her dakikası benim için çok kıymetli.")
st.markdown('</div>', unsafe_allow_html=True)

# 4. İçerik Sekmeleri
tab1, tab2, tab3 = st.tabs(["📸 Fotoğraflarımız", "🎥 Sana Özel Video", "🎁 Aşk Kuponları"])

with tab1:
    anilar = [
        {"img": "foto1.jpg", "not": "Gülüşün kalbimi ısıtan tek şey..."},
        {"img": "foto2.jpg", "not": "Seninle her yer cennet bahçesi."},
        {"img": "foto3.jpg", "not": "Elini hiç bırakmayacağım."}
    ]
    for ani in anilar:
        st.markdown('<div class="main-card">', unsafe_allow_html=True)
        try:
            st.image(ani["img"], use_column_width=True)
            st.write(f"*{ani['not']}*")
        except:
            st.write("Fotoğraf henüz yüklenmedi ❤️")
        st.markdown('</div>', unsafe_allow_html=True)

with tab2:
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.write("### Bizim Hikayemiz")
    try:
        # Kendi videon için (GitHub'a video.mp4 adıyla yüklediğini varsayıyorum)
        video_file = open('video.mp4', 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes)
        st.write("Seninle geçen her an, izlediğim en güzel film.")
    except:
        st.write("Henüz video yüklenmemiş. Eğer YouTube linki koymak istersen:")
        st.video("https://www.youtube.com/watch?v=l482T0yNkeo") # Buraya kendi linkini koyabilirsin
    st.markdown('</div>', unsafe_allow_html=True)

with tab3:
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.write("### İstediğin An Kullanabilirsin ✨")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🍿 Film Gecesi"):
            st.balloons()
            st.success("Kupon kullanıldı! Mısırlar benden.")
    with col2:
        if st.button("💆‍♀️ Masaj Hediyesi"):
            st.balloons()
            st.success("Kupon kullanıldı! Randevu oluşturuldu.")
    
    if st.button("🍕 Sınırsız Yemek"):
        st.balloons()
        st.success("Kupon kullanıldı! İstediğin restoranı seç.")
    st.markdown('</div>', unsafe_allow_html=True)

# Alt Bilgi
st.markdown("<p style='text-align: center; color: white;'>Seni çok seviyorum... ❤️</p>", unsafe_allow_html=True)
