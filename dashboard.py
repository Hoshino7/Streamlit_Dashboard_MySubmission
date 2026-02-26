import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Konfigurasi gaya visualisasi
sns.set(style='whitegrid')


# Load dataset
def load_data():
    df = pd.read_csv("day.csv")
    df['dteday'] = pd.to_datetime(df['dteday'])
    # Mapping cuaca agar sinkron dengan notebook
    df['weathersit'] = df['weathersit'].map({
        1: 'Clear',
        2: 'Misty/Cloudy',
        3: 'Light Rain/Snow',
        4: 'Heavy Rain/Fog'
    })
    return df


day_df = load_data()

# Header Dashboard
st.header('Bike Sharing Analytics Dashboard 🚲')

# Sidebar untuk Filter
with st.sidebar:
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png")  # Bisa ganti dengan logo lokal kamu

    # Filter Rentang Waktu
    start_date, end_date = st.date_input(
        label='Rentang Waktu',
        min_value=day_df["dteday"].min(),
        max_value=day_df["dteday"].max(),
        value=[day_df["dteday"].min(), day_df["dteday"].max()]
    )

# Filter data berdasarkan input sidebar
main_df = day_df[(day_df["dteday"] >= str(start_date)) &
                 (day_df["dteday"] <= str(end_date))]

# Visualisasi 1: Tren Pertumbuhan 2012
st.subheader('Tren Pertumbuhan Penyewaan Sepeda (2012)')
df_2012 = main_df[main_df['dteday'].dt.year == 2012]
monthly_df = df_2012.resample(rule='M', on='dteday').agg({"cnt": "sum"})
monthly_df.index = monthly_df.index.strftime('%B')
monthly_df = monthly_df.reset_index()

fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(monthly_df['dteday'], monthly_df['cnt'], marker='o', linewidth=3, color='#2E86C1')
ax.set_title("Total Penyewaan per Bulan di Tahun 2012", fontsize=15)
plt.xticks(rotation=45)
st.pyplot(fig)

# Visualisasi 2: Pengaruh Cuaca (Bar Chart)
st.subheader('Rata-rata Penyewaan Berdasarkan Kondisi Cuaca')
weather_df = main_df.groupby('weathersit')['cnt'].mean().reset_index()

fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='weathersit', y='cnt', data=weather_df, palette='viridis', ax=ax)
ax.set_xlabel('Kondisi Cuaca')
ax.set_ylabel('Rata-rata Penyewa')
st.pyplot(fig)

st.caption('Copyright © Muhammad Putra 2026')