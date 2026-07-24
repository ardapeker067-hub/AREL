import streamlit as st
import random

# 1. Sayfa Ayarları
st.set_page_config(page_title="Sonsuz Aşkımıza ❤️", page_icon="💖", layout="centered")

# 2. CSS: Fotoğrafları Küçültme ve Yoğun Yazı Tasarımı
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Playfair+Display:ital,wght@1&display=swap');

    [data-testid="stAppViewContainer"] {
        background: #fff5f7;
    }
    
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #ffebee 0%, #fce4ec 100%);
    }

    /* FOTOĞRAF KARTLARI - İyice Küçültüldü (280px) */
    .photo-card {
        max-width: 280px; 
        margin: 20px auto; 
        padding: 8px;
        background: white;
        border-radius: 5px;
        box-shadow: 0 8px 20px rgba(0,0,0,0.1);
        text-align: center;
        border: 10px solid white; /* Polaroid efekti */
    }

    /* Romantik Kısa Sözler */
    .romantic-text {
        font-family: 'Dancing Script', cursive;
        font-size: 24px;
        color: #ad1457;
        text-align: center;
        padding: 30px 10px;
        line-height: 1.4;
    }

    /* Şiirsel Uzun Metinler */
    .poem-text {
        font-family: 'Playfair Display', serif;
        font-size: 20px;
        font-style: italic;
        color: #880e4f;
        text-align: center;
        padding: 50px 20px;
        line-height: 1.8;
        border-bottom: 1px solid #ffc1e3;
        border-top: 1px solid #ffc1e3;
        margin: 40px 0;
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

# --- 3. BÜYÜK SÖZ HAVUZU (Burayı istediğin kadar uzatabilirsin) ---
kisa_sozler = [
    "Gülüşün, dünyadaki tüm karanlıkları aydınlatıyor sevgilim.",
    "Seninle geçen 960 gün, ömrümün en güzel masalı.",
    "Ellerini tuttuğum an, zamanın durmasını istiyorum.",
    "Kalbimdeki tek ritim, senin adın.",
    "İyi ki hayatımdasın, iyi ki benimlesin...",
    "Seni sevmek, nefes almak kadar doğal benim için.",
    "Gözlerine baktığımda huzuru görüyorum.",
    "960 gündür her sabah seninle yeniden doğuyorum.",
    "Sen benim evimsin, en huzurlu limanımsın.",
    "Dünyanın en güzel manzarası, senin yüzün."
]

uzun_sozler = [
    "Biliyorum ki biz, birbirine geç kalmış iki ruhun nihayet kavuşmasıyız. Seninle geçen her dakika, her anı zihnime altın harflerle kazındı. İyi ki varsın...",
    "Zaman akıp gidiyor ama sana olan aşkım her geçen saniye daha da kök salıyor. 960 gün önce başlayan bu yolculuk, sonsuza kadar sürsün istiyorum.",
    "Sen sadece sevdiğim değil, aynı zamanda en yakın arkadaşım, sırdaşım ve dünyamsın. Seninle her şey o kadar kolay ve güzel ki...",
    "Hangi kelime senin güzelliğini anlatmaya yeter? Hangi şiir senin kalbinin temizliğini tarif edebilir? Ben sadece seni yaşamayı seçiyorum.",
    "Bazen sadece oturup seni izlemek istiyorum. Dünyanın bütün karmaşası içinde bulduğum en büyük sessizlik ve huzursun sen."
]

final_notlari = {
    "2023": "2023 bizim için bir başlangıcın, kök salmanın yılıydı. Her anı pırlanta değerinde...",
    "2024": "2024'te daha çok büyüdük, daha çok güldük. Zorlukları beraber aştık, aşkımızı taçlandırdık.",
    "2025": "2025 bizim yılımız olacak. El ele, omuz omuza daha nice güzel günlere...",
}

# --- 4. VERİLER ---
dosyalar_2023 = ["2023_1.jpg", "2023_2.jpg", "2023_3.jpg", "2023_4.jpg"]
dosyalar_2024 = ["2024_1.jpg", "2024_2.jpg", "2024_3.jpg", "2024_4.jpg", "2024_5.jpg"]
dosyalar_2025 = ["2025_1.jpg", "2025_2.jpg"]

# --- 5. İÇERİK OLUŞTURUCU ---

def album_olustur(yıl, liste):
    st.markdown(f"<h1 style='text-align:center; font-family:Dancing Script; color:#ad1457; font-size:40px;'>✨ {yıl} Anılarımız</h1>", unsafe_allow_html=True)
    
    # Başlangıca uzun bir romantik giriş
    st.markdown(f"<div class='poem-text'>{random.choice(uzun_sozler)}</div>", unsafe_allow_html=True)

    for i, foto in enumerate(liste):
        # Her fotoğraftan önce kısa bir söz
        st.markdown(f"<div class='romantic-text'>{random.choice(kisa_sozler)}</div>", unsafe_allow_html=True)
        
        # Küçük Fotoğraf Kartı
        st.markdown('<div class="photo-card">', unsafe_allow_html=True)
        try:
            st.image(foto, use_column_width=True)
        except:
            st.write(f"🖼️ {foto}")
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Araya serpiştirilen rastgele uzun metinler (Her 2 fotoda bir)
        if i % 2 == 0 and i != 0:
            st.markdown(f"<div class='poem-text'>{random.choice(uzun_sozler)}</div>", unsafe_allow_html=True)

    # SAYFA SONU - O yıla özel farklı final sözü
    st.markdown(f"<div class='poem-text' style='background:#fce4ec;'>🌟 {final_notlari[yıl]} <br><br> Seni seviyorum...</div>", unsafe_allow_html=True)

# --- 6. NAVİGASYON ---
if 'page' not in st.session_state: st.session_state.page = "Ana Sayfa"

with st.sidebar:
    st.markdown("<h1 style='text-align:center; font-family:Dancing Script; color:#ad1457;'>❤️ Aşk Defterimiz</h1>", unsafe_allow_html=True)
    if st.button("🏠 Başlangıç"): st.session_state.page = "Ana Sayfa"
    if st.button("📅 2023 Yılı"): st.session_state.page = "2023"
    if st.button("📅 2024 Yılı"): st.session_state.page = "2024"
    if st.button("📅 2025 Yılı"): st.session_state.page = "2025"

# --- 7. SAYFALAR ---
if st.session_state.page == "Ana Sayfa":
    st.markdown("<h1 style='text-align:center; font-family:Dancing Script; color:#ad1457; font-size:50px;'>960 Günlük Mucizemiz</h1>", unsafe_allow_html=True)
    
    st.markdown(f"<div class='poem-text'>{random.choice(uzun_sozler)}</div>", unsafe_allow_html=True)
    
    st.markdown('<div class="photo-card" style="max-width:350px;">', unsafe_allow_html=True)
    try: st.image("foto1.jpg", use_column_width=True)
    except: st.write("Ana Sayfa Resmi")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown(f"<div class='romantic-text'>Seninle her şey daha güzel, her şey daha anlamlı...</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='poem-text'>Bu sayfalar bizim hikayemizi anlatıyor sevgilim. Sol taraftan yılları seçerek hatıralarımız arasında kaybolabilirsin.</div>", unsafe_allow_html=True)

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
