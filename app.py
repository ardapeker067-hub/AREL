import streamlit as st
import random

# 1. Sayfa Ayarları
st.set_page_config(page_title="Sonsuz Aşkımıza ❤️", page_icon="💖", layout="centered")

# 2. CSS: Tasarım ve Boyutlar
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Playfair+Display:ital,wght@1&display=swap');

    [data-testid="stAppViewContainer"] {
        background: #fff5f7;
    }
    
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #ffebee 0%, #fce4ec 100%);
    }

    /* FOTOĞRAF KARTLARI - Küçük ve Zarif */
    .photo-card {
        max-width: 260px; 
        margin: 15px auto; 
        padding: 5px;
        background: white;
        border-radius: 4px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        text-align: center;
        border: 8px solid white;
    }

    /* Yazı Stilleri */
    .romantic-text {
        font-family: 'Dancing Script', cursive;
        font-size: 24px;
        color: #ad1457;
        text-align: center;
        padding: 25px 10px;
    }
    .poem-text {
        font-family: 'Playfair Display', serif;
        font-size: 19px;
        font-style: italic;
        color: #880e4f;
        text-align: center;
        padding: 40px 20px;
        line-height: 1.6;
        border-bottom: 1px solid #ffc1e3;
    }
    .troll-text {
        font-family: 'Comic Sans MS', cursive;
        font-size: 18px;
        color: #d81b60;
        text-align: center;
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
    </style>
    """, unsafe_allow_html=True)

# --- 3. VERİ LİSTELERİ ---
# Buraya fotoğraf adlarını eklemeyi unutma kanka
dosyalar_2023 = ["2023_1.jpg", "2023_2.jpg", "2023_3.jpg"]
dosyalar_2024 = ["2024_1.jpg", "2024_2.jpg", "2024_3.jpg"]
dosyalar_2025 = ["2025_1.jpg", "2025_2.jpg"]
dosyalar_troll = ["troll1.jpg", "troll2.jpg", "troll3.jpg"] # Troll fotolarını buraya ekle

kisa_sozler = [
    "960 gün değil, bir ömür yetmez seni sevmeye...",
    "Gülüşünde hayat bulduğum kadın.",
    "Dünyanın en güzel kalbine sahipsin.",
    "Seninle her an bir başka güzel sevgilim.",
    "İyi ki yolumuz birleşmiş, iyi ki varsın."
]

uzun_sozler = [
    "Bazen kelimeler yetmez ya hani, seni anlatmaya ne lügat yetiyor ne de şiirler. Sen benim başıma gelen en güzel mucizesin.",
    "Zaman geçiyor, biz büyüyoruz, anılar birikiyor ama sana olan o ilk günkü heyecanım hiç azalmıyor. Aksine her gün daha da katlanıyor.",
    "Seninle gülmek, seninle ağlamak, seninle saçmalamak... Hayatın her rengi seninle daha parlak."
]

troll_sozler = [
    "Tipe bak ya, nasıl sevmişim ben bunu? 😂",
    "Güzelliğinin yanında benim karizmanın yerle bir olduğu o an...",
    "Burada ne yapıyorduk hatırlayan var mı? jsdfkgjsdg",
    "Şekilden şekle girsek de yine en tatlı biziz!",
    "Karizma desen yok, yakışıklılık desen yok ama aşk var kanka! 😎"
]

# --- 4. YAN PANEL (SIDEBAR) ---
if 'page' not in st.session_state: st.session_state.page = "Ana Sayfa"

with st.sidebar:
    st.markdown("<h1 style='text-align:center; font-family:Dancing Script; color:#ad1457;'>💖 Aşk Menüsü</h1>", unsafe_allow_html=True)
    
    if st.button("🏠 Ana Sayfa"): st.session_state.page = "Ana Sayfa"
    st.markdown("---")
    if st.button("📅 2023 Anıları"): st.session_state.page = "2023"
    if st.button("📅 2024 Anıları"): st.session_state.page = "2024"
    if st.button("📅 2025 Anıları"): st.session_state.page = "2025"
    st.markdown("---")
    if st.button("🤪 Troll Köşesi"): st.session_state.page = "Troll"
    
    st.markdown("---")
    st.subheader("🎵 Bizim Şarkımız")
    st.write("Taa Uzak Yollardan...")
    try:
        st.audio("sarki.mp3")
    except:
        st.error("Müzik dosyası (sarki.mp3) bulunamadı.")

# --- 5. SAYFA FONKSİYONLARI ---

def album_ciz(liste, mod="romantik"):
    for i, foto in enumerate(liste):
        # Yazı kısmı
        if mod == "romantik":
            st.markdown(f"<div class='romantic-text'>{random.choice(kisa_sozler)}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='troll-text'>✨ {random.choice(troll_sozler)}</div>", unsafe_allow_html=True)
            
        # Fotoğraf kartı
        st.markdown('<div class="photo-card">', unsafe_allow_html=True)
        try:
            st.image(foto, use_column_width=True)
        except:
            st.write(f"🖼️ {foto} yüklenecek.")
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Araya uzun romantik metinler
        if i % 2 == 0:
            st.markdown(f"<div class='poem-text'>{random.choice(uzun_sozler)}</div>", unsafe_allow_html=True)

# --- 6. SAYFA İÇERİKLERİ ---

if st.session_state.page == "Ana Sayfa":
    st.markdown("<h1 style='text-align:center; font-family:Dancing Script; color:#ad1457; font-size:45px;'>Sonsuz Masalımız</h1>", unsafe_allow_html=True)
    st.markdown(f"<div class='poem-text'>960 koca gün... Dile kolay, kalbe huzur. Seninle başladığımız bu yolculuğun her durağı ayrı bir hatıra.</div>", unsafe_allow_html=True)
    st.markdown('<div class="photo-card" style="max-width:320px;">', unsafe_allow_html=True)
    st.image("foto1.jpg") # Ana fotoğrafın
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown(f"<div class='romantic-text'>Tüm anılarımızı görmek için yandaki menüyü kullanabilirsin sevgilim. Müziği açmayı unutma! 🎵</div>", unsafe_allow_html=True)

elif st.session_state.page == "2023":
    st.markdown("<h2 style='text-align:center; font-family:Dancing Script;'>✨ 2023: Her Şeyin Başladığı Yer</h2>", unsafe_allow_html=True)
    album_ciz(dosyalar_2023)
    st.balloons()

elif st.session_state.page == "2024":
    st.markdown("<h2 style='text-align:center; font-family:Dancing Script;'>✨ 2024: Aşkla Büyüdüğümüz Yıl</h2>", unsafe_allow_html=True)
    album_ciz(dosyalar_2024)
    st.balloons()

elif st.session_state.page == "2025":
    st.markdown("<h2 style='text-align:center; font-family:Dancing Script;'>✨ 2025: Geleceğe İlk Adımlar</h2>", unsafe_allow_html=True)
    album_ciz(dosyalar_2025)
    st.balloons()

elif st.session_state.page == "Troll":
    st.markdown("<h1 style='text-align:center; font-family:Dancing Script; color:#ad1457;'>🤪 Bizim Halleri</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;'>Biraz da gülelim dedik... İyi ki bu kadar saçmalayabiliyoruz!</p>", unsafe_allow_html=True)
    album_ciz(dosyalar_troll, mod="troll")
    st.snow() # Troll sayfasına kar yağdıralım değişiklik olsun :)

# Arkaplan Kalpleri
for i in range(15):
    st.markdown(f'<div class="heart-bg" style="left:{i*7}%; animation-delay:{i*0.5}s; animation-duration:{8+i%3}s;">❤️</div>', unsafe_allow_html=True)
