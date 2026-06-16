# Laporan Praktikum Jaringan Komputer Modul 12

## Internet Control Message Protocol (ICMP)

### Tujuan Praktikum

1. Memahami dan menganalisis cara kerja protokol ICMP menggunakan aplikasi Wireshark.
2. Mengimplementasikan program ICMP Pinger untuk menguji konektivitas jaringan.

## Pengertian ICMP

Internet Control Message Protocol (ICMP) merupakan protokol yang bekerja pada lapisan jaringan (Network Layer) dalam model TCP/IP. Protokol ini digunakan oleh perangkat jaringan, seperti router, server, dan komputer klien, untuk mengirimkan informasi mengenai kondisi jaringan, melaporkan kesalahan yang terjadi selama proses komunikasi data, serta membantu proses diagnostik dan pemecahan masalah jaringan.

## Fungsi ICMP

ICMP memiliki beberapa fungsi penting dalam komunikasi jaringan, antara lain:

1. Menyampaikan informasi mengenai kesalahan yang terjadi selama proses pengiriman paket data.
2. Memeriksa status konektivitas antara dua perangkat dalam jaringan.
3. Membantu proses pelacakan jalur yang dilalui paket data dari sumber ke tujuan.
4. Memberikan notifikasi ketika suatu host atau tujuan tidak dapat dijangkau.
5. Menginformasikan adanya rute alternatif yang lebih efisien untuk proses pengiriman data.

## Cara Kerja ICMP

Cara kerja ICMP berfokus pada pertukaran pesan kontrol dan informasi status jaringan. Mekanisme ini memungkinkan perangkat jaringan untuk mendeteksi, melaporkan, dan menangani berbagai kondisi yang terjadi selama proses komunikasi data.

1. **Deteksi Permasalahan atau Permintaan Diagnostik**
   Ketika paket IP sedang dikirimkan melalui jaringan, perangkat perantara seperti router atau perangkat tujuan dapat mendeteksi adanya masalah, misalnya nilai Time To Live (TTL) yang habis atau tujuan yang tidak dapat ditemukan. Selain itu, ICMP juga dapat diaktifkan melalui permintaan diagnostik, seperti penggunaan perintah ping.

2. **Pembuatan Pesan ICMP**
   Setelah mendeteksi suatu kondisi tertentu, perangkat akan membuat pesan ICMP yang berisi informasi mengenai jenis pesan (Type), kode pesan (Code), serta sebagian data dari paket IP yang terkait dengan kejadian tersebut.

3. **Enkapsulasi ke Dalam Paket IP**
   Pesan ICMP yang telah dibuat kemudian dibungkus langsung ke dalam paket IP. Berbeda dengan data aplikasi yang umumnya menggunakan TCP atau UDP, ICMP tidak memerlukan protokol transport sebagai perantara.

4. **Pengiriman ke Pengirim Asal**
   Paket IP yang membawa pesan ICMP akan dikirim kembali kepada perangkat pengirim awal sebagai bentuk pemberitahuan mengenai kondisi yang terjadi selama proses transmisi.

5. **Penerimaan dan Analisis Pesan**
   Setelah pesan ICMP diterima, sistem operasi atau aplikasi jaringan akan menganalisis informasi yang terkandung di dalamnya. Berdasarkan hasil analisis tersebut, perangkat dapat menampilkan pesan kesalahan, melakukan tindakan korektif, atau melanjutkan proses komunikasi sesuai kondisi jaringan yang ada.

## Percobaan
1. Jalankan wireshark dan pilih interface wifi
2. Buka cmd, ketikan perintah "ping -n 10 www.ox.ac.uk"
    ![](../assets/week%2012/1.png)  

3. Lalu pada wireshark, stop capture dan filter "icmp"
      ![](../assets/week%2012/2.png)

4. pilih salah satu paket ICMP echo reply
     ![](../assets/week%2012/3.png)
Alamat IP 104.20.34.13 berperan sebagai pengirim paket balasan yang ditujukan kepada klien dengan alamat IP 192.168.68.52

Berdasarkan informasi pada panel detail Wireshark, paket tersebut memiliki nilai **Type = 0** dan **Code = 0**, yang menunjukkan bahwa paket tersebut merupakan **ICMP Echo Reply**. Pesan ini menandakan bahwa host tujuan telah berhasil menerima **ICMP Echo Request** yang dikirim sebelumnya dan memberikan respons kembali kepada pengirim. Dengan demikian, dapat disimpulkan bahwa perangkat tujuan dalam keadaan aktif serta dapat dijangkau melalui jaringan.

5. pilih salah satu paket ICMP echo request
    ![](../assets/week%2012/4.png)
Alamat 192.168.68.52 berperan sebagai pengirim paket balasan yang ditujukan kepada klien dengan alamat IP 104.20.34.13

Pada panel detail di bagian bawah, teridentifikasi bahwa pesan ini memiliki atribut Type: 8 dan Code: 0, yang secara standar protokol didefinisikan sebagai pesan ICMP Echo (ping) Request. Ini berarti komputer klien sedang meminta konfirmasi kehadiran dan konektivitas dari komputer tujuan.

## Pesan ICMP yang dihasilkan oleh program Traceroute
1. Jalankan wireshark dan pilih interface wifi
2. Buka cmd, ketikan perintah "tracert www.ox.ac.uk"
    ![](../assets/week%2012/5.png)
3. Lalu pada wireshark, stop capture dan filter "icmp"
    ![](../assets/week%2012/6.png)

Berdasarkan gambar yang ditampilkan, proses pelacakan rute (traceroute) memanfaatkan dua jenis pesan ICMP untuk mengidentifikasi jalur yang dilalui paket data menuju tujuan. Ketika nilai Time To Live (TTL) suatu paket mencapai nol sebelum sampai ke tujuan, router yang menerima paket tersebut akan membuangnya dan mengirimkan pesan ICMP Time Exceeded kepada pengirim. Dengan meningkatkan nilai TTL secara bertahap pada setiap pengiriman, aplikasi traceroute dapat mengetahui dan mencatat setiap router yang dilewati paket di sepanjang jalur komunikasi.

Selain itu, proses traceroute juga dapat menghasilkan pesan ICMP Destination Unreachable atau respons lain dari host tujuan. Pesan ini menunjukkan bahwa paket telah mencapai tujuan akhir atau mengindikasikan bahwa host tujuan tidak dapat dijangkau karena adanya kendala pada jaringan. Melalui kombinasi respons ICMP tersebut, traceroute mampu memetakan jalur komunikasi serta membantu dalam proses analisis dan diagnosis masalah jaringan.