import streamlit as st
import random

# 1. Sayfa Ayarları
st.set_page_config(page_title="Sonsuz Aşkımıza ❤️", page_icon="💖", layout="centered")

# 2. CSS: Tasarım ve Süslemeler
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Playfair+Display:ital,wght@1&display=swap');

    [data-testid="stAppViewContainer"] { background: #fff5f7; }
    [data-testid="stSidebar"] { background: linear-gradient(180deg, #ffebee 0%, #fce4ec 100%); }

    /* FOTOĞRAF KARTLARI */
    .photo-card {
        max-width: 250px; 
        margin: 10px auto; 
        padding: 5px;
        background: white;
        border-radius: 10px;
        box-shadow: 0 8px 20px rgba(0,0,0,0.1);
        text-align: center;
        border: 6px solid white;
    }

    /* Farklı Yazı Tipleri */
    .short-quote {
        font-family: 'Dancing Script', cursive;
        font-size: 22px;
        color: #ad1457;
        text-align: center;
        padding: 15px 5px;
    }
    .long-quote {
        font-family: 'Playfair Display', serif;
        font-size: 18px;
        font-style: italic;
        color: #880e4f;
        text-align: center;
        padding: 30px 20px;
        line-height: 1.6;
        border-left: 3px solid #ffc1e3;
        margin: 20px 0;
    }
    .final-touch {
        font-family: 'Dancing Script', cursive;
        font-size: 30px;
        color: #d81b60;
        text-align: center;
        padding: 50px 10px;
        background: rgba(255, 255, 255, 0.4);
        border-radius: 15px;
        margin-top: 40px;
    }
    .special-troll {
        font-family: 'Dancing Script', cursive;
        font-size: 26px;
        color: #ff4081;
        text-align: center;
        font-weight: bold;
        padding: 20px 0;
    }
    .heart-bg {
        position: fixed; top: -10%; color: #ff4081; font-size: 20px; z-index: 0; animation: fall linear infinite;
    }
    @keyframes fall { to { transform: translateY(110vh) rotate(360deg); } }
    </style>
    """, unsafe_allow_html=True)

# --- 3. DEV SÖZ LİSTELERİ ---
kisa_sozler = [
    "Seninle her saniye bir ömre bedel...", "Gülüşün kalbimin en tatlı melodisi.", "Dünyanın en güzel manzarası senin yüzün.",
    "Bakışlarında huzuru bulduğum tek insansın.", "Elimi tuttuğun an her şey güzelleşiyor.", "İyi ki varsın, iyi ki benimlesin sevgilim.",
    "960 gündür kalbim sadece senin için çarpıyor.", "Aşk seninle anlam buluyor her gün.", "Seni sevmek nefes almak kadar doğal.",
    "Sen benim evimsin, en güvenli limanımsın.", "Ruhumun eşi, kalbimin neşesi...", "Gözlerin gökyüzü, gülüşün güneş.",
    "Hayatımın en güzel 'iyi ki'sisin.", "Yanında kendimi bulduğum kadın.", "Sana olan aşkım her gün daha da büyüyor.",
    "Sonsuzluğa seninle yürümek istiyorum.", "Gönlümün sultanı, ömrümün baharı."
]

uzun_sozler = [
    "Bazen kelimeler yetmez ya hani, seni anlatmaya ne lügat yetiyor ne de şiirler. Sen benim başıma gelen en güzel mucizesin.",
    "Zaman geçiyor, biz büyüyoruz, anılar birikiyor ama sana olan o ilk günkü heyecanım hiç azalmıyor. Aksine her gün daha da katlanıyor.",
    "Biliyorum ki biz, birbirine geç kalmış iki ruhun nihayet kavuşmasıyız. Seninle geçen her dakika zihnime altın harflerle kazındı.",
    "Sen sadece sevdiğim değil, aynı zamanda en yakın arkadaşım, sırdaşım ve dünyamsın. Seninle her şey o kadar kolay ve güzel ki...",
    "Hangi şiir senin kalbinin temizliğini tarif edebilir? Ben sadece seni yaşamayı, seninle yaşlanmayı seçiyorum her sabah."
]

final_notlari = {
    "Ana Sayfa": "Seninle başladığımız bu hikaye, ömrümün en kıymetli hazinesi. Beraber yaşlanacağımız nice 960 günlere sevgilim... ❤️",
    "2023": "2023 bizi biz yapan, temellerimizi atan yıldı. Her zorlukta birbirimize daha sıkı sarıldığımız o günler için teşekkür ederim. ✨",
    "2024": "2024'te aşkımız çiçek açtı, her anı bir pırlanta gibi parladı. Seninle büyümenin keyfi hiçbir şeyde yok. 🌸",
    "2025": "Yeni hayaller, yeni umutlar ve değişmeyen tek şey: Sana olan sonsuz aşkım. Bu yıl da sadece biz olalım. 🥂",
    "Troll": "En çok seninle saçmalamayı, seninle kahkaha atmayı seviyorum. Aşk sadece romantizm değil, beraber çocuklaşabilmektir. 😂❤️"
}

# --- 4. VERİLER VE NAVİGASYON ---
dosyalar_2023 = ["2023_1.jpg", "2023_2.jpg", "2023_3.jpg", "2023_4.jpg"]
dosyalar_2024 = ["2024_1.jpg", "2024_2.jpg", "2024_3.jpg", "2024_4.jpg"]
dosyalar_2025 = ["2025_1.jpg", "2025_2.jpg"]
dosyalar_troll = ["troll1.jpg", "troll2.jpg", "troll3.jpg", "troll4.jpg"]

if 'page' not in st.session_state: st.session_state.page = "Ana Sayfa"

with st.sidebar:
    st.markdown("<h1 style='text-align:center; font-family:Dancing Script; color:#ad1457;'>💖 Aşk Menüsü</h1>", unsafe_allow_html=True)
    if st.button("🏠 Ana Sayfa"): st.session_state.page = "Ana Sayfa"
    st.markdown("---")
    if st.button("📅 2023"): st.session_state.page = "2023"
    if st.button("📅 2024"): st.session_state.page = "2024"
    if st.button("📅 2025"): st.session_state.page = "2025"
    st.markdown("---")
    if st.button("🤪 Troll Köşesi"): st.session_state.page = "Troll"
    st.markdown("---")
    st.subheader("🎵 Bizim Şarkımız")
    try: st.audio("sarki.mp3")
    except: st.error("Müzik dosyası bulunamadı.")

# --- 5. ALBÜM ÇİZİCİ FONKSİYON ---

def sayfa_olustur(liste, sayfa_ismi, mod="normal"):
    st.markdown(f"<h1 style='text-align:center; font-family:Dancing Script; color:#ad1457;'>✨ {sayfa_ismi} ✨</h1>", unsafe_allow_html=True)
    
    # Karıştırma yapıyoruz ki her girişte farklı sözler gelsin
    secilen_kisalar = random.sample(kisa_sozler, len(liste))
    secilen_uzunlar = random.sample(uzun_sozler, min(len(uzun_sozler), len(liste)))

    for i, foto in enumerate(liste):
        # Troll sayfası özel içerik kontrolü
        if mod == "troll":
            if i == 1: st.markdown("<div class='special-troll'>✨ 👀 Gözlerine ölmemek elde mi? 👀 ✨</div>", unsafe_allow_html=True)
            elif i == 2: st.markdown("<div class='special-troll'>🌈 🍭 Tipe bak yerim ben bunu! 🍭 🌈</div>", unsafe_allow_html=True)
            else: st.markdown(f"<div class='short-quote'>🤪 {random.choice(['Tipe bak ya!', 'Karizma yerlerde...', 'Ne yapıyoruz burada?'])}</div>", unsafe_allow_html=True)
        else:
            # Normal sayfalarda kısa söz
            st.markdown(f"<div class='short-quote'>{secilen_kisalar[i]}</div>", unsafe_allow_html=True)

        # Fotoğraf Kartı
        st.markdown('<div class="photo-card">', unsafe_allow_html=True)
        try: st.image(foto, use_column_width=True)
        except: st.write(f"🖼️ {foto}")
        st.markdown('</div>', unsafe_allow_html=True)

        # Araya uzun söz serpiştir (her 2 fotoğrafta bir)
        if i % 2 == 0 and i < len(secilen_uzunlar):
            st.markdown(f"<div class='long-quote'>{secilen_uzunlar[i]}</div>", unsafe_allow_html=True)

    # HER PANELİN EN ALTINA FARKLI SÖZ
    st.markdown(f"<div class='final-touch'>{final_notlari[sayfa_ismi]}</div>", unsafe_allow_html=True)

# --- 6. SAYFA GÖSTERİMLERİ ---

if st.session_state.page == "Ana Sayfa":
    st.markdown("<h1 style='text-align:center; font-family:Dancing Script; color:#ad1457; font-size:45px;'>Sonsuz Masalımız</h1>", unsafe_allow_html=True)
    st.markdown('<div class="photo-card" style="max-width:320px;">', unsafe_allow_html=True)
    try: st.image("foto1.jpg")
    except: st.write("Ana Sayfa Resmi")
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown("<div class='long-quote'>Her şey seninle başladı sevgilim... Kalbimdeki en özel köşe senin.</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='final-touch'>{final_notlari['Ana Sayfa']}</div>", unsafe_allow_html=True)

elif st.session_state.page == "Troll":
    sayfa_olustur(dosyalar_troll, "Troll", mod="troll")
    st.snow()
else:
    sayfa_olustur(eval(f"dosyalar_{st.session_state.page}"), st.session_state.page)
    st.balloons()

# Arkaplan Kalpleri
for i in range(15):
    st.markdown(f'<div class="heart-bg" style="left:{i*7}%; animation-delay:{i*0.5}s; animation-duration:{8+i%3}s;">❤️</div>', unsafe_allow_html=True)
