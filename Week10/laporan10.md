# Laporan Praktikum Jaringan Modul 10 - IP
## Pengenalan
    IP adalah singktana dari internet protokol, yakni alamat yang digunakan perangkat untuk melakukan komunikasi, jenisnya, yakni.

        1. IPv4 dan IPv6 (32-bit dan 128-bit)
        2. Public dan Private IP Address

    fungsinya :
    
        1. alamat tujuan paket akan dikirim
        2. identitas  suatu perangkat


## Pengecekan IP Address

1. Buka cmd dan ketik ipconfig, lalu enter
    ![](../assets/week%2010/1.png)

2. scroll kebawah, cari bagian wifi adapter/wireless/modul wifi.
    ![](../assets/week%2010/2.png)

3. gambar di atas beripakan hasil dari ipconfig, dimana itu menampilkan ip address dari device kita

## Menangkap Paket Dari Eksekusi Traceroute

buka cmd, dan ketik : tracert gaia.cs.umass.edu
    ![](../assets/week%2010/3.png)
hasilnya seperti diatas ini

Jika menggunakan wireshark + cmd :
1. Buka wireshark
2. lakukan capturing pada jaringan yang kalian gunakan (contoh wifi adapter)
3. buka cmd, dan ketik : tracert gaia.cs.umass.edu
4. Balik ke wireshark, filtering dengan kata icmp.
5. hasil :
  ![](../assets/week%2010/4.png)


## Fragmentasi 

Fragmentasi merupakan mekanisme pemecahan paket IP berukuran besar menjadi beberapa bagian yang lebih kecil untuk memastikan paket tersebut dapat melewati jaringan dengan batas ukuran transmisi maksimum yang telah ditentukan.
contoh :
1. Buka wireshark
2. lakukan capturing pada jaringan yang kalian gunakan (contoh wifi adapter)
3. Buka cmd, dan ketik: ping 8.8.8.8 -l 3000
![](../assets/week%2010/5.png)
4. Balik kewireshark, filtering menggunakan kata: ip.flags.mf == 1 || ip.frag_offset > 0
5. hasil :
    ![](../assets/week%2010/6.png)


## IPv6
Berikut langkah untuk melihat protokol jaringan IPV6 di wireshark
1. Buka wireshark
2. lakukan capturing pada jaringan yang kalian gunakan (contoh wifi adapter)
3. Lakukan Filtering dengan kata: ipv6
4. Hasil :
    ![](../assets/week%2010/7.png)

