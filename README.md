# Proyek Analisis Data: Bike Sharing Dataset 🚲

Selamat datang di proyek analisis data saya! Proyek ini merupakan bagian dari tugas akhir (submission) untuk kursus **"Belajar Analisis Data dengan Python"** di Dicoding. Di sini, saya menganalisis tren penggunaan sepeda berdasarkan faktor waktu, cuaca, dan kondisi harian.

## Identitas
- **Nama:** Muhammad Putra
- **Email:** pashalv74@gmail.com
- **ID Dicoding:** Muhammad Putra

## Struktur Proyek
- `/dashboard`: Berisi file `dashboard.py` dan dataset yang digunakan untuk menjalankan dashboard Streamlit.
- `Bike_Sharing_Analysis.ipynb`: Notebook utama tempat saya melakukan Data Wrangling, EDA, hingga Visualisasi Data.
- `requirements.txt`: Daftar library Python yang dibutuhkan untuk menjalankan proyek ini.
- `day.csv`: Dataset utama yang digunakan dalam analisis.

## Pertanyaan Bisnis
1. Bagaimana tren pertumbuhan penyewaan sepeda di tahun 2012?
2. Bagaimana pengaruh kondisi cuaca dan status hari kerja terhadap perilaku jumlah penyewaan sepeda?
3. Bagaimana karakteristik penyewaan berdasarkan kategori suhu melalui teknik manual clustering?

## Kesimpulan Singkat
- **Tren 2012:** Terdapat kenaikan signifikan dari awal tahun dengan puncak penyewaan pada bulan September.
- **Pengaruh Cuaca:** Cuaca cerah mendominasi total penyewaan, terutama pada hari kerja (working day) yang menunjukkan sepeda digunakan untuk mobilitas harian.
- **Manual Clustering:** Penyewa lebih aktif pada kategori suhu "Warm" (Hangat) dan "Hot" (Panas), sementara pada suhu dingin terjadi penurunan drastis.

## Cara Menjalankan Dashboard

### 1. Instalasi Library
Pastikan Anda memiliki Python terinstal, lalu jalankan perintah berikut untuk menginstal library yang dibutuhkan:
```bash
pip install pandas matplotlib seaborn streamlit