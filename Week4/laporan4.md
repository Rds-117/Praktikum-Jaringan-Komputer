# Modul 4 DNS
## A. Nslookup
Perintah **nslookup** digunakan untuk memperoleh informasi DNS dengan mengirimkan kueri ke server DNS tertentu. Melalui perintah ini, sebuah host dapat meminta data DNS dari berbagai jenis server, seperti server DNS root, server domain tingkat atas (TLD), server DNS otoritatif, maupun server DNS perantara. Prosesnya dimulai ketika nslookup mengirimkan permintaan DNS ke server yang dituju, kemudian menerima respons dari server tersebut, dan akhirnya menampilkan hasil informasi DNS yang diperoleh kepada pengguna.
    ![](../assets/week%204/1.png)


## Lakukan beberapa hal berikut (dan amati hasilnya):
1. Jalankan nslookup untuk mendapatkan alamat IP dari server web di Asia. Berapa alamat IP server tersebut?
    ![](../assets/week%204/2.png)
Dari hasil nslookup untuk server berita di indonesia, kita dapatkan ipnya 203.190.242.211 dan 103.49.221.211

2. Jalankan nslookup agar dapat mengetahui server DNS otoritatif untuk universitas di Eropa.
    ![](../assets/week%204/3.png)
dari hasil nslookup -type=NS ox.ac.uk (University of Oxford) terlihat ada 3 namaserver utama dan 3 authoritative server tambahan yang jika dijumlahkan jadi terdapat 6 dns.

3. Jalankan nslookup untuk mencari tahu informasi mengenai server email dari Yahoo! 
    ![](../assets/week%204/4.png)

Mail melalui salah satu server yang didapatkan di pertanyaan nomor 2. Apa alamat IP-nya?
    ![](../assets/week%204/5.png)
dari hasil di atas bisa kita lihat ipnya adalah 67.212.182.148

## C. Ipconfig
Ipconfig digunakan untuk menampilkan informasi konfigurasi TCP/IP yang sedang digunakan pada komputer, seperti alamat IP, alamat server DNS, jenis adaptor jaringan, dan informasi jaringan lainnya. Untuk melihat informasi lengkap mengenai konfigurasi jaringan host, Anda dapat menjalankan perintah ipconfig /all.
    ![](../assets/week%204/6.png)

Ipconfig juga dapat digunakan untuk mengelola informasi DNS yang tersimpan pada host. Untuk menampilkan seluruh record DNS yang tersimpan dalam cache, jalankan perintah ipconfig /displaydns pada terminal. Perintah ini akan menampilkan daftar entri DNS yang telah disimpan oleh sistem untuk mempercepat proses resolusi nama domain.
    ![](../assets/week%204/7.png)
Hasil dari perintah ipconfig /displaydns akan menampilkan daftar record DNS yang tersimpan beserta nilai Time To Live (TTL) dalam satuan detik. Untuk menghapus seluruh cache DNS, gunakan perintah ipconfig /flushdns. Perintah ini akan mengosongkan semua record DNS yang tersimpan dan memaksa sistem untuk memuat ulang informasi DNS dari file host maupun server DNS saat diperlukan.
    ![](../assets/week%204/8.png)

## Tracing DNS dengan Wireshark

Download file pada link berikut :  http://gaia.cs.umass.edu/wireshark-labs/wireshark-traces.zip

