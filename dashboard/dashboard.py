# Import library
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load dataset and preprocess data
data_clean = pd.read_csv('dashboard/main_data.csv')
data_clean['dteday'] = pd.to_datetime(data_clean['dteday'])
data_clean['season_name'] = data_clean['season'].replace({1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'})

# Title
st.title("Dashboard Penyewaan Sepeda")
st.header("Visualisasi Penyewaan Sepeda")

# Sidebar Filter
st.sidebar.title("Filter Data")
selected_season = st.sidebar.multiselect("Pilih Musim", data_clean['season'].unique(), default=data_clean['season'].unique())
filtered_data = data_clean[data_clean['season'].isin(selected_season)]

# Pertanyaan 1: Pola Penyewaan Sepeda berdasarkan musim dan hari kerja/non kerja

# Visualisasi 1: Penyewaan Berdasarkan Musim
# Kelompokkan data berdasarkan tahun, season_name, dan hitung jumlah cnt
result = data_clean.groupby([data_clean['dteday'].dt.year, 'season_name'])['cnt'].sum().reset_index()
result.columns = ['year', 'season_name', 'total_cnt']

# Membuat diagram batang berdampingan
def plot_sewa_per_musim(data_clean):
    plt.figure(figsize=(10, 6))

# Tentukan lebar setiap batang dan jarak antar kelompok batang
width = 0.35

# Hitung posisi x untuk setiap batang
x = np.arange(len(result['season_name'].unique()))

# Iterasi untuk setiap tahun
for i, year in enumerate(result['year'].unique()):
    plt.bar(x + i*width,
            result[result['year'] == year]['total_cnt'],
            width=width,
            label=str(year))

# Menambahkan judul, label sumbu, dan legend
plt.title('Jumlah Sewa Sepeda per Musim di tahun 2011-2012')
plt.xlabel('Musim')
plt.ylabel('Jumlah Sewa')
plt.xticks(x + width/2, result['season_name'].unique())  # Atur posisi x-ticks
plt.legend()

st.pyplot(plt)

# Panggil fungsi untuk menampilkan grafik
plot_sewa_per_musim(data_clean.copy())

# Visualisasi 2: Penyewaan Berdasarkan Hari Kerja/Libur
# Menghitung rata-rata jumlah penyewaan sepeda berdasarkan workingday
workingday_rentals = data_clean.groupby('workingday')['cnt'].mean().reset_index()

# Plot bar chart
fig, ax = plt.subplots(figsize=(8, 6))  # Buat objek figure dan axis
sns.barplot(x='workingday', y='cnt', data=workingday_rentals, palette='coolwarm', ax=ax)
ax.set_title('Rata-rata Sewa Keseluruhan di Hari Kerja dan Non Kerja', fontsize=14)
ax.set_xlabel('Jenis Hari', fontsize=12)
ax.set_ylabel('Rata-rata Jumlah Penyewaan', fontsize=12)
ax.set_xticklabels(['Non-Kerja', 'Kerja'])

st.pyplot(fig)


# Pertanyaan 2: Faktor Lingkungan yang Mempengaruhi Penyewaan

# Visualisasi : Matriks Korelasi Penyewaan dan Faktor Lingkungan
correlation = data_clean[['cnt', 'hum', 'temp', 'windspeed', 'weathersit']].corr()

fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(correlation, annot=True, cmap='coolwarm', ax=ax)
ax.set_title('Matriks Korelasi Faktor Lingkungan dan Penyewaan Sepeda', fontsize=14)

st.pyplot(plt)

# Kesimpulan
st.header("Kesimpulan")
st.write("""
1. Terindikasi adanya pola penggunaan sepeda berdasarkan musim, dimana penyewaan sepeda mencapai jumlah tertingginya pada musim fall, dan mencapai titik terendahnya pada musim spring, sedangkan pada musim summer dan winter relatif sama besarnya.
2. Tidak ada indikasi adanya pola penggunaan sepeda secara keseluruhan di hari kerja maupun non kerja.
3. Diantara berbagai faktor lingkungan yang diamati, hanya suhu udara (`temp` atau `atemp`) yang memiliki korelasi yang paling kuat terhadap jumlah penyewaan sepeda (`cnt`), dimana semakin meningkat suhu udaranya maka jumlah penyewaan sepeda akan semakin meningkat pula.
""")
