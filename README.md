# Algoritma

Nama: Yuyun Aulia Afrianty/ Nim: F55123025

#(Peseudocode Bubble Sort:)
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

#(Peseudocode Marge Sort:)
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