Selanjutnya, lakukan pengamatan untuk menjawab beberapa pertanyaan yang diberikan. Sebelum memulai, buka situs IETF (https://www.ietf.org/) pada browser.
    ![](../assets/week%204/9.png)
Setelah itu, jalankan Wireshark dan masukkan filter ip.addr == <your_IP_address>, dengan <your_IP_address> diganti menggunakan alamat IP yang diperoleh melalui perintah ipconfig. Filter ini akan menampilkan hanya paket yang berasal dari atau ditujukan ke host Anda. Untuk mempersempit hasil pengamatan pada proses resolusi DNS terkait situs IETF, tambahkan filter dns dan cari paket yang memuat kata ietf, sehingga hanya lalu lintas DNS yang berhubungan dengan domain IETF yang ditampilkan dan dianalisis.
    ![](../assets/week%204/10.png)

1. Cari pesan permintaan DNS dan balasannya. Apakah pesan tersebut dikirimkan melalui UDP atau TCP?
    ![](../assets/week%204/11.png)
terlihat pesantersebut dikirim melalui UDP (User Datagram Protocol)

2. Apa port tujuan pada pesan permintaan DNS? Apa port sumber pada pesan balasannya?
    ![](../assets/week%204/11.png)
bisa dilihat port tujuannya adalah 19332 dari source port57574

3. Pada pesan permintaan DNS, apa alamat IP tujuannya?
    ![](../assets/week%204/12.png)
    ![](../assets/week%204/13.png)
ya alamat ip tujuan dan server dns lokal sama.

4. Periksa pesan permintaan DNS. Apa “jenis” atau ”type” dari pesan tersebut? 
    ![](../assets/week%204/14.png)
dari hasil di atas bisa dilihat type A adalah jawabannya

5. Periksa pesan balasan DNS. Berapa banyak ”jawaban” atau ”answers” yang terdapat di dalamnya? Apa saja isi yang terkandung dalam setiap jawaban tersebut?
     ![](../assets/week%204/15.png)
Ada 3 jawaban, isi nya Name,Type,Class, TTL,Data Lenght, dan CNAME.

6. Perhatikan paket TCP SYN yang selanjutnya dikirimkan oleh host Anda. Apakah alamat IP pada paket tersebut sesuai dengan alamat IP yang tertera pada pesan balasan DNS?
    ![](../assets/week%204/16.png)
sudah sesuai dengan saat pengecekan nslookup alamat 107.167.96.30

7. Halaman web yang sebelumnya anda akses (http://www.ietf.org) memuat beberapa gambar. Apakah host Anda perlu mengirimkan pesan permintaan DNS baru setiap kali ingin mengakses suatu gambar?
    ![](../assets/week%204/17.png)
Tidak, karena saat pertama kali mengakses www.ietf.org, komputer melakukan proses lookup DNS untuk memperoleh alamat IP domain tersebut. Hasil lookup kemudian disimpan di dalam DNS cache lokal. Akibatnya, pada akses berikutnya komputer tidak perlu lagi mengirim permintaan ke server DNS karena alamat IP yang dibutuhkan sudah tersedia di cache, sehingga proses resolusi nama dapat dilakukan lebih cepat.

Selanjutnya adalah menjawab beberapa pertanyaan kembali sesuai dengan arahan modul yaitu mengabaikan dua pasangan permintaan-balasan pertama karena mereka merupakan paket yang khusus dihasilkan oleh nslookup. kita cukup fokus pada pesan permintaan dan balasan terakhir. berikut beberapa pertanyaan yang bisa dijawab yaitu.

Jawaban pertanyaan 2 nslookup -type=NS mit.edu

1. Ke alamat IP manakah pesan permintaan DNS dikirimkan? Apakah alamat IP tersebut merupakan default alamat IP server DNS lokal Anda?
    ![](../assets/week%204/18.png)

Berdasarkan gambar di samping, terlihat bahwa permintaan DNS dikirim ke alamat IP 192.168.18.1 melalui port 53, yang merupakan port standar untuk layanan DNS. Namun, alamat IP tersebut bukan merupakan alamat server DNS lokal yang ditampilkan pada konfigurasi jaringan komputer saya. Hal ini menunjukkan bahwa permintaan DNS kemungkinan diteruskan terlebih dahulu ke perangkat jaringan, seperti router atau gateway, yang kemudian meneruskan permintaan tersebut ke server DNS yang sebenarnya.

2. Periksa pesan permintaan DNS. Apa ”jenis” atau ”type” dari pesan tersebut? Apakah pesan tersebut mengandung ”jawaban” atau ”answers”?
    ![](../assets/week%204/19.png)
dari gambar di samping terlihat type dari pesan tersebut adalah queries, dengan tidak ada jawaban / jawaban langsung query

3. Periksa pesan balasan DNS. Apa nama server MIT yang diberikan oleh pesan balasan? Apakah pesan balasan ini juga memberikan alamat IP untuk server MIT tersebut?
    ![](../assets/week%204/20.png)
dari jawaban dns hanya mengembalikan Nameserver tidak dengan ip server.

Jawaban pertanyaan 3 nslookup www.aiitr.or.kr bitsy.mit.edu
nslookup www.aiit.or.kr bitsy.mit.edu
    ![](../assets/week%204/21.png)


1. Ke alamat IP manakah pesan permintaan DNS dikirimkan? Apakah alamat IP tersebut merupakan default alamat IP server DNS lokal Anda?
     ![](../assets/week%204/22.png)
dari gambar di samping terlihat pesan permintaan dikirim ke ip 192.168.68.52 dan itu merupakan default alamat ip server dns lokal saya

2. Periksa pesan permintaan DNS. Apa ”jenis” atau ”type” dari pesan tersebut? Apakah pesan tersebut mengandung ”jawaban” atau ”answers”?
    ![](../assets/week%204/23.png)
pesan dns tersebut bertype queries dengan tidak ada jawaban

3. Periksa pesan balasan DNS. Berapa banyak ”jawaban” atau “answers” yang terdapat di dalamnya. Apa saja isi yang terkandung dalam setiap jawaban tersebut?
    ![](../assets/week%204/24.png)
dari gambar di samping terlihat hanya ada satu jawaban yang dimana jawabannya berisi record dari bitsy.mit.edu serta additional records









