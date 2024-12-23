# Import library
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Load dataset
@st.cache_data
def load_data():
    data = pd.read_csv('main_data.csv')
    data['season'] = data['season'].replace({1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'})
    data['workingday'] = data['workingday'].replace({0: 'Non-Working Day', 1: 'Working Day'})
    data['weekday'] = pd.Categorical(data['weekday'], categories=[0, 1, 2, 3, 4, 5, 6], ordered=True)
    return data

data = load_data()

# Title
st.title("Dashboard Penyewaan Sepeda")
st.header("Visualisasi Penyewaan Sepeda")

# Sidebar Filter
st.sidebar.title("Filter Data")
selected_season = st.sidebar.multiselect("Pilih Musim", data['season'].unique(), default=data['season'].unique())
filtered_data = data[data['season'].isin(selected_season)]

# Visualisasi 1: Tren Penyewaan Sepeda per Bulan
st.subheader("Tren Penyewaan Sepeda per Bulan")
monthly_rentals = filtered_data.groupby('mnth')['cnt'].sum()

# Mendefinisikan musim untuk setiap bulan
season_ranges = {
    'Winter': [12, 1, 2],
    'Spring': [3, 4, 5],
    'Summer': [6, 7, 8],
    'Fall': [9, 10, 11]
}

# Membuat label musim dengan rentang bulan
season_labels = [""] * 12
for season, months in season_ranges.items():
    for month in months:
        index = month - 1 if month != 12 else 11  # Adjust for December as the last index
        # Set label hanya jika bulan pertama musim
        if month == months[0]:
            season_labels[index] = f"{season}"

fig, ax = plt.subplots(figsize=(10, 6))
monthly_rentals.plot(kind='line', title='Jumlah Sepeda Sewa per Bulan', ax=ax, marker='o')

# Menambahkan label musim di bawah sumbu x
ax.set_xticks(range(1, 13))
ax.set_xticklabels([
    f"{month}\n{season}" if season_labels[month - 1] else f"{month}" 
    for month, season in zip(range(1, 13), season_labels)
])

ax.set_xlabel('Bulan')
ax.set_ylabel('Jumlah Sewa')
ax.grid(True)
st.pyplot(fig)

# Visualisasi 2: Penyewaan Berdasarkan Hari Kerja/Libur
st.subheader("Penyewaan Berdasarkan Hari Kerja/Libur")
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(x='workingday', y='cnt', data=filtered_data, ax=ax)
ax.set_title('Penyewaan Berdasarkan Hari Kerja/Libur')
ax.set_xlabel('Hari Kerja/Libur')
ax.set_ylabel('Jumlah Penyewaan')
st.pyplot(fig)

# Visualisasi 3: Tren Penyewa Berdasarkan Hari dalam Seminggu
st.subheader("Tren Penyewa Berdasarkan Hari dalam Seminggu")
fig, ax = plt.subplots(figsize=(12, 6))
sns.lineplot(x="weekday", y="casual", data=filtered_data, label="Casual", marker="o", ax=ax)
sns.lineplot(x="weekday", y="registered", data=filtered_data, label="Registered", marker="o", ax=ax)
ax.set_title("Tren Penyewa Berdasarkan Hari dalam Seminggu")
ax.set_xlabel("Hari dalam Seminggu (0 = Minggu, 6 = Sabtu)")
ax.set_ylabel("Jumlah Penyewa")
ax.legend()
st.pyplot(fig)

# Pertanyaan 2: Faktor Lingkungan yang Mempengaruhi Penyewaan
st.header("Faktor Lingkungan yang Mempengaruhi Penyewaan Sepeda")
correlation = filtered_data[['temp', 'atemp', 'hum', 'windspeed', 'weathersit', 'cnt']].corr()
fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt='.2f', ax=ax)
ax.set_title('Korelasi antara Faktor Lingkungan dan Penyewaan Sepeda')
st.pyplot(fig)

# Kesimpulan
st.header("Kesimpulan")
st.write("""
1. Pola penggunaan sepeda terlihat berbeda antara musim panas dan dingin, dimana penyewa lebih senang bersepeda di saat musim panas seperti pada spring, summer, dan fall daripada di saat musim dingin (winter).  Sedangkan antara hari kerja dan hari libur, secara keseluruhan tidak ada perbedaan. Meski demikian, sebagai catatan, ada perbedaan perilaku antara penyewa casual dengan registered, dimana penyewa casual lebih banyak menyewa di saat hari libur karena tujuan penggunaannya untuk rekreasi, sebaliknya penyewa registered di hari kerja karena tujuannya sebagai alat transportasi ke tempat kerja atau sekolah.
2. Diantara berbagai faktor lingkungan yang diamati, hanya suhu udara (`temp` atau `atemp`) yang memiliki korelasi yang paling kuat terhadap jumlah penyewaan sepeda (`cnt`), dimana semakin meningkat suhu udara maka jumlah penyewaan sepeda akan semakin meningkat pula. Faktor cuaca (`weathersit`) juga menyatakan hal serupa dimana semakin cuacanya dingin seperti hujan atau salju maka penyewaan sepeda akan menurun. Sedangkan untuk faktor kelembaban (`hum`) dan kecepatan angin (`windspeed`) memiliki pengaruh negatif yang lemah atau tidak terlalu berpengaruh terhadap perilaku sewa sepeda.
""")
