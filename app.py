import streamlit as st
from datetime import datetime

# 1. Sayfa Ayarları ve CSS (Görselliği burada patlatıyoruz)
st.set_page_config(page_title="Bizim Hikayemiz", page_icon="💖", layout="centered")

st.markdown("""
    <style>
    /* Arka plan animasyonu */
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
        background-size: 400% 400%;
        animation: gradient 15s ease infinite;
    }
    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* Kart tasarımı */
    .photo-card {
        background-color: rgba(255, 255, 255, 0.2);
        padding: 20px;
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.3);
        backdrop-filter: blur(10px);
        margin-bottom: 25px;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    
    .stButton>button {
        border-radius: 50px;
        background: white;
        color: #e73c7e;
        font-weight: bold;
        border: none;
        transition: 0.3s;
    }
    .stButton>button:hover {
        transform: scale(1.05);
        background: #ffebee;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Üst Kısım: Başlık ve Karşılama
st.write(f"<h1 style='text-align: center; color: white; font-family: cursive;'>✨ İyi ki Benimlesin ✨</h1>", unsafe_allow_html=True)

# 3. Aşk Sayacı (Tanışma veya Yıldönümü tarihinizi girin)
baslangic_tarihi = datetime(2023, 5, 14) # YIL, AY, GÜN
fark = datetime.now() - baslangic_tarihi
st.write(f"<h3 style='text-align: center; color: white;'>Tam {fark.days} gündür hayatımın anlamısın... ❤️</h3>", unsafe_allow_html=True)

st.write("---")

# 4. İnteraktif Bölüm: "Bizim Anılarımız" (Tab yapısı ile daha modern)
tab1, tab2, tab3 = st.tabs(["📸 Fotoğraflarımız", "💌 Notlarım", "🎁 Kuponların"])

with tab1:
    # Fotoğrafları birer "Kart" içinde gösterelim
    anilar = [
        {"img": "foto1.jpg", "text": "Bu gülüşün, dünyadaki en güzel manzara..."},
        {"img": "foto2.jpg", "text": "Elini ilk tuttuğumda zaman dursun istemiştim."},
        {"img": "foto3.jpg", "text": "Her maceramızda yanımda olduğun için teşekkürler."}
    ]
    
    for ani in anilar:
        st.markdown('<div class="photo-card">', unsafe_allow_html=True)
        try:
            st.image(ani["img"], use_column_width=True)
            st.write(f"*{ani['text']}*")
        except:
            st.write("Fotoğraf yüklenemedi (İsmini kontrol et!)")
        st.markdown('</div>', unsafe_allow_html=True)

with tab2:
    st.write("### Sana Küçük Bir Not...")
    st.info("""
    Buraya sevgiline yazmak istediğin uzun ve romantik bir mektup yazabilirsin. 
    Mesela: 'Seninle tanıştığım günden beri dünyam daha renkli. Sadece bir sevgili değil, 
    en iyi dostum oldun...'
    """)
    st.balloons()

with tab3:
    st.write("### Senin İçin Hazırladığım Hediye Kuponları")
    st.write("İstediğin zaman kullanabilirsin, itiraz hakkım yok! 😉")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🎫 Sinema & Patlamış Mısır"):
            st.success("Kupon kullanıldı! Bu akşam film bizde. 🍿")
    with col2:
        if st.button("🍕 En Sevdiğin Yemek"):
            st.success("Kupon kullanıldı! Menüde ne varsa ben ısmarlıyorum. 🍕")
    
    if st.button("💆 15 Dakika Masaj"):
        st.success("Kupon kullanıldı! Hemen yerini hazırla. 💆‍♀️")

# 5. Alt Kısım: Müzik
st.write("---")
st.write("🎵 **Bu şarkıyı dinlerken bizi düşün...**")
# Buraya sizin şarkınızın YouTube linkini koyabilirsin
st.video("https://www.youtube.com/watch?v=YOUR_VIDEO_ID") 

# Sayfanın en altına küçük bir imza
st.markdown("<p style='text-align: center; color: white; opacity: 0.7;'>Seni Seviyorum...</p>", unsafe_allow_html=True)
