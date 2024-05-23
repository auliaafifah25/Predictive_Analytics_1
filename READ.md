# Laporan Proyek Machine Learning - Aulia Afifah

## Domain Proyek

Pasar saham adalah salah satu indikator utama kesehatan ekonomi, di mana harga saham mencerminkan ekspektasi investor terhadap kinerja masa depan suatu perusahaan. Alibaba Group Holding Limited (BABA) adalah salah satu perusahaan teknologi terbesar di dunia dengan kapitalisasi pasar yang besar dan pengaruh signifikan di pasar global. Menganalisis performa saham Alibaba dapat memberikan wawasan penting tentang tren pasar, sentimen investor, dan potensi pergerakan harga di masa depan.

Pada proyek ini akan melakukan predictive analytics terhadap Alibaba stock. Data yang digunakan adalah 1089 ribu.

**Rubrik/Kriteria Tambahan (Opsional)**:

Mengapa dan bagaimana masalah ini harus diselesaikan?

1. Pemahaman investasi: Analisis data saham Alibaba dapat membantu investor dalam membuat keputusan investasi yang lebih cerdas. Dengan memprediksi pergerakan harga saham, investor bisa meminimalkan risiko dan memaksimalkan keuntungan.
2. Strategi perdagangan: Trader dapat menggunakan data historis untuk mengembangkan strategi perdagangan yang lebih efektif, seperti menentukan titik masuk dan keluar yang optimal berdasarkan pola harga masa lalu.
3. Peningkatan model prediksi: Menggunakan teknik analisis prediktif dan machine learning, kita bisa membangun model yang lebih akurat dalam memprediksi harga saham.

