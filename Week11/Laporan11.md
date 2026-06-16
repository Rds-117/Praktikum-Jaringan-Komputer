# Laporan Praktikum Jaringan Modul 11 - DHCP

## A. Pengenalan

DHCP (Dynamic Host Configuration Protocol) merupakan protokol jaringan yang digunakan untuk memberikan konfigurasi jaringan, terutama alamat IP, kepada perangkat secara otomatis. Dengan DHCP, administrator tidak perlu melakukan konfigurasi alamat IP secara manual pada setiap perangkat yang terhubung ke jaringan, sehingga proses pengelolaan jaringan menjadi lebih mudah dan efisien.

### Fungsi DHCP

1. Mencegah terjadinya konflik alamat IP antar perangkat dalam jaringan.
2. Melakukan pembaruan alamat IP secara otomatis sesuai kebutuhan jaringan.
3. Mendukung penggunaan kembali alamat IP yang sudah tidak digunakan oleh perangkat lain.

### Kelebihan DHCP

1. Memungkinkan konfigurasi alamat IP dilakukan secara otomatis.
2. Meningkatkan efisiensi dalam pengelolaan jaringan.
3. Mendukung pembaruan alamat IP secara dinamis tanpa campur tangan administrator.

### Kekurangan DHCP

1. Ketergantungan pada satu server DHCP sebagai pusat layanan.
2. Memiliki risiko keamanan apabila tidak dikonfigurasi dengan baik.
3. Pengelolaannya dapat menjadi lebih kompleks pada jaringan berskala besar.

## B. Proses DORA

DORA merupakan singkatan dari Discover, Offer, Request, dan Acknowledgment. DORA adalah tahapan komunikasi yang terjadi antara DHCP Client dan DHCP Server untuk memperoleh konfigurasi jaringan secara otomatis.

1. **Discover**
   DHCP Client mengirimkan pesan DHCP Discover untuk mencari dan memberitahukan keberadaannya kepada DHCP Server serta meminta konfigurasi jaringan.

2. **Offer**
   Setelah menerima pesan Discover, DHCP Server merespons dengan mengirimkan DHCP Offer yang berisi informasi konfigurasi jaringan yang tersedia, termasuk alamat IP yang dapat digunakan oleh client.

3. **Request**
   DHCP Client memilih penawaran yang diterima dan mengirimkan DHCP Request kepada server untuk meminta penggunaan alamat IP yang ditawarkan.

4. **Acknowledgment**
   DHCP Server mengirimkan DHCP Acknowledgment (DHCP ACK) sebagai konfirmasi bahwa permintaan client telah diterima dan konfigurasi jaringan dapat digunakan.

Contoh:
    ![](../assets/week%2011/1.png)  






Source:
https://www.geeksforgeeks.org/computer-networks/dynamic-host-configuration-protocol-dhcp/