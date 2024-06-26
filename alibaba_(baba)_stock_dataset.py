# -*- coding: utf-8 -*-
"""Alibaba (BABA) Stock Dataset.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1UXXDjz33lB5wtDfs9gUeaXkVmN8qGJx_

**Submission Pertama**
- **Nama:** Aulia Afifah
- **Email:** auliaafifah2205@gmail.com
- **ID Dicoding:** auliaafifah253

# Data Loading

import library yang dibutuhkan
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# %matplotlib inline
import seaborn as sns

from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import AdaBoostRegressor

"""Masukkan dataset dan lihat isi dataset 5 baris di awal"""

df = pd.read_csv('BABA.csv')
df.head()

"""# Exploratory Data Analysis

## Exploratory Data Analysis - Deskripsi Variabel

menghapus kolom yang tidak diperlukan dengan fitur drop()
"""

df = df.drop(columns=['Date'])

"""mengecek missing value dengan fitur isna().sum()"""

df.isna().sum()

"""mengecek informasi pada dataset dengan fungsi info()"""

df.info()

"""mengecek deskripsi statistik data dengan fitur describe()"""

df.describe()

"""## Exploratory Data Analysis - Menangani outliers"""

df.shape

"""visualisasikan data df dengan boxplot untuk mendeteksi outliers"""

sns.boxplot(x=df['Open'])

sns.boxplot(x=df['High'])

sns.boxplot(x=df['Low'])

sns.boxplot(x=df['Close'])

sns.boxplot(x=df['Adj Close'])

sns.boxplot(x=df['Volume'])

"""Pada kolom volume terlhat, bahwa terdapat outliers

Mengatasi outliers tersebut dengan metode IQR
"""

q1 = df.quantile(0.25)
q3 = df.quantile(0.75)
iqr = q3-q1

df = df[~((df<(q1-1.5*iqr))|(df>(q3+1.5*iqr))).any(axis=1)]

df.shape

"""Dataset Anda sekarang telah bersih dan memiliki 1.017 sampel

## Explaratory Data Analysis - Univariate Analysis

melihat histogram masing-masing fiturnya
"""

df.hist(bins=50, figsize=(20,15))
plt.show()

"""histogram untuk variabel "Adj Close" yang merupakan fitur target (label) pada data

## Exploratory Data Analysis - Multivariate Analysis

mengamati hubungan antara fitur numerik menggunakan fungsi pairplot()
"""

sns.pairplot(df, diag_kind = 'kde')

"""mengobservasi korelasi antara fitur numerik dengan fitur target menggunakan fungsi corr()"""

plt.figure(figsize=(10, 8))
correlation_matrix = df.corr().round(2)

# Untuk menge-print nilai di dalam kotak, gunakan parameter anot=True
sns.heatmap(data=correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5, )
plt.title("Correlation Matrix untuk Fitur Numerik ", size=20)

""" fitur 'Open', 'High', 'Low', dan 'Close' memiliki skor korelasi yang besar (di atas 0.9) dengan fitur target 'Adj Close'. Artinya, fitur 'Adj Close' berkorelasi tinggi dengan keempat fitur tersebut. Sementara itu, fitur 'Volume' memiliki korelasi yang sangat kecil (-0.21). Sehingga, fitur tersebut dapat di-drop."""

df.drop(['Volume'], inplace=True, axis=1)
df.head()

"""# Data Preparation

cek menggunakan fungsi pairplot, keempat fitur ukuran df dalam 4 kolom tersebut memiliki korelasi yang tinggi. Hal ini karena keempat fitur ini memiliki informasi yang sama, yaitu ukuran df
"""

sns.pairplot(df[['Open', 'High', 'Low', 'Close']], plot_kws={"s": 3});

"""aplikasikan class PCA dari library scikit learn dengan kode berikut."""

pca = PCA(n_components=4, random_state=123)
pca.fit(df[['Open', 'High', 'Low', 'Close']])
princ_comp = pca.transform(df[['Open', 'High', 'Low', 'Close']])

"""mengetahui proporsi informasi dari keempat komponen tadi."""

pca.explained_variance_ratio_.round(4)

"""mambahkan fitur baru ke dataset dengan nama 'dimension' dan melakukan proses transformasi."""

pca = PCA(n_components=1, random_state=123)
pca.fit(df[['Open', 'High', 'Low', 'Close']])
df['dimension'] = pca.transform(df.loc[:, ('Open', 'High', 'Low', 'Close')]).flatten()
df.drop(['Open', 'High', 'Low', 'Close'], axis=1, inplace=True)
df.head()

"""**Train-Test-Split**
menggunakan proporsi pembagian sebesar 90:10 dengan fungsi train_test_split dari sklearn.
"""

X = df.drop(["Adj Close"],axis =1)
y = df["Adj Close"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.1, random_state = 123)

"""mengecek jumlah sampel pada masing-masing bagian"""

print(f'Total # of sample in whole dataset: {len(X)}')
print(f'Total # of sample in train dataset: {len(X_train)}')
print(f'Total # of sample in test dataset: {len(X_test)}')

"""menerapkan fitur standarisasi pada data latih"""

numerical_features = ['dimension']

scaler = StandardScaler()
scaler.fit(X_train[numerical_features])
X_train[numerical_features] = scaler.transform(X_train.loc[:, numerical_features])
X_train[numerical_features].head()

"""mengecek nilai mean dan standar deviasi pada setelah proses standarisasi"""

X_train[numerical_features].describe().round(2)

"""# Model Development"""

# Siapkan dataframe untuk analisis model
models = pd.DataFrame(index=['train_mse', 'test_mse'],
                      columns=['KNN', 'RandomForest', 'Boosting'])

"""## Model Development dengan K-Nearest Neighbor

melatih data dengan KNN dan menggunakan k = 10 tetangga dan metric Euclidean untuk mengukur jarak antara titik.
"""

knn = KNeighborsRegressor(n_neighbors=10)
knn.fit(X_train, y_train)

models.loc['train_mse','knn'] = mean_squared_error(y_pred = knn.predict(X_train), y_true=y_train)

"""## Model Development dengan Random Forest"""

# buat model prediksi random forest
RF = RandomForestRegressor(n_estimators=50, max_depth=16, random_state=55, n_jobs=-1)
RF.fit(X_train, y_train)

models.loc['train_mse','RandomForest'] = mean_squared_error(y_pred=RF.predict(X_train), y_true=y_train)

"""set n_estimator=50, kedalaman=16, dan n_jobs=-1 artinya semua proses berjalan secara paralel

## Model Development dengan Boosting Algorithm
"""

boosting = AdaBoostRegressor(learning_rate=0.05, random_state=55)
boosting.fit(X_train, y_train)
models.loc['train_mse','Boosting'] = mean_squared_error(y_pred=boosting.predict(X_train), y_true=y_train)

"""bobot yang diterapkan pada setiap regressor di masing-masing proses iterasi boosting sebesar 0.05 dan mengontrol random number generator yang digunakan sebesar 55

# Evaluasi Model

melakukan proses scaling terhadap data uji agar skala antara data latih dan data uji sama dan kita bisa melakukan evaluasi
"""

# Lakukan scaling terhadap fitur numerik pada X_test sehingga memiliki rata-rata=0 dan varians=1
X_test.loc[:, numerical_features] = scaler.transform(X_test[numerical_features])

"""evaluasi ketiga model kita dengan metrik MSE"""

# Buat variabel mse yang isinya adalah dataframe nilai mse data train dan test pada masing-masing algoritma
mse = pd.DataFrame(columns=['train', 'test'], index=['KNN','RF','Boosting'])

# Buat dictionary untuk setiap algoritma yang digunakan
model_dict = {'KNN': knn, 'RF': RF, 'Boosting': boosting}

# Hitung Mean Squared Error masing-masing algoritma pada data train dan test
for name, model in model_dict.items():
    mse.loc[name, 'train'] = mean_squared_error(y_true=y_train, y_pred=model.predict(X_train))/1e3
    mse.loc[name, 'test'] = mean_squared_error(y_true=y_test, y_pred=model.predict(X_test))/1e3

# Panggil mse
mse

"""plot metrik tersebut dengan bar chart"""

fig, ax = plt.subplots()
mse.sort_values(by='test', ascending=False).plot(kind='barh', ax=ax, zorder=3)
ax.grid(zorder=0)

"""model KNN dan Random Forest memberikan nilai eror yang paling kecil. Sedangkan model dengan algoritma Boosting memiliki eror yang paling besar (berdasarkan grafik)"""

prediksi = X_test.iloc[:1].copy()
pred_dict = {'y_true':y_test[:1]}
for name, model in model_dict.items():
    pred_dict['prediksi_'+name] = model.predict(prediksi).round(1)

pd.DataFrame(pred_dict)

"""Berdasarkan hasil evaluasi, model Random Forest dipilih sebagai model terbaik karena memiliki MSE terendah pada data pelatihan dan performa yang kompetitif pada data pengujian. Berikut adalah beberapa alasan memilih Random Forest:
* Akurasi: Random Forest memiliki MSE terendah pada data pelatihan, menunjukkan kemampuan belajar yang baik dari data.
* Generalizability: Meskipun MSE pada data pengujian sedikit lebih tinggi dari KNN, perbedaan ini kecil dan menunjukkan bahwa Random Forest memiliki generalizability yang baik.
"""