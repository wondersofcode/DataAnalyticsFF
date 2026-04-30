import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="Kino Analitikası | Premium Dashboard", layout="wide", initial_sidebar_state="expanded")

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
    .sub-header { 
        font-size: 1.1rem; 
        color: #aaaaaa; 
        text-align: center; 
        margin-bottom: 30px; 
    }
    [data-testid="stSidebar"] {
        background-color: #121212;
    }
    .sidebar-title {
        color: #f5c518;
        font-size: 1.3rem;
        font-weight: bold;
        margin-bottom: 20px;
        text-align: center;
    }
    .footer {
        text-align: center;
        margin-top: 50px;
        padding: 20px;
        color: #666;
        border-top: 1px solid #333;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header">🎬 Kino Sənayesi: Verilənlərin Təhlili Paneli</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Büdcə və IMDb reytinqləri arasındakı asılılığın real-time interaktiv vizuallaşdırılması</div>', unsafe_allow_html=True)

# İndi birbaşa orijinal və gerçək faylı oxuyuruq
@st.cache_data
def load_data():
    df = pd.read_csv("tmdb_5000_movies.csv")
    df['release_year'] = pd.to_datetime(df['release_date'], errors='coerce').dt.year
    df = df.dropna(subset=['release_year'])
    df['release_year'] = df['release_year'].astype(int)
    # Təmizləmələr
    df = df[df['budget'] > 1000000]
    df = df[['title', 'budget', 'vote_average', 'release_year']]
    return df

try:
    df = load_data()
except Exception as e:
    st.error("Data yüklənərkən xəta baş verdi. Zəhmət olmasa internet bağlantısını yoxlayın.")
    st.stop()

# --- YAN PANEL (SIDEBAR) ---
with st.sidebar:
    st.markdown(
        """
        <div style="text-align: center;">
            <img src="https://upload.wikimedia.org/wikipedia/commons/6/69/IMDB_Logo_2016.svg" width="120" style="margin-bottom: 20px;">
        </div>
        """, 
        unsafe_allow_html=True
    )
    
    st.markdown('<div class="sidebar-title">⚙️ Analitika Filtrləri</div>', unsafe_allow_html=True)
    st.markdown("---")
    
    min_year = int(df['release_year'].min())
    max_year = int(df['release_year'].max())
    selected_years = st.slider("📅 Çıxış İlləri Aralığı:", min_value=min_year, max_value=max_year, value=(2000, max_year))
    
    min_budget = float(df['budget'].min() / 1_000_000)
    max_budget = float(df['budget'].max() / 1_000_000)
    selected_budget = st.slider("💰 Büdcə (Milyon Dolar):", min_value=min_budget, max_value=max_budget, value=(min_budget, max_budget))
    
    min_vote = float(df['vote_average'].min())
    max_vote = float(df['vote_average'].max())
    selected_vote = st.slider("⭐ Minimum IMDb Balı:", min_value=min_vote, max_value=max_vote, value=min_vote)
    
    st.markdown("---")
    st.markdown("""
    <div style='background-color: #1e1e1e; padding: 15px; border-radius: 10px; border-left: 4px solid #f5c518;'>
        <h4 style='color: #ffffff; margin-top: 0;'>👨‍💻 Layihə Tədqiqatçıları</h4>
        <ul style='color: #cccccc; padding-left: 20px;'>
            <li><b>Tunar Eyyublu</b></li>
            <li><b>Mayılova Ləman</b></li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

filtered_df = df[
    (df['release_year'] >= selected_years[0]) & 
    (df['release_year'] <= selected_years[1]) &
    (df['budget'] >= selected_budget[0] * 1_000_000) &
    (df['budget'] <= selected_budget[1] * 1_000_000) &
    (df['vote_average'] >= selected_vote)
]

# --- ÜMUMİ STATİSTİKA ---
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric(label="📽️ Cəmi Film Sayı", value=f"{len(filtered_df):,}")
with col2:
    st.metric(label="⭐ Orta IMDb Balı", value=f"{filtered_df['vote_average'].mean():.1f}")
with col3:
    st.metric(label="💸 Orta Büdcə", value=f"${filtered_df['budget'].mean() / 1_000_000:.1f}M")
with col4:
    st.metric(label="🚀 Maksimum Büdcə", value=f"${filtered_df['budget'].max() / 1_000_000:.1f}M")

st.markdown("<br>", unsafe_allow_html=True)

# --- QRAFİKLƏR ---
tab1, tab2, tab3 = st.tabs(["🔴 İNTERAKTİV SCATTER PLOT", "📈 İLLƏR ÜZRƏ TREND", "📋 DATA CƏDVƏLİ"])

with tab1:
    st.markdown("### 🎯 Büdcə və IMDb Balı Arasındakı Asılılıq")
    
    if not filtered_df.empty:
        fig1 = px.scatter(
            filtered_df, 
            x='budget', 
            y='vote_average', 
            hover_name='title',
            color='vote_average',
            color_continuous_scale=px.colors.sequential.Agsunset,
            size_max=10,
            opacity=0.8,
            labels={'budget': 'Büdcə (USD)', 'vote_average': 'IMDb Balı'},
            hover_data={'budget': ':,.0f', 'vote_average': ':.1f'}
        )
        fig1.update_layout(height=500, margin=dict(l=0, r=0, t=0, b=0), paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig1, use_container_width=True)
        
        correlation = filtered_df['budget'].corr(filtered_df['vote_average'])
        if pd.notna(correlation):
            st.info(f"💡 **Analitik Nəticə:** Büdcə və Bal arasındakı Pearson Korrelyasiya Əmsalı: **{correlation:.4f}**. Nəticə etibarilə maliyyə yatırımı filmin reytinqinə birbaşa və güclü təsir göstərmir.")
    else:
        st.warning("Bu filtrlərə uyğun film tapılmadı.")

with tab2:
    st.markdown("### 📈 Zamanla IMDb Reytinqinin Dəyişməsi")
    if not filtered_df.empty:
        yearly_data = filtered_df.groupby('release_year')['vote_average'].mean().reset_index()
        fig2 = px.line(
            yearly_data, 
            x='release_year', 
            y='vote_average', 
            markers=True,
            line_shape='spline',
            color_discrete_sequence=['#f5c518'],
            labels={'release_year': 'Çıxış İli', 'vote_average': 'Orta IMDb Balı'}
        )
        fig2.update_layout(height=400, margin=dict(l=0, r=0, t=0, b=0), paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig2, use_container_width=True)
    else:
        st.warning("Bu filtrlərə uyğun film tapılmadı.")

with tab3:
    st.markdown("### 🗃️ Detallı Verilənlər Bazası (Dataset)")
    st.dataframe(
        filtered_df[['title', 'budget', 'vote_average', 'release_year']].sort_values(by='vote_average', ascending=False), 
        use_container_width=True, 
        height=400
    )

st.markdown('<div class="footer">© 2026 Data Analitika Laboratoriyası | Tədqiqatçı Analitiklər: <b>Tunar Eyyublu</b> və <b>Mayılova Ləman</b></div>', unsafe_allow_html=True)
