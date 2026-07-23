import streamlit as st

# Sayfa Ayarları
st.set_page_config(page_title="Bizim Hikayemiz", page_icon="❤️", layout="centered")

# Arka planı biraz güzelleştirelim (Opsiyonel)
st.markdown("""
    <style>
    .main {
        background-color: #fff5f5;
    }
    h1 {
        color: #ff4b4b;
        text-align: center;
        font-family: 'Dancing Script', cursive;
    }
    .stText {
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# Başlık
st.title("❤️ İyi Ki Varsın Sevgilim ❤️")
st.write("---")

# Fotoğraflar ve Sözler Listesi
# Burayı fotoğraflarının isimlerine ve yazmak istediğin sözlere göre düzenle
anilar = [
    {
        "foto": "foto1.jpg", 
        "soz": "Seninle içtiğimiz o ilk kahve, hayatımın en tatlı anıydı..."
    },
    {
        "foto": "foto2.jpg", 
        "soz": "Gülüşünde saklı olan o huzuru başka hiçbir yerde bulamadım."
    },
    {
        "foto": "foto3.jpg", 
        "soz": "Her geçen gün seninle daha güzel anılar biriktirmek dileğiyle."
    }
]

# Fotoğrafları Ekrana Basma
for ani in anilar:
    try:
        st.image(ani["foto"], use_column_width=True)
        st.subheader(ani["soz"])
        st.write("---")
    except:
        st.warning(f"{ani['foto']} dosyası bulunamadı, lütfen klasöre ekle!")

# Kapanış Notu
st.balloons() # Sayfa açıldığında balonlar uçar
st.info("Seni her gün daha çok seviyorum. ❤️")

# Spotify Çalma Listesi (Opsiyonel - Linki değiştirirsin)
st.write("🎵 Bizim Şarkımız")
st.video("https://www.youtube.com/watch?v=YOUR_VIDEO_ID") # Ya da YouTube linki