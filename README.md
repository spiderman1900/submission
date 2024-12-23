# Dashboard Penyewaan Sepeda
Proyek ini bertujuan untuk membuat dashboard analisis data penyewaan sepeda. Dashboard ini dibangun menggunakan **Streamlit** untuk memberikan insight mengenai pola penggunaan sepeda berdasarkan musim, hari kerja/non-hari kerja, serta pengaruh faktor lingkungan seperti suhu udara, cuaca, kecepatan angin dan kelembaban.

## Struktur Direktori
submission
├───dashboard
│   ├───main_data.csv
│   └───dashboard.py
├───data
│   ├───day.csv
│   └───hour.csv
│   └───Readme.txt
├───notebook.ipynb
├───README.md
├───requirements.txt
└───url.txt


## Prasyarat (Dependencies)
Software atau library yang dibutuhkan :
- Python 3.8 atau lebih baru
- Virtual environment (opsional)
- Library Python:
    - pandas
    - numpy
    - matplotlib
    - seaborn
    - streamlit


## Cara Menjalankan

1. **Clone atau unduh repository ini** ke komputer Anda.
2. **Masuk ke folder proyek:**
   ```bash
   cd submission/dashboard
   ```
3. **Aktifkan virtual environment (opsional):**
   ```bash
   .\env\Scripts\activate  # untuk Windows
   ```
4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
5. **Jalankan Streamlit:**
   ```bash
   streamlit run dashboard.py
   ```
6. **Akses dashboard di browser Anda:** https://submissiongit-gn3iz4fuegfqb3myeeyhvr.streamlit.app/
   


## Fitur Dashboard

- **Pola Penyewaan Berdasarkan Bulan**
  Visualisasi jumlah penyewaan sepeda per bulan.
- **Penyewaan Berdasarkan Hari Kerja dan Hari Libur**
  Analisis penyewaan sepeda pada hari kerja vs hari libur.
- **Faktor Lingkungan**
  Grafik untuk memahami faktor yang mempengaruhi jumlah penyewaan.


## Sumber Data

Dataset yang digunakan adalah **day.csv** (disesuaikan menjadi main.csv) yang berisi data penyewaan sepeda per hari, termasuk informasi musim, suhu, kelembapan, dan faktor lingkungan lainnya.