Sumber referensi: (Analisis Data Time Series Menggunakan Model Kernel: Pemodelan
Data Harga Saham MDKA)[https://jurnal.uns.ac.id/ijas/article/view/79385/43851], (Implementasi Algoritma Regresi pada Machine Learning untuk Prediksi Indeks Harga Saham Gabungan)[https://ejournal.poltekharber.ac.id/index.php/informatika/article/view/6105/2848]

## Business Understanding

Pada bagian ini, menjelaskan proses klarifikasi masalah.
Bagian laporan ini mencakup:

### Problem Statements

- Bagaimana cara memprediksi harga penutupan (Adj Close) saham Alibaba di masa depan?
  Investor dan trader memerlukan prediksi harga saham untuk membuat keputusan investasi yang lebih baik. Harga penutupan yang disesuaikan mencerminkan nilai riil saham setelah penyesuaian untuk dividen dan split saham, menjadikannya indikator yang penting.
- Apakah faktor-faktor yang paling mempengaruhi harga penutupan saham Alibaba?
  Mengetahui faktor-faktor yang mempengaruhi harga saham dapat membantu investor memahami dinamika pasar dan meningkatkan strategi investasi mereka.
- Bagaimana mengukur kinerja model prediksi harga saham dan memastikan model tersebut akurat dan dapat diandalkan?
  Mengetahui faktor-faktor yang mempengaruhi harga saham dapat membantu investor memahami dinamika pasar dan meningkatkan strategi investasi mereka.

### Goals

- Membangun model prediktif yang dapat memprediksi harga penutupan saham Alibaba dengan akurasi tertinggi: akan membantu investor dan trader dalam membuat keputusan investasi yang lebih tepat dan efektif.
- Mengidentifikasi dan menganalisis faktor-faktor utama yang mempengaruhi harga penutupan saham Alibaba: akan memberikan wawasan yang lebih dalam tentang faktor-faktor yang mempengaruhi harga saham dan bagaimana faktor-faktor tersebut dapat dimanfaatkan dalam strategi investasi.
- Mengembangkan metrik evaluasi untuk mengukur kinerja model prediksi dan melakukan validasi untuk memastikan keandalan model: memastikan bahwa model yang dikembangkan dapat diandalkan dan memberikan prediksi yang akurat.

**Rubrik/Kriteria Tambahan (Opsional)**:

### Solution statements

- Menggunakan beberapa algoritma untuk membangun model prediktif: KNN (K-Nearest Neighbors), Random Forest, dan Boosting.
- Menggunakan hasil evaluasi model: Dari hasil evaluasi, terlihat bahwa model RandomForest memiliki Train MSE yang paling rendah, menunjukkan performa yang baik dalam memprediksi harga penutupan saham Alibaba pada data pelatihan. Namun, performa pada data pengujian (Test MSE) serupa dengan model KNN. Model Boosting memiliki MSE yang lebih tinggi, menunjukkan performa yang kurang baik dibandingkan dua model lainnya.

## Data Understanding

Dataset yang digunakan dalam proyek ini adalah Alibaba (BABA) Stock Dataset yang tersedia di Kaggle. Dataset ini berisi data harga saham historis Alibaba Group Holding (BABA) dari 1 Januari 2020 hingga 1 Mei 2024. Data ini mencakup harga pembukaan, tertinggi, terendah, dan penutupan harian, serta harga penutupan yang disesuaikan dan volume perdagangan.
Sumber data: (Alibaba (BABA) Stock Dataset)[https://www.kaggle.com/datasets/innocentmfa/alibaba-baba-stock-dataset?select=BABA.csv]

### Variabel-variabel pada ulasan aplikasi DANA dataset adalah sebagai berikut:

Variabel-variabel pada Alibaba (BABA) Stock Dataset adalah sebagai berikut:

- Date: Tanggal data dicatat, mencerminkan setiap hari perdagangan.
- Open: Harga pembukaan saham pada hari itu.
- High: Harga tertinggi saham pada hari itu.
- Low: Harga terendah saham pada hari itu.
- Close: Harga penutupan saham pada hari itu.
- Adj Close: Harga penutupan yang disesuaikan (adjusted close), mencerminkan harga riil saham setelah penyesuaian untuk dividen dan split saham.
- Volume: Jumlah saham yang diperdagangkan pada hari itu.

**Rubrik/Kriteria Tambahan (Opsional)**:

- Melakukan beberapa tahapan yang diperlukan untuk memahami data, contohnya teknik visualisasi data dan exploratory data analysis: dapat memahami karakteristik dan distribusi data saham Alibaba, mendeteksi outliers, serta mengeksplorasi hubungan antar variabel. Ini merupakan langkah penting untuk memastikan data siap digunakan dalam model prediktif yang akurat dan andal.

## Data Preparation

Pada bagian ini, teknik data preparation dilakukan seperti Visualisasi Pairplot, Principal Component Analysis (PCA), Membagi Data menjadi Train dan Test Set, dan Standardisasi Fitur Numerik.

**Rubrik/Kriteria Tambahan (Opsional)**:

- Visualisasi Pairplot: Untuk melihat hubungan antara variabel-variabel Open, High, Low, dan Close.
- Principal Component Analysis (PCA): Untuk mereduksi dimensi data dengan menjaga sebanyak mungkin variasi dari dataset asli.
- Membagi Data menjadi Train dan Test Set: Untuk membagi data menjadi set pelatihan dan pengujian.
- Standardisasi Fitur Numerik: Untuk menstandarisasi fitur dimension agar memiliki mean 0 dan standard deviation 1.

## Modeling

Model machine learning yang digunakan untuk memprediksi harga penutupan (Adj Close) saham Alibaba. Tiga algoritma yang digunakan adalah K-Nearest Neighbors (KNN), Random Forest, dan Boosting. Setiap model memiliki kelebihan dan kekurangan masing-masing, serta parameter tertentu yang mempengaruhi kinerjanya.

**Rubrik/Kriteria Tambahan (Opsional)**:

- K-Nearest Neighbors (KNN): algoritma non-parametrik yang menggunakan kedekatan data dalam ruang fitur untuk membuat prediksi. Kelebihan: Mudah dipahami dan diimplementasikan dan Tidak memerlukan asumsi distribusi data. Kekurangan: Kinerja bisa menurun pada dataset yang besar dan Sensitif terhadap skala fitur dan outliers.
- Random Forest: algoritma ensemble learning yang menggunakan banyak pohon keputusan untuk membuat prediksi. Kelebihan: Dapat menangani data dengan fitur yang banyak dan saling berkorelasi dan Memberikan estimasi pentingnya fitur. Kekurangan: Model yang besar bisa lambat untuk prediksi dan Cenderung overfitting jika tidak ada cukup data.
- Boosting (AdaBoost): teknik ensemble yang menggabungkan beberapa model lemah untuk membentuk model kuat. Kelebihan: Meningkatkan akurasi model dengan mengurangi bias dan Efektif pada dataset dengan noise. Kekurangan: Rentan terhadap overfitting jika tidak dikonfigurasi dengan baik dan Membutuhkan lebih banyak waktu untuk training.

## Evaluation

Dalam proyek ini, metrik evaluasi yang digunakan adalah Mean Squared Error (MSE). MSE adalah metrik yang sangat umum digunakan dalam masalah regresi, termasuk prediksi harga saham. MSE menghitung rata-rata dari kuadrat selisih antara nilai yang diprediksi oleh model dan nilai sebenarnya.
Mengapa MSE Digunakan?

- Sensitivitas terhadap Outliers: MSE memperbesar kesalahan besar, sehingga lebih sensitif terhadap outliers dibanding metrik lain seperti Mean Absolute Error (MAE).
- Konsisten: Memberikan hasil yang konsisten dan dapat diandalkan untuk berbagai macam dataset.

**Rubrik/Kriteria Tambahan (Opsional)**:

1. KNN:

   - Train MSE: 0.001799
   - Test MSE: 0.002539
   - Interpretasi: KNN memiliki performa yang baik pada data pelatihan dan pengujian, menunjukkan generalisasi yang baik tanpa overfitting.

2. Random Forest:

   - Train MSE: 0.000402
   - Test MSE: 0.002541
   - Interpretasi: Random Forest memiliki MSE terendah pada data pelatihan, menunjukkan bahwa model ini sangat baik dalam menangkap pola dalam data. Meskipun ada sedikit peningkatan MSE pada data pengujian, performanya tetap konsisten dan baik.

3. Boosting:
   - Train MSE: 0.032853
   - Test MSE: 0.030033
   - Interpretasi: Boosting memiliki MSE yang cukup tinggi baik pada data pelatihan maupun pengujian. Ini menunjukkan bahwa model Boosting mungkin overfitting terhadap data pelatihan atau kurang mampu menangkap pola dengan baik.

**---Ini adalah bagian akhir laporan---**
