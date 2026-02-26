import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Set gaya visualisasi
sns.set(style='dark')

# Helper function untuk menyiapkan berbagai dataframe yang dibutuhkan
def create_monthly_rent_df(df):
    monthly_rent_df = df.resample(rule='M', on='dteday').agg({
        "cnt": "sum"
    })
    monthly_rent_df.index = monthly_rent_df.index.strftime('%B %Y')
    monthly_rent_df = monthly_rent_df.reset_index()
    return monthly_rent_df

def create_weather_rent_df(df):
    weather_rent_df = df.groupby("weathersit").cnt.mean().reset_index()
    return weather_rent_df

# 1. Load data
day_df = pd.read_csv("day.csv")
day_df['dteday'] = pd.to_datetime(day_df['dteday'])

# Mapping label cuaca agar lebih cantik di dashboard
weather_labels = {1: 'Clear', 2: 'Misty/Cloudy', 3: 'Light Snow/Rain', 4: 'Severe Weather'}
day_df['weathersit_label'] = day_df['weathersit'].map(weather_labels)

# 2. Membuat Komponen Sidebar
with st.sidebar:
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png") # Opsional: ganti logo
    
    # Mengambil rentang waktu
    min_date = day_df["dteday"].min()
    max_date = day_df["dteday"].max()
    
    start_date, end_date = st.date_input(
        label='Rentang Waktu',
        min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

# Filter data berdasarkan pilihan tanggal
main_df = day_df[(day_df["dteday"] >= str(start_date)) & 
                (day_df["dteday"] <= str(end_date))]

# Menyiapkan dataframe untuk visualisasi
monthly_rent_df = create_monthly_rent_df(main_df)
weather_rent_df = create_weather_rent_df(main_df)

# 3. Melengkapi Dashboard dengan Visualisasi
st.header('Bike Sharing Dashboard 🚲')

# Menampilkan metrik utama
col1, col2 = st.columns(2)
with col1:
    total_rentals = main_df.cnt.sum()
    st.metric("Total Penyewaan", value=f"{total_rentals:,}")
with col2:
    avg_rentals = round(main_df.cnt.mean(), 2)
    st.metric("Rata-rata Harian", value=f"{avg_rentals:,}")

# Visualisasi 1: Tren Penyewaan
st.subheader('Tren Penyewaan Sepeda')
fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(
    monthly_rent_df["dteday"],
    monthly_rent_df["cnt"],
    marker='o', 
    linewidth=2,
    color="#90CAF9"
)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15, rotation=45)
st.pyplot(fig)

# Visualisasi 2: Performa berdasarkan Cuaca
st.subheader('Rata-rata Penyewaan Berdasarkan Kondisi Cuaca')
fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(
    x="weathersit_label", 
    y="cnt", 
    data=main_df, # menggunakan data asli yang sudah difilter
    palette="viridis",
    ax=ax
)
ax.set_xlabel(None)
ax.set_ylabel(None)
ax.tick_params(axis='x', labelsize=12)
st.pyplot(fig)

st.caption('Copyright (c) Muhammad Putra 2026')