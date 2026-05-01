import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Kino Analitikası | Premium Dashboard", layout="wide", initial_sidebar_state="collapsed")

# Sessiya yoxlanışı (Səhifələr arası keçid üçün)
if 'page' not in st.session_state:
    st.session_state.page = "landing"

def go_to_dashboard():
    st.session_state.page = "dashboard"

# Xüsusi CSS - Landing səhifəsi üçün daha "Roadmap" uyğunlaşdırılmış dizayn
st.markdown("""
<style>
    .main-header { 
        font-size: 2.8rem; 
        background: -webkit-linear-gradient(#f5c518, #e6b91e);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 900; 
        text-align: center; 
        margin-bottom: 5px;
    }
    .hero-title {
        font-size: 3.5rem; 
        color: #ffffff;
        font-weight: 900; 
        text-align: center;
        margin-top: 20px;
        text-shadow: 2px 2px 4px #000000;
    }
    .hero-subtitle {
        font-size: 1.4rem; 
        color: #f5c518; 
        text-align: center; 
        margin-bottom: 30px;
        font-weight: 600;
    }
    .landing-card {
        background-color: #1e1e1e;
        padding: 30px;
        border-radius: 15px;
        border-left: 6px solid #f5c518;
        box-shadow: 0 10px 25px rgba(0,0,0,0.5);
        margin-bottom: 20px;
    }
    .roadmap-number {
        font-size: 2.5rem;
        font-weight: bold;
        color: #333333;
        float: right;
        margin-top: -20px;
    }
    .stButton>button {
        width: 100%;
        background-color: #f5c518;
        color: black;
        font-weight: bold;
        font-size: 1.3rem;
        padding: 15px;
        border-radius: 50px;
        border: none;
        transition: 0.3s;
        box-shadow: 0 5px 15px rgba(245, 197, 24, 0.4);
    }
    .stButton>button:hover {
        background-color: #e6b91e;
        transform: scale(1.03);
    }
    .footer {
        text-align: center;
        margin-top: 50px;
        padding: 20px;
        color: #666;
        border-top: 1px solid #333;
    }
    .uni-info {
        text-align: center;
        color: #cccccc;
        font-size: 1.1rem;
        margin-bottom: 40px;
    }
</style>
""", unsafe_allow_html=True)

# ---------------- LANDING PAGE (YOL XƏRİTƏSİ ƏSASLI) ----------------
if st.session_state.page == "landing":
    
    # 1. Titul hissəsi
    st.markdown('<div class="hero-title">KİNO İNDUSTRİYASININ ANALİZİ</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-subtitle">Büdcə və IMDb Balı Arasındakı Asılılıq</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="uni-info">
        <b>Bakı Mühəndislik Universiteti</b><br>
        Fakültə: İqtisadiyyat və İdarəetmə | Kafedra: Biznesin İdarə Edilməsi<br>
        Tələbələr: <b>Nəcəfi Tunar</b> və <b>Mayılova Ləman</b>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1.2])
    
    with col1:
        st.image("https://images.unsplash.com/photo-1489599849927-2ee91cede3ba?auto=format&fit=crop&w=800&q=80", use_container_width=True)
        st.markdown("<br>", unsafe_allow_html=True)
        st.button("🚀 PANELE KECID (GET STARTED)", on_click=go_to_dashboard)
        
    with col2:
        # 3. Problemin Təhlili
        st.markdown("""
        <div class="landing-card">
            <span class="roadmap-number">01</span>
            <h3 style='color: white; margin-top:0;'>Problemin Təhlili</h3>
            <p style='color: #cccccc;'><b>Tədqiqat Obyekti:</b> Qlobal kino bazarındakı 4800+ filmin maliyyə və reytinq məlumatları.<br>
            <b>Biznes Tərəfdaşlar:</b> Kino studiyaları, prodüserlər və Netflix/HBO kimi striminq platformaları.<br>
            <b>Problem:</b> Yüksək büdcənin avtomatik olaraq yüksək keyfiyyət və tamaşaçı rəğbəti (IMDb balı) gətirib-gətirmədiyini analiz etmək.</p>
        </div>
        """, unsafe_allow_html=True)
        
        # 4. İstifadə olunacaq Data
        st.markdown("""
        <div class="landing-card">
            <span class="roadmap-number">02</span>
            <h3 style='color: white; margin-top:0;'>İstifadə Olunan Verilənlər (Data)</h3>
            <p style='color: #cccccc;'><b>Mənbə:</b> <a href='https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata' target='_blank' style='color:#f5c518;'>Kaggle - TMDB Movie Metadata</a><br>
            <b>Quruluş:</b> Sistem məlumatları lokal (offline) və ya birbaşa Kaggle API-dən real-time çəkərək işləmək qabiliyyətinə malikdir. Məlumatlar sıfır büdcəli səhvlərdən təmizlənmişdir.</p>
        </div>
        """, unsafe_allow_html=True)
        
        # 6. Digər Modellərin Analizi
        st.markdown("""
        <div class="landing-card">
            <span class="roadmap-number">03</span>
            <h3 style='color: white; margin-top:0;'>Digər Analiz Modelləri</h3>
            <p style='color: #cccccc;'>Gələcəkdə yalnız Pearson korrelyasiyası deyil, həmçinin aşağıdakı modellər tətbiq oluna bilər:<br>
            • <b>Multiple Linear Regression:</b> Büdcə ilə yanaşı, aktyor populyarlığı və janrın bala təsirini ölçmək.<br>
            • <b>Sentiment Analysis (NLP):</b> Twitter və Reddit-dəki izləyici rəylərinin (müsbət/mənfi) IMDb balına təsirini tapmaq.</p>
        </div>
        """, unsafe_allow_html=True)


# ---------------- MAIN DASHBOARD (ƏSAS PANEL) ----------------
elif st.session_state.page == "dashboard":
    
    @st.cache_data
    def load_data():
        df = pd.read_csv("tmdb_5000_movies.csv")
        df['release_year'] = pd.to_datetime(df['release_date'], errors='coerce').dt.year
        df = df.dropna(subset=['release_year'])
        df['release_year'] = df['release_year'].astype(int)
        df = df[df['budget'] > 1000000]
        df = df[['title', 'budget', 'vote_average', 'release_year']]
        return df

    try:
        df = load_data()
    except Exception as e:
        st.error("Data yüklənərkən xəta baş verdi.")
        st.stop()

    with st.sidebar:
        st.markdown("<div style='text-align: center;'><img src='https://upload.wikimedia.org/wikipedia/commons/6/69/IMDB_Logo_2016.svg' width='120' style='margin-bottom: 20px;'></div>", unsafe_allow_html=True)
        st.markdown('### ⚙️ Analitika Filtrləri')
        st.markdown("---")
        
        min_year = int(df['release_year'].min())
        max_year = int(df['release_year'].max())
        selected_years = st.slider("📅 Çıxış İlləri:", min_value=min_year, max_value=max_year, value=(2000, max_year))
        
        min_budget = float(df['budget'].min() / 1_000_000)
        max_budget = float(df['budget'].max() / 1_000_000)
        selected_budget = st.slider("💰 Büdcə (Milyon $):", min_value=min_budget, max_value=max_budget, value=(min_budget, max_budget))
        
        min_vote = float(df['vote_average'].min())
        max_vote = float(df['vote_average'].max())
        selected_vote = st.slider("⭐ Min. IMDb Balı:", min_value=min_vote, max_value=max_vote, value=min_vote)
        
        st.markdown("<br><br>", unsafe_allow_html=True)
        if st.button("⬅️ Ana Səhifəyə Qayıt"):
            st.session_state.page = "landing"
            st.rerun()

    filtered_df = df[
        (df['release_year'] >= selected_years[0]) & 
        (df['release_year'] <= selected_years[1]) &
        (df['budget'] >= selected_budget[0] * 1_000_000) &
        (df['budget'] <= selected_budget[1] * 1_000_000) &
        (df['vote_average'] >= selected_vote)
    ]

    st.markdown('<div class="main-header">🎬 Kino Sənayesi: Analitika Paneli</div>', unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("📽️ Film Sayı", f"{len(filtered_df):,}")
    with col2:
        st.metric("⭐ Orta Bal", f"{filtered_df['vote_average'].mean():.1f}")
    with col3:
        st.metric("💸 Orta Büdcə", f"${filtered_df['budget'].mean() / 1_000_000:.1f}M")
    with col4:
        st.metric("🚀 Max Büdcə", f"${filtered_df['budget'].max() / 1_000_000:.1f}M")

    st.markdown("<br>", unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(["🔴 INTERAKTİV SCATTER PLOT", "📉 YEKUN NƏTİCƏ", "📋 CƏDVƏL"])

    with tab1:
        if not filtered_df.empty:
            fig1 = px.scatter(
                filtered_df, x='budget', y='vote_average', hover_name='title',
                color='vote_average', color_continuous_scale=px.colors.sequential.Agsunset,
                size_max=10, opacity=0.8,
                labels={'budget': 'Büdcə', 'vote_average': 'IMDb Balı'},
                hover_data={'budget': ':,.0f', 'vote_average': ':.1f'}
            )
            fig1.update_layout(height=450, margin=dict(l=0, r=0, t=0, b=0), paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
            st.plotly_chart(fig1, use_container_width=True)
            
            correlation = filtered_df['budget'].corr(filtered_df['vote_average'])
            st.info(f"💡 **Pearson Korrelyasiyası:** {correlation:.4f}")

    with tab2:
        st.markdown("### 🎯 Sərbəst İşin Yekun Nəticəsi")
        st.markdown("""
        <div style='background-color: #1e1e1e; padding: 25px; border-radius: 10px; border-left: 5px solid #28a745;'>
            <p style='font-size: 1.2rem; color: #e0e0e0; line-height: 1.6;'>
            Analiz və <b>Pearson korrelyasiya əmsalı</b> göstərdi ki, büdcə ilə IMDb balı arasında <b>çox zəif asılılıq</b> mövcuddur.<br><br>
            Qrafikdən də aydın şəkildə görünür ki, bəzi çox kiçik büdcəli filmlər yüksək reytinq ala bildiyi halda, milyonlarla dollar xərclənmiş blokbasterlər izləyicilər tərəfindən çox pis qiymətləndirilə bilir.<br><br>
            <b>Yekun:</b> Kino sənayesində maliyyə yatırımı (büdcə) filmin keyfiyyətinə və tamaşaçı rəğbətinə (IMDb balı) heç bir halda birbaşa zəmanət vermir.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with tab3:
        st.dataframe(filtered_df[['title', 'budget', 'vote_average', 'release_year']].sort_values(by='vote_average', ascending=False), use_container_width=True, height=400)

    st.markdown('<div class="footer">© 2026 BMU | Tədqiqatçılar: <b>Nəcəfi Tunar</b> və <b>Mayılova Ləman</b></div>', unsafe_allow_html=True)
