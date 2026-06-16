## Pengenalan ARP dan Ethernet

Setelah pada praktikum sebelumnya membahas mengenai Internet Control Message Protocol (ICMP), pada modul ini akan dibahas mengenai Address Resolution Protocol (ARP) dan Ethernet. ARP merupakan singkatan dari Address Resolution Protocol, yaitu protokol jaringan yang berfungsi untuk menerjemahkan atau memetakan alamat IP menjadi alamat MAC (Media Access Control). Protokol ini memungkinkan perangkat dalam jaringan lokal untuk mengetahui alamat fisik tujuan sehingga proses komunikasi data dapat berlangsung dengan benar.

Dalam model OSI, ARP bekerja di antara Layer 2 (Data Link Layer) dan Layer 3 (Network Layer). Ketika suatu perangkat mengetahui alamat IP tujuan namun belum mengetahui alamat MAC tujuan, ARP akan digunakan untuk memperoleh informasi alamat MAC tersebut. Setelah alamat MAC diperoleh, data dapat dikirimkan dalam bentuk frame Ethernet ke perangkat yang tepat pada jaringan lokal.

## Cara Kerja ARP

Proses kerja ARP dimulai ketika sebuah perangkat ingin mengirimkan data ke perangkat lain dalam jaringan lokal. Pada awalnya, perangkat pengirim hanya mengetahui alamat IP tujuan, sedangkan pengiriman frame pada Data Link Layer memerlukan alamat MAC tujuan.

Langkah pertama yang dilakukan adalah memeriksa tabel ARP (ARP Cache) yang tersimpan pada memori lokal perangkat. Jika alamat MAC yang sesuai dengan alamat IP tujuan telah tersedia, maka perangkat dapat langsung mengirimkan data. Namun, apabila informasi tersebut tidak ditemukan, perangkat akan mengirimkan paket ARP Request secara broadcast ke seluruh perangkat dalam jaringan lokal.

Pesan ARP Request pada dasarnya berisi pertanyaan mengenai pemilik alamat IP tertentu. Seluruh perangkat dalam jaringan akan menerima pesan tersebut, tetapi hanya perangkat yang memiliki alamat IP yang sesuai yang akan memberikan respons. Perangkat tersebut kemudian mengirimkan ARP Reply yang berisi alamat MAC miliknya kepada pengirim. Setelah menerima balasan tersebut, perangkat pengirim akan menyimpan pasangan alamat IP dan alamat MAC ke dalam ARP Cache untuk digunakan pada komunikasi berikutnya.

## Implementasi Praktikum

### 1 Menghapus dan Memeriksa ARP Cache

Langkah pertama yang dilakukan adalah membuka Command Prompt (CMD) dengan hak akses administrator. Selanjutnya dijalankan perintah `arp -d *` untuk menghapus seluruh entri pada tabel ARP yang tersimpan di sistem. Tujuan dari langkah ini adalah memastikan bahwa proses ARP dapat diamati secara langsung selama praktikum berlangsung.

Pada saat pelaksanaan praktikum terjadi kendala sehingga digunakan alternatif perintah `netsh interface ip delete arpcache`, yang memiliki fungsi serupa untuk menghapus seluruh ARP Cache. Setelah proses penghapusan selesai, perintah `arp -a` dijalankan untuk menampilkan isi tabel ARP dan memastikan bahwa cache telah berhasil dibersihkan.
    ![](../assets/week%2013/1.png)

    
## 2 Konfigurasi Wireshark
Setelah ARP Cache dibersihkan, langkah berikutnya adalah membuka aplikasi Wireshark dan memilih antarmuka jaringan yang sedang digunakan untuk terhubung ke internet. Selanjutnya masuk ke menu **Analyze → Enabled Protocols**, kemudian menonaktifkan protokol IPv4 dengan menghilangkan tanda centang pada opsi tersebut. Pengaturan ini dilakukan agar proses pengamatan paket ARP menjadi lebih mudah karena lalu lintas IPv4 tidak ditampilkan.


![](../assets/week%2013/2.png)

## 3 Pengujian Menggunakan Website

Pada tahap pengujian, digunakan halaman web berikut sebagai media untuk menghasilkan lalu lintas jaringan:

`http://gaia.cs.umass.edu/wireshark-labs/HTTP-ethereal-lab-file3.html`

![](../assets/week%2013/3.png)

Sebelum membuka halaman tersebut, cache browser dan riwayat akses dihapus terlebih dahulu agar browser benar-benar melakukan permintaan baru ke server dan menghasilkan aktivitas jaringan yang dapat diamati melalui Wireshark.

### 4 Penyaringan Paket ARP

Kembali ke Wireshark, filter `arp` diterapkan pada kolom filter untuk menampilkan hanya paket-paket ARP. Dengan menggunakan filter ini, proses analisis menjadi lebih mudah karena informasi mengenai alamat MAC pengirim (Sender MAC Address) dan alamat MAC tujuan (Target MAC Address) dapat diamati secara langsung pada paket ARP Request maupun ARP Reply.
    ![](../assets/week%2013/4.png)

### 5 Analisis ARP Request

ARP Request terjadi ketika suatu perangkat mengetahui alamat IP tujuan tetapi belum mengetahui alamat MAC yang bersesuaian. Sebagai contoh, perangkat dengan alamat IP 192.168.68.52 ingin berkomunikasi dengan perangkat yang memiliki alamat IP 192.168.68.1.

Karena alamat MAC tujuan belum diketahui, perangkat pengirim akan mengirimkan paket ARP Request secara broadcast kepada seluruh perangkat dalam jaringan lokal. Pada paket tersebut, alamat tujuan Ethernet diisi dengan alamat broadcast sehingga seluruh perangkat dapat menerimanya. Informasi yang terkandung dalam paket tersebut umumnya berbentuk pertanyaan seperti:

“Who has 192.168.68.1? Tell 192.168.68.52”

Pada tahap ini, Target MAC Address masih bernilai kosong karena informasi tersebut belum diketahui oleh pengirim.
    ![](../assets/week%2013/5.png)

## 6 Analisis ARP Reply

Setelah menerima ARP Request, perangkat yang memiliki alamat IP 192.168.68.1 akan mengirimkan ARP Reply secara unicast kepada pengirim. Paket balasan ini berisi informasi alamat MAC yang dimiliki oleh perangkat tersebut.

![](../assets/week%2013/7.png)

Setelah ARP Reply diterima, perangkat pengirim akan menyimpan pasangan alamat IP dan alamat MAC ke dalam ARP Cache sehingga komunikasi berikutnya dapat dilakukan tanpa perlu mengirimkan ARP Request kembali. Dengan demikian, fungsi utama ARP adalah membantu perangkat menemukan alamat MAC tujuan berdasarkan alamat IP yang diketahui, sehingga frame Ethernet dapat dikirim ke perangkat yang tepat dalam jaringan lokal.





![](../assets/week%2013/7.png)
