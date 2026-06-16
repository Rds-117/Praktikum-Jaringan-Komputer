# Laporan Jaringan Komputer Informatika Week 14

## Pengenalan

Pada praktikum kali ini, pembahasan berlanjut setelah materi ARP dan Ethernet, yaitu mengenai teknologi Wi-Fi 802.11. Standar ini dikembangkan oleh IEEE sebagai acuan untuk komunikasi jaringan nirkabel pada Wireless Local Area Network (WLAN). Sejak pertama kali diperkenalkan pada tahun 1997, standar 802.11 mengalami berbagai pengembangan seperti 802.11b, 802.11g, hingga 802.11n yang masing-masing membawa peningkatan dalam hal kecepatan transmisi, cakupan sinyal, serta kemampuan menangani lebih banyak perangkat dalam satu jaringan.

## 1. Cara Kerja Wi-Fi 802.11

Prinsip kerja Wi-Fi 802.11 dimulai dari proses konversi data digital menjadi sinyal radio oleh perangkat pengguna seperti laptop atau smartphone. Data tersebut kemudian dipancarkan melalui frekuensi 2,4 GHz atau 5 GHz menggunakan kartu jaringan nirkabel. Sinyal yang dikirim akan diterima oleh Access Point (router), lalu diubah kembali menjadi data digital agar dapat diteruskan ke jaringan internet.

Proses ini juga terjadi secara sebaliknya ketika router mengirimkan data dari internet ke perangkat pengguna, di mana sinyal radio kembali dikonversi menjadi data yang dapat dipahami oleh perangkat.

## 2. Implementasi Praktikum

Praktikum dilakukan menggunakan file **Wireshark_802_11.pcap** yang disediakan pada modul.

![](../assets/week%2014/1.png)

## Analisis Beacon Frame
![](../assets/week%2014/2.png)

Beacon Frame digunakan untuk mengidentifikasi informasi jaringan yang dipancarkan oleh Access Point. Dari hasil analisis diperoleh bahwa jaringan menggunakan standar **802.11b** dengan kecepatan **1 Mb/s**, beroperasi pada **Channel 6 (2437 MHz)**, serta memiliki kekuatan sinyal **-29 dBm** dan nilai **SNR 71 dB** yang menunjukkan kualitas sinyal yang sangat baik.



Selanjutnya digunakan filter wwlan.fc.subtype == 8 && wlan.fc.type == 0 pada Wireshark untuk memfilter dan menampilkan Beacon Frame, yaitu paket yang berfungsi sebagai sinyal pemberitahuan (beacon) dalam jaringan Wi-Fi untuk mengumumkan keberadaan Access Point kepada perangkat di sekitarnya.

![](../assets/week%2014/3.png)


![](../assets/week%2014/4.png)
Analisis Data Transfer

Untuk mengamati proses transfer data digunakan filter: ip.addr == 128.119.245.12

Filter tersebut menampilkan komunikasi antara host lokal dan server tujuan.


  ![](../assets/week%2014/5.png)
Analisis Association

Proses association diamati melalui frame Association Request dan Association Response. Paket-paket tersebut menunjukkan bahwa host berusaha terhubung ke Access Point dengan SSID "linksys_SES_24086". Munculnya beberapa Association Request menandakan adanya proses negosiasi koneksi antara perangkat klien dan Access Point sebelum koneksi berhasil dibangun.

  ![](../assets/week%2014/6.png)

Analisis Disassociation

Untuk mencari frame pemutusan koneksi digunakan filter: wlan.fc.type_subtype == 0x0a
    ![](../assets/week%2014/7.png)
Namun, hasil penyaringan tidak menunjukkan adanya frame Disassociation. Hal ini menandakan bahwa selama proses perekaman berlangsung, tidak terjadi pemutusan hubungan antara host dan Access Point.