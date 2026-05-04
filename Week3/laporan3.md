Tujuan Praktikum

Tujuan dari praktikum ini adalah untuk memahami cara melakukan analisis paket jaringan menggunakan Wireshark, khususnya pada protokol HTTP. Selain itu, praktikum ini bertujuan agar mahasiswa mampu mengidentifikasi isi paket data, membaca struktur komunikasi jaringan, serta memahami bagaimana data dikirim dan diterima melalui jaringan.

Langkah-Langkah:

1.Menjalankan aplikasi Wireshark.

![](../assets/week%203/1.png)

LINK 1 Basic HTTP GET/response interaction

2.Lalu buka browser dan tempelkan link ini, http://gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file1.html.

![](../assets/week%203/2.png)

3.Buka kembali Wireshark, lalu ketik **http** (tanpa tanda kutip) pada kolom pencarian dan tekan Enter. Setelah itu, cari baris dengan keterangan length **200 OK (text/html)**. Dari sana, kita dapat melihat bagian **Hypertext** serta **Line-based text data**.

![](../assets/week%203/3.png)

![](../assets/week%203/4.png)

LINK 2 Retrieving Long Documents

4.Lalu buka browser kembali dan tempelkan link ini, http://gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file3.html.

![](../assets/week%203/5.png)

5.Buka kembali Wireshark, lalu ketik **http** (tanpa tanda kutip) pada kolom pencarian dan tekan Enter. Setelah itu, cari baris dengan keterangan length **200 OK (text/html)**. Dari sana, kita dapat melihat bagian **Hypertext** serta **Line-based text data**.

![](../assets/week%203/6.png)

![](../assets/week%203/7.png)

LINK 3 HTML Documents dengan Embedded Objects

6.Lalu buka browser kembali dan tempelkan link ini, http://gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file4.html.

![](../assets/week%203/8.png)

7.Buka kembali Wireshark, lalu ketik **http** (tanpa tanda kutip) pada kolom pencarian dan tekan Enter. Setelah itu, cari baris dengan keterangan length **200 OK (text/html)**. Dari sana, kita dapat melihat bagian **Hypertext** serta **Line-based text data**.

![](../assets/week%203/9.png)

LINK 4 HTTP Authentication

8.Lalu Buka URL: http://gaia.cs.umass.edu/wireshark-labs/protected_pages/HTTP-wireshark-file5.html pada browser, akan muncul tampilan login seperti ini

![](../assets/week%203/10.png)

9.Masukkan username wireshark-students dan password network

![](../assets/week%203/11.png)

10.Pastikan login berhasil

![](../assets/week%203/12.png)

11.Buka kembali Wireshark, lalu ketik **http** (tanpa tanda kutip) pada kolom pencarian dan tekan Enter. Setelah itu, cari baris dengan keterangan length **200 OK (text/html)**. Dari sana, kita dapat melihat bagian **Hypertext** serta **Line-based text data**.

![](../assets/week%203/13.png)

![](../assets/week%203/14.png)



