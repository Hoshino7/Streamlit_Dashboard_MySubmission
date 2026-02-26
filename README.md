Proyek Analisis Data: Bike Sharing Dataset 
Deskripsi
Proyek ini bertujuan untuk menganalisis tren penyewaan sepeda berdasarkan faktor waktu dan kondisi cuaca menggunakan Bike Sharing Dataset. Analisis ini diwujudkan dalam bentuk dashboard interaktif yang dapat digunakan untuk melihat pola distribusi penyewaan secara harian.

Identitas
Nama: Muhammad Putra

Email: pashalv74@gmail.com

ID Dicoding: Muhammad Putra

Struktur Proyek
dashboard/: Direktori utama aplikasi dashboard.

day.csv: Dataset penyewaan sepeda harian.

requirements.txt: Daftar pustaka (library) yang dibutuhkan.

Bike_Sharing_Analysis.ipynb: File analisis data lengkap.

Cara Menjalankan di Local Laptop
1. Setup Environment - Anaconda
Disarankan menggunakan Anaconda untuk manajemen environment yang lebih rapi:

Bash
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt
2. Setup Environment - Shell/Terminal
Jika Anda menggunakan terminal biasa (Windows PowerShell atau Linux/Mac Terminal):

Bash
# Membuat direktori proyek
mkdir proyek_analisis_data
cd proyek_analisis_data

# Menggunakan pipenv
pipenv install
pipenv shell

# Instalasi library berdasarkan requirements.txt
pip install -r requirements.txt
3. Menjalankan Dashboard Streamlit
Setelah environment aktif dan library terinstal, jalankan perintah berikut:

Bash
streamlit run dashboard.py