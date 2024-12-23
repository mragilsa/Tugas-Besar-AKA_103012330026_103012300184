# Tugas-Besar-AKA_103012330026_103012300184

Disusun oleh:
Muhammad Ragil Sahyuda - 103012330026  
Yudistira Ramadhan Senoaji - 103012300184

## Deskripsi

Analisis perbandingan algoritma pangkat (iteratif vs rekursif) ini membandingkan waktu eksekusi atau running time antara algoritma **iteratif** dan **algoritma rekursif dengan optimasi Divide and Conquer**. Fokus utama proyek ini adalah untuk menganalisis kompleksitas waktu eksekusi untuk berbagai ukuran input.

## Deskripsi Algoritma

- **Algoritma Iteratif**: Menggunakan perulangan untuk menghitung hasil pangkat dengan mengalikan bilangan x secara berulang.
- **Algoritma Rekursif (Optimasi Divide and Conquer)**: Menggunakan pembagian masalah menjadi sub-masalah lebih kecil untuk efisiensi perhitungan, dengan memanfaatkan sifat matematika X^n = X^(n/2) * X^(n/2) untuk pangkat genap.

Eksperimen dilakukan dengan beberapa ukuran input dan waktu eksekusi dari kedua algoritma dicatat untuk dianalisis lebih lanjut.

## Fitur

- Perbandingan waktu eksekusi antara algoritma iteratif dan rekursif.
- Visualisasi grafik yang menunjukkan perbedaan waktu eksekusi dalam skala logaritma.
- Penggunaan bahasa Python dan pustaka Matplotlib untuk visualisasi.

## Struktur Proyek

- `power_iterative.py`: Implementasi algoritma iteratif.
- `power_recursive_optimized.py`: Implementasi algoritma rekursif dengan optimasi Divide and Conquer.
- `pangkat.py`: Skrip untuk menghasilkan grafik perbandingan.

## Cara Penggunaan

1. Clone repositori ini ke komputer Anda:
   ```bash
   git clone https://github.com/mragilsa/Tugas-Besar-AKA_103012330026_103012300184.git
2. Instal dependensi yang diperlukan:
   ```bash
   pip install matplotlib
3. Jalankan skrip untuk melihat hasil eksperimen dan grafik:
   ```bash
   python3 pangkat.py
