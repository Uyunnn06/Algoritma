# Algoritma

Nama: Yuyun Aulia Afrianty/ Nim: F55123025

#### (Peseudocode Bubble Sort:)
```
Fungsi BUBBLE_SORT(Array)
    Tentukan n = panjang Array
    UNTUK setiap elemen i dari 0 sampai n-1:
        UNTUK setiap elemen j dari 0 sampai n-i-2:
            Jika Array[j] > Array[j+1], maka:
                Tukar Array[j] dengan Array[j+1]
        AKHIR UNTUK
    AKHIR UNTUK
AKHIR FUNGSI 
```
Bubble Sort
Pseudocode: 
- Bubble Sort bekerja dengan cara membandingkan elemen-elemen yang berdekatan dan menukarnya jika urutannya salah. Proses ini diulang hingga seluruh array terurut.

Big O (Worst Case) dan Big Theta (Average Case):
1. Iterasi Pertama: Pada iterasi pertama, kita membandingkan n elemen.
2. Iterasi Kedua: Pada iterasi kedua, kita hanya perlu membandingkan n-1 elemen, dan seterusnya.
3. Jumlah Iterasi: Total jumlah perbandingan adalah n + (n-1) + (n-2) + ... + 1, yang menghasilkan jumlah perbandingan sekitar O(n²).

Analisis:
- Big O (Worst Case): O(n²)  
- Big Theta (Average Case): Θ(n²)  
Pada Bubble Sort, baik di kasus terbaik (sudah terurut) maupun kasus terburuk (urutannya terbalik), jumlah iterasi tetap O(n²). Pada kasus terbaik, jika array sudah terurut, algoritma masih perlu melakukan pengecekan perbandingan, yang tetap membutuhkan O(n) waktu.


#### (Peseudocode Merge Sort: )
```
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
```
Merge Sort
Pseudocode: 
- Merge Sort menggunakan pembagian dan penggabungan, yang membuatnya bekerja secara rekursif dengan membagi array menjadi dua bagian, kemudian menggabungkannya setelah diurutkan.

Big O (Worst Case) dan Big Theta (Average Case):
1. Operasi Pembagian: Pada setiap langkah, array dibagi menjadi dua bagian. Pembagian ini terjadi hingga setiap bagian berukuran satu elemen, yang berarti kedalaman rekursi adalah log₂(n), di mana n adalah panjang array.
2. Operasi Penggabungan: Pada setiap tingkat rekursi, kita menggabungkan dua bagian yang telah diurutkan. Proses penggabungan memerlukan waktu O(n) untuk setiap tingkat rekursi. Karena ada log₂(n) tingkat rekursi, penggabungan dilakukan sebanyak O(n log n) waktu.

Analisis:
- Big O (Worst Case): O(n log n)
- Big Theta (Average Case): Θ(n log n)
Merge Sort memiliki kompleksitas waktu O(n log n) baik pada kasus terbaik maupun terburuk, karena pembagian dan penggabungan tetap terjadi di setiap langkah.

