import time
import matplotlib.pyplot as plt

# Fungsi iteratif untuk menghitung pangkat
def power_iterative(x, n):
    result = 1
    for _ in range(n):
        result *= x
    return result

# Fungsi rekursif menggunakan Divide and Conquer
def power_recursive_optimized(x, n):
    if n == 0:
        return 1
    if n % 2 == 0:  # Jika pangkat genap
        half = power_recursive_optimized(x, n // 2)
        return half * half
    else:  # Jika pangkat ganjil
        return x * power_recursive_optimized(x, n - 1)

# Input ukuran untuk eksperimen
input_sizes = [1, 10, 100, 1000, 10000]
iterative_times = []
recursive_times = []

# Mengukur waktu eksekusi untuk setiap input size
for n in input_sizes:
    # Mengukur waktu untuk fungsi iteratif
    start_time = time.time()
    power_iterative(2, n)
    iterative_times.append((time.time() - start_time) * 1e9)  # Konversi ke nanosecond

    # Mengukur waktu untuk fungsi rekursif (Divide and Conquer)
    start_time = time.time()
    power_recursive_optimized(2, n)
    recursive_times.append((time.time() - start_time) * 1e9)  # Konversi ke nanosecond

# Menampilkan hasil waktu eksekusi
print(f"Input Sizes: {input_sizes}")
print(f"Iterative Times (nanoseconds): {iterative_times}")
print(f"Recursive Times (nanoseconds): {recursive_times}")

# Membuat grafik perbandingan waktu
plt.plot(input_sizes, iterative_times, label='Iterative', marker='o')
plt.plot(input_sizes, recursive_times, label='Recursive (Optimized)', marker='o')
plt.xscale('log')  # Sumbu x dalam skala log
plt.yscale('log')  # Sumbu y dalam skala log
plt.xlabel('Input Size (n)')
plt.ylabel('Running Time (nanoseconds)')
plt.title('Comparison of Iterative and Optimized Recursive Power Functions')
plt.legend()
plt.grid(True)
plt.show()