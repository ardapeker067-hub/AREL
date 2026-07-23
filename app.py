import streamlit as st
from datetime import datetime, timedelta

# 1. Sayfa Ayarları
st.set_page_config(page_title="Bizim Dünyamız", page_icon="💖", layout="centered")

# Görsel CSS Güzelleştirmesi
st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(-45deg, #ff9a9e, #fad0c4, #fad0c4, #ff9a9e);
        background-size: 400% 400%;
        animation: gradient 15s ease infinite;
    }
    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    .photo-card {
        background-color: rgba(255, 255, 255, 0.25);
        padding: 15px;
        border-radius: 15px;
        backdrop-filter: blur(5px);
        margin-bottom: 20px;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Başlık
st.write(f"<h1 style='text-align: center; color: white;'>✨ İyi ki Benimlesin ✨</h1>", unsafe_allow_html=True)

# 3. Aşk Sayacı (Tam 960 GÜN Ayarı)
# Eğer tam 960 gün görünmesini istiyorsan, bugünden 960 gün öncesini otomatik hesaplıyoruz.
# Ama istersen buraya gerçek tanışma tarihini (Yıl, Ay, Gün) yazabilirsin:
tanisma_tarihi = datetime.now() - timedelta(days=960) 
fark = datetime.now() - tanisma_tarihi

st.write(f"<h3 style='text-align: center; color: white;'>Tam {fark.days} gündür hayatımın anlamısın... ❤️</h3>", unsafe_allow_html=True)

st.write("---")

# 4. Sekmeler
tab1, tab2, tab3 = st.tabs(["📸 Anılarımız", "💌 Notum", "🎁 Kuponların"])

with tab1:
    anilar = [
        {"img": "foto1.jpg", "text": "Bu gülüşün her şeye değer..."},
        {"img": "foto2.jpg", "text": "Seninle her an bir macera."},
        {"img": "foto3.jpg", "text": "Seni çok seviyorum!"}
    ]
    for ani in anilar:
        st.markdown('<div class="photo-card">', unsafe_allow_html=True)
        try:
            st.image(ani["img"], use_column_width=True)
            st.write(ani["text"])
        except:
            st.write("Fotoğraf dosyası bulunamadı!")
        st.markdown('</div>', unsafe_allow_html=True)

with tab2:
    st.info("Buraya onun için en içten duygularını yazabilirsin kanka. O okuduğunda yüzündeki gülümseme her şeye değecek.")

with tab3:
    st.write("### Hediye Kuponların")
    if st.button("🍿 Sinema Gecesi Kuponu"):
        st.success("Kupon Alındı! Bu akşam film seçimi sende.")
    if st.button("🍕 Yemek Ismarlama Kuponu"):
        st.warning("Bu kupon bir akşam yemeği kazandırır!")

# 5. Müzik Kısmı (DÜZELTİLDİ)
st.write("---")
st.write("🎵 **Bizim Şarkımız**")

# ÖNEMLİ: YouTube linkini tırnak içine tam olarak yapıştır. 
# Örnek olarak çalışan bir link koydum, sen bunu kendi linkinle değiştir.
youtube_linki = "https://www.youtube.com/watch?v=-jDEFIRkeg4&list=RD-jDEFIRkeg4&start_radio=1" # Buraya kendi linkini koy
st.video(youtube_linki)

st.markdown("<p style='text-align: center; color: white; opacity: 0.8;'>Sonsuza Dek...</p>", unsafe_allow_html=True)
