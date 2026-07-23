import streamlit as st
from datetime import datetime, timedelta

# 1. Sayfa Ayarları
st.set_page_config(page_title="Bizim Hikayemiz", page_icon="❤️", layout="centered")

# 2. Gelişmiş Tasarım (CSS)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Playfair+Display:ital,wght@1,500&display=swap');

    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #fce4ec 0%, #f1f8e9 100%);
    }

    .love-text {
        font-family: 'Playfair Display', serif;
        font-size: 24px;
        color: #880e4f;
        text-align: center;
        padding: 40px 10px;
        line-height: 1.6;
        font-style: italic;
    }

    .photo-frame {
        background: white;
        padding: 15px;
        border-radius: 5px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        margin-top: 50px;
        margin-bottom: 50px;
        transform: rotate(-1deg);
        transition: 0.5s;
    }
    
    .photo-frame:hover {
        transform: rotate(0deg) scale(1.02);
    }

    .counter-card {
        background: rgba(255, 255, 255, 0.4);
        backdrop-filter: blur(10px);
        border-radius: 30px;
        padding: 20px;
        text-align: center;
        border: 1px solid rgba(255,255,255,0.5);
        margin-bottom: 50px;
    }

    .stButton>button {
        width: 100%;
        background: #ad1457;
        color: white;
        border-radius: 50px;
        height: 3em;
        font-weight: bold;
        border: none;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Müzik ve Giriş Kontrolü
if 'play' not in st.session_state:
    st.session_state.play = False

if not st.session_state.play:
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: #ad1457;'>Sana Bir Sürprizim Var...</h2>", unsafe_allow_html=True)
    if st.button("Sürprizi Başlat ❤️"):
        st.session_state.play = True
        st.rerun()
else:
    # Arka Planda Çalacak Müzik (YouTube'dan Taa Uzak Yollardan)
    # Autoplay için küçük bir hile:
    st.markdown("""
        <iframe width="0" height="0" src="https://www.youtube.com/embed/S2C9X-98b-E?autoplay=1" 
        frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
        """, unsafe_allow_html=True)

    # 4. Başlık ve Sayaç
    st.markdown('<div class="counter-card">', unsafe_allow_html=True)
    baslangic = datetime.now() - timedelta(days=960)
    fark = datetime.now() - baslangic
    st.markdown(f"<h1 style='font-family: Dancing Script; color: #ad1457;'>Tam {fark.days} Gündür...</h1>", unsafe_allow_html=True)
    st.write("Taa uzak yollardan koştum geldim senin kollarına...")
    st.markdown('</div>', unsafe_allow_html=True)

    # 5. Fotoğraflar ve Romantik Sözler (Aralıklı Yapı)
    
    # --- 1. Bölüm ---
    st.markdown('<div class="photo-frame">', unsafe_allow_html=True)
    st.image("foto1.jpg", use_column_width=True, caption="O ilk bakış...")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="love-text">"Seninle geçen her gün, hayatımın en güzel şarkısının bir notası gibi. Taa uzak yollardan gelmişiz gibi ama hep birbirimizi beklemişiz gibi..."</div>', unsafe_allow_html=True)

    # --- 2. Bölüm ---
    st.markdown('<div class="photo-frame" style="transform: rotate(1deg);">', unsafe_allow_html=True)
    st.image("foto2.jpg", use_column_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="love-text">"Dünya ne kadar büyük olursa olsun, benim huzur bulduğum tek yer senin yanın. Sesin, en güzel melodi kalbimde çalan."</div>', unsafe_allow_html=True)

    # --- 3. Bölüm ---
    st.markdown('<div class="photo-frame">', unsafe_allow_html=True)
    st.image("foto3.jpg", use_column_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="love-text">"960 gün önce başlayan bu masal, sonsuza kadar sürsün diye her gün dua ediyorum. İyi ki benimlesin, iyi ki varsın sevgilim."</div>', unsafe_allow_html=True)

    # 6. Video Bölümü (Opsiyonel)
    st.write("---")
    st.markdown("<h2 style='text-align: center; font-family: Dancing Script;'>Bizim Hikayemiz</h2>", unsafe_allow_html=True)
    try:
        video_file = open('video.mp4', 'rb')
        st.video(video_file.read())
    except:
        st.write("*(Buraya sevgilinle olan videonu yükleyebilirsin!)*")

    # 7. Kapanış
    st.balloons()
    st.markdown("<br><br><h3 style='text-align: center; color: #ad1457;'>Seni Seviyorum ❤️</h3><br><br>", unsafe_allow_html=True)
