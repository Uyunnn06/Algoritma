'''
peseudocode:

marge sort:
Fungsi MERGE_SORT(Array)
    Jika Array memiliki lebih dari 1 elemen:
        Bagi Array menjadi dua bagian: KIRI dan KANAN
        Panggil MERGE_SORT untuk KIRI
        Panggil MERGE_SORT untuk KANAN
        
        Inisialisasi i, j, k dengan 0
        
        SELAMA ada elemen yang tersisa di KIRI dan KANAN:
            Jika KIRI[i] < KANAN[j], maka:
                Simpan KIRI[i] ke dalam Array[k]
                Tambah i
            Jika tidak:
                Simpan KANAN[j] ke dalam Array[k]
                Tambah j
            Tambah k
        AKHIR SELAMA
        
        SELAMA ada elemen yang tersisa di KIRI:
            Simpan KIRI[i] ke dalam Array[k]
            Tambah i
            Tambah k
        AKHIR SELAMA
        
        SELAMA ada elemen yang tersisa di KANAN:
            Simpan KANAN[j] ke dalam Array[k]
            Tambah j
            Tambah k
        AKHIR SELAMA
    AKHIR JIKA
AKHIR FUNGSI

Bubble Sort:
Fungsi BUBBLE_SORT(Array)
    Tentukan n = panjang Array
    UNTUK setiap elemen i dari 0 sampai n-1:
        UNTUK setiap elemen j dari 0 sampai n-i-2:
            Jika Array[j] > Array[j+1], maka:
                Tukar Array[j] dengan Array[j+1]
        AKHIR UNTUK
    AKHIR UNTUK
AKHIR FUNGSI

Program utamnanya:
MULAI

1. Buat data acak DATA (100 angka antara 1 dan 100)
2. Salin DATA menjadi arr_merge dan arr_bubble

3. Mengukur waktu untuk Merge Sort:
    - Mulai pengukuran waktu
    - Panggil MERGE_SORT untuk arr_merge
    - Hentikan pengukuran waktu
    - Hitung waktu yang dibutuhkan untuk Merge Sort (time_complexity_merge)

4. Mengukur waktu untuk Bubble Sort:
    - Mulai pengukuran waktu
    - Panggil BUBBLE_SORT untuk arr_bubble
    - Hentikan pengukuran waktu
    - Hitung waktu yang dibutuhkan untuk Bubble Sort (time_complexity_bubble)

5. Tampilkan hasil:
    - "Hasil perhitungan dari bubble sort" dan arr_bubble
    - "Hasil perhitungan dari merge sort" dan arr_merge
    - "Time Complexity untuk Bubble Sort" dan time_complexity_bubble
    - "Time Complexity untuk Merge Sort" dan time_complexity_merge

SELESAI
'''
import time
import random

# Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Generate random numbers
arr_bubble = [random.randint(1, 100) for _ in range(100)]
arr_merge = [random.randint(1, 100) for _ in range(100)]

#untuk bubble
start_time_bubble_sort = time.perf_counter()
bubble_sort(arr_bubble)
end_time_bubble_sort = time.perf_counter()
time_complexity_bubble = end_time_bubble_sort - start_time_bubble_sort

#untuk merge
start_time_merge_sort = time.perf_counter()
merge_sort(arr_merge)
end_time_merge_sort = time.perf_counter()
time_complexity_merge = end_time_merge_sort - start_time_merge_sort



print(f"Hasil perhitungan dari bubble sort adalah sebagai berikut: {arr_bubble}\n")
print(f"Hasil perhitungan dari merge sort adalah sebagai berikut: {arr_merge}\n")

print(f"Time Complexity untuk Bubble Sort {time_complexity_bubble:.10f} detik \n")
print(f"Time Complexity untuk Merge Sort  {time_complexity_merge:.10f} detik \n")