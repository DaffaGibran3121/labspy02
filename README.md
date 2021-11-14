# Repository Praktikum Labspy 02 dan Labspy03
# labspy02
## Algoritma untuk menentukan nilai terbesar dari 3 buah bilangan
# Flowchart
![Flowchart (1)](https://user-images.githubusercontent.com/92356397/141675919-9be3d2d1-d9be-4748-963c-fe5b094d445f.png)
## Menggunakan statement if untuk mencari nilai terbesar dari 3 bilangan
untuk a di inisiasikan sebagai bilangan pertama, b untuk bilangan kedua, c untuk bilangan ketiga

dengan cara statement if untuk a sebagai bilangan pertama, elif untuk b bilangan kedua, dan else untuk c bilangan ketiga, berikut gambar program dan tulisan programnya
![Screenshot (65)](https://user-images.githubusercontent.com/92356397/141676320-7cad99e6-5cd7-4bdb-8527-d5bf13096b8c.png)
untuk hasil ketika program dijalankan, bilangan pertama yang terbesar
![Screenshot (67)](https://user-images.githubusercontent.com/92356397/141676348-3df6fe90-3510-44da-98ac-64f01936c087.png)
untuk bilangan kedua yang terbesar ketika program dijalankan
![Screenshot (70)](https://user-images.githubusercontent.com/92356397/141676526-74eba496-2235-4228-a169-65f55a7e8480.png)
sedangkan untuk bilangan ketiga yang terbesar ketika program dijalankan
![Screenshot (71)](https://user-images.githubusercontent.com/92356397/141676535-0083a9fc-03c7-43d4-a5a4-5f8e3e23e84b.png)
# Labspy03
# Latihan 1
## Program Untuk Menampilkan n Bilangan Acak Yang Lebih Kecil Dari 0.5
## Flowchart Program
### berikut flowchart dari program latihan 1, untuk menampilkan n bilangan acak yang lebih kecil dari 0.5
![flowchart_latihan1](https://user-images.githubusercontent.com/92356397/141676672-dc657e37-ebad-45dc-90fc-fe84a58d0756.png)
#### Penjelasan alur program
1.print("Tampilkan n bilangan acak yang lebih kecil dari 0.5") - adalah perintah untuk menampilkan judulnya.

2.jumlah = int(input("Masukkan jumlah n: ")) - adalah perintah untuk menginput nilai n tersebut

3.import random - adalah perintah untuk mengimport built-in random yang telah tersedia di python

4.for i in range(jumlah): - adalah perintah untuk i sebagai integer dalam baris jumlah

5.print("data ke", i+1,"=",(random.uniform(0.1,0.5))) - adalah perintah untuk menampilkan hasil yang telah di input dengan ketentuan random uniform mulai dari nilai 0.1 sampai 0.5
#### berikut gambaran programnya
![Screenshot (75)](https://user-images.githubusercontent.com/92356397/141676914-78da6967-e039-4be8-96de-5c0c3315b0c5.png)
#### berikut hasil dari program saat dijalankan
![Screenshot (74)](https://user-images.githubusercontent.com/92356397/141676919-c4ac3d81-8d55-438d-9afd-c0c2d789d221.png)
# Latihan 2
## Buat program untuk menampilkan bilangan terbesar dari n buah data yang diinputkan
### Flowchart program
#### Berikut flowchar untuk program menampilkan bilangan tersbesar dari n buah data yang diinputkan
![flowchart_latihan2 (1)](https://user-images.githubusercontent.com/92356397/141677652-fd9f1084-ddb5-43e5-a5c0-145f34f0cd67.png)
## Penjelasan alur program
1. print("Menampilkan bilangan terbesar dari n buah data yang diinput") - adalah perintah untuk menampilkan judul program

2. max = 0 - adalah perintah untuk menampilkan nilai max yang adalah 0

3. while True: - adalah perintah untuk pengulangan hingga waktu yang tidak ditentukan

4. a = int(input("Masukkan Bilangan: ")) - adalah perintah untuk menginput nilai integer

5. if max < a: - adalah perintah untuk tipe data if atau jika, maksimal nilai lebih kecil dari a atau integer

6. max = a - perintah untuk nilai maximal sama dengan a atau integer

7. if a ==0: - perintah untuk tipe data if atau jika a sama dengan 0 maka

8. break - perintah untuk mengakhiri pengulangan, jadi jika menginput nilai 0 maka pengulangan berakhir atau selesai

9. print("Bilangan Terbesar Adalah: ", max) - adalah perintah untuk menampilkan hasil bilangan yang terbesar dari angka-angka yang telah terinput
#### berikut gambaran programnya
![Screenshot (79)](https://user-images.githubusercontent.com/92356397/141677277-4752b581-7c6b-497d-987e-5b038c39109d.png)
berikut hasil dari program setelah dijalankan

![Screenshot (78)](https://user-images.githubusercontent.com/92356397/141677290-77aa05fb-9124-4ff5-aafa-280bf3150881.png)
# Program 1
## Program untuk menghitung laba investasi
### Flowchart program
#### berikut flowchart dari program menghitung laba investasi
![flowchart_program1](https://user-images.githubusercontent.com/92356397/141677217-9b7d1a2b-531e-4d8f-a6f0-81d6033b3abc.png)
#### penjelasan alur program
print("Laba Investasi") - adalah untuk menampilkan judul

x = int(input("Uang Modal Awal: ")) - adalah untuk menginput nilai x sebagai modal awal

a = 0*x - a adalah bulan pertama, karena bulan pertama belum memiliki laba, jadi masih 0 dikali dengan x nilai uang modal awal

b = 0*x - b adalah bulan kedua, karena bulan kedua belum memiliki laba, jadi nilai x dari uang modal dikali dengan 0

c = 0.01*x - c adalah bulan ketiga, dan sudah memiliki laba 1%, jadi ditulis 0.01 bentuk sederhana dari 1% dikali dengan modal atau uang awal dengan nilai x

d = 0.01*x - d adalah bulan keempat, dan labanya 1%, jadi ditulis 0.01 dikalikan dengan nilai x yang adalah uang awal atau modal

e = 0.05*x - e adalah bulan kelima, dan laba pada bulan kelima sebesar 5%, maka ditulis 0.05 dikalikan dengan nilai x untuk nilai uang awal atau modal

f = 0.05*x - f adalah bulan keenam, dan laba pada bulan keenam sebesar 5%, maka ditulis 0.05 dikalikan dengan nilai x untuk nilai uang awal atau modal

g = 0.05*x - g adalah bulan ketujuh, dan laba pada bulan ketujuh sebesar 5%, maka ditulis 0.05 dikalikan dengan nilai x untuk nilai uang awal atau modal

h = 0.02*x - h adalah bulan kedelapan, dan laba pada bulan kedelapan sebesar 2%, maka ditulis 0.02 dikalikan dengan nilai x untuk nilai uang awal atau modal

y=[a,b,c,d,e,f,g,h] - adalah untuk menentukan syarat y yang berisi a,b,c,d,e,f,g,h

for i in range(len(y)): - adalah untuk perulangan data dengan isi data y, dengan menampilkan urutan laba perbulan sesuai range yang di tentukan dengan hasil ke urutan yang diinputkan dari data y

print("Laba Bulan Ke",i+1 ,"sebesar: ",y[i]) - untuk menampilkan hasil laba dari bulan ke 1 sampai terakhir

z=(a+b+c+d+e+f+g+h) - Z untuk data yang berisi hasil penjumlahan laba dari bulan pertama sampai bulan ke delapan

print("Jumlah Laba Selama 8 Bulan: ",z) - menampilkan hasil dari jumlah laba
#### berikut gambaran programnya
![Screenshot (82)](https://user-images.githubusercontent.com/92356397/141677688-38da0392-926e-4dc9-872d-56b0fee7a780.png)
#### berikut hasil dari program setelah dijalankan
![Screenshot (83)](https://user-images.githubusercontent.com/92356397/141677700-a83f7820-5d5d-4012-881c-ed49173521a9.png)


