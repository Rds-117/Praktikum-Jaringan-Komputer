# Laporan Praktikum Modul 6 TCP

## Tujuan Praktikum
1. Mahasiswa dapat menganalisis cara kerja protokol TCP menggunakan aplikasi Wireshark.

## Menangkap Tansfer TCP dalam Jumlah Besar dari Komputer Pribadi ke Remote Server 

Steps:

1. Jalankan peramban web, kemudian akses http://gaia.cs.umass.edu/wireshark-labs/alice.txt untuk mengunduh salinan teks ASCII dari naskah Alice in Wonderland. Setelah proses unduhan selesai, simpan file tersebut pada komputer untuk digunakan dalam kegiatan praktikum selanjutnya.
2. Selanjutnya buka http://gaia.cs.umass.edu/wireshark-labs/TCP-wireshark-file1.html .
3. Anda akan melihat tampilan layar seperti gambar di bawah:
    ![](../assets/week%206/1.png)


4. Gunakan tombol Browse untuk memilih file Alice in Wonderland yang telah disimpan pada komputer dengan menyertakan lokasi atau path lengkap file tersebut. Setelah file berhasil dipilih, jangan menekan tombol “Upload alice.txt file” terlebih dahulu, karena langkah tersebut akan dilakukan pada tahap berikutnya.
5. Setelah itu, jalankan Wireshark dan mulai penangkapan paket
6. Kembali ke peramban web, kemudian tekan tombol “Upload file alice.txt” untuk
7. Hentikan penangkapan paket pada Wireshark. Jendela Wireshark Anda akan terlihat seperti gambar di bawah.
    ![](../assets/week%206/2.png)
8. file telah berhasil di unggah


## Tampilan Awal pada Captured Trace
Jawablah pertanyaan-pertanyaan berikut dengan menganalisis paket yang tertangkap pada trace tcp- ethereal-trace-1

 1. Berapa alamat IP dan nomor port TCP yang digunakan oleh komputer klien (sumber) untuk mentransfer file ke gaia.cs.umass.edu? Cara paling mudah menjawab pertanyaan ini adalah dengan memilih sebuah pesan HTTP dan meneliti detail paket TCP yang digunakan untuk membawa pesan HTTP tersebut.
 ![](../assets/week%206/3.png)
 Alamat IP komputer klien adalah **192.168.68.52** dan port TCP sumber yang digunakan adalah **63887**, seperti terlihat pada paket HTTP nomor 1409 menuju server 128.119.245.12.
 2. Apa alamat IP dari gaia.cs.umass.edu? Pada nomor port berapa ia mengirim dan menerima segmen TCP untuk koneksi ini? 
  ![](../assets/week%206/4.png)
  Ip = **192.168.68.52** dan port = **80**

3. Berapa alamat IP dan nomor port TCP yang digunakan oleh komputer klien Anda (sumber) untuk mentransfer ke gaia.cs.umass.edu?
 ![](../assets/week%206/3.png)
 Source: 192.168.68.52 : 63887 Destination : 128.119.245.12 : 80

## Dasar TCP
kita akan menggunakan trace paket yang telah Anda tangkap untuk mempelajari sifat TCP dari paket tcp-ethereal-trace-1.
    ![](../assets/week%206/5.png)

Jawablah beberapa pertanyaan berikut untuk segmen TCP:

1. Berapa nomor urut segmen TCP SYN yang digunakan untuk memulai sambungan TCP antara komputer klien dan gaia.cs.umass.edu? Apa yang dimiliki segmen tersebut sehingga teridentifikasi sebagai segmen SYN?
    ![](../assets/week%206/6.png)
Berdasarkan gambar di atas, nilai SYN = 1 dan ACK = 0 menunjukkan bahwa segmen tersebut adalah paket SYN untuk memulai koneksi TCP. Paket ini merupakan tahap pertama dalam proses Three-Way Handshake.

2. Berapa nomor urut segmen SYNACK yang dikirim oleh gaia.cs.umass.edu ke komputer klien sebagai balasan dari SYN? Berapa nilai dari field Acknowledgement pada segmen SYNACK? Bagaimana gaia.cs.umass.edu menentukan nilai tersebut? Apa yang dimiliki oleh segmen sehingga teridentifikasi sebagai segmen SYNACK?

     ![](../assets/week%206/6.png)
Nomor urut SYNACK tidak dapat ditentukan dari tangkapan yang diberikan karena paket balasan dari server tidak ditampilkan. Namun secara umum, field Acknowledgment pada SYNACK akan bernilai nomor urut SYN klien (4113720497) ditambah 1, dan segmen dikenali sebagai SYNACK jika flag SYN dan ACK sama-sama bernilai 1 (0x012).

3. Berapa nomor urut segmen TCP yang berisi perintah HTTP POST? Perhatikan bahwa untuk menemukan perintah POST, Anda harus menelusuri content field milik paket di bagian bawah jendela Wireshark, kemudian cari segmen yang berisi "POST" di bagian field DATAnya.
    ![](../assets/week%206/7.png)
Nilai Seq: 94009 adalah sequence number (relative) dari segmen tersebut, yang merupakan awal dari data HTTP POST yang dikirimkan.

4. Anggap segmen TCP yang berisi HTTP POST sebagai segmen pertama dalam koneksi TCP. Berapa nomor urut dari enam segmen pertama dalam TCP (termasuk segmen yang berisi HTTP POST)? Pada jam berapa setiap segmen dikirim? Kapan ACK untuk setiap segmen diterima? Dengan adanya perbedaan antara kapan setiap segmen TCP dikirim dan kapan acknowledgement-nya diterima, berapakah nilai RTT untuk keenam segmen tersebut? Berapa nilai EstimatedRTT setelah penerimaan setiap ACK? (Catatan: Wireshark memiliki fitur yang memungkinkan Anda untuk memplot RTT untuk setiap segmen TCP yang dikirim. Pilih segmen TCP yang dikirim dari klien ke server gaia.cs.umass.edu pada jendela "daftar paket yang ditangkap". Kemudian pilih: Statistics->TCP Stream Graph- >Round Trip Time Graph).
    ![](../assets/week%206/8.png)
Berdasarkan gambar di bawah, nomor urut pada enam segmen pertama berada di kisaran 7865 dan meningkat sesuai urutan pengiriman segmen. Selain itu, terdapat informasi Round Trip Time, yaitu waktu yang dibutuhkan segmen untuk menerima balasan ACK. Nilai RTT diperoleh dari selisih antara waktu ACK diterima dan waktu segmen dikirim, yang pada kasus ini sekitar 300 ms. Nilai tersebut kemudian digunakan sebagai dasar dalam perhitungan Estimated RTT.
    ![](../assets/week%206/9.png)

5. Berapa panjang setiap enam segmen TCP pertama?
Berdasarkan data pada gambar, panjang data TCP pertama diperoleh dari penjumlahan ukuran data pada segmen-segmen yang dikirim, yaitu 565 byte dan 1460 byte. Nilai Sequence Number kemudian bertambah sesuai jumlah byte data yang telah dikirim, sehingga urutan segmen berikutnya dapat dihitung berdasarkan total ukuran data sebelumnya. Dengan demikian, nilai nomor urut yang terlihat berada di sekitar 7865 sesuai dengan akumulasi data yang telah ditransmisikan.

6. Berapa jumlah minimum ruang buffer tersedia yang disarankan kepada penerima dan diterima untuk seluruh trace? Apakah kurangnya ruang buffer penerima pernah menghambat pengiriman?
    ![](../assets/week%206/10.png)
minimum ruang buffer 62780, tidak karena tidak berpengaruh pada kecepatan pengiriman

7. Apakah ada segmen yang ditransmisikan ulang dalam file trace? Apa yang anda periksa (di dalam file trace) untuk menjawab pertanyaan ini?
     ![](../assets/week%206/11.png)
tidak ada

8. Berapa banyak data yang biasanya diakui oleh penerima dalam ACK? Dapatkah anda mengidentifikasi kasus-kasus di mana penerima melakukan ACK untuk setiap segmen yang diterima?
     ![](../assets/week%206/12.png)
jika nilai ACK berubah dari 7866 menjadi 14619, maka jumlah data yang telah diterima adalah 14619 − 7866 = 6753 byte. Dengan demikian, dapat disimpulkan bahwa penerima telah berhasil menerima dan mengonfirmasi sebanyak 6753 byte data.

9. Berapa throughput (byte yang ditransfer per satuan waktu) untuk sambungan TCP? Jelaskan bagaimana Anda menghitung nilai ini.
    ![](../assets/week%206/13.png)
Nilai throughput yang tertera pada grafik adalah 200 kbps, yang dihitung dari total byte yang ditransfer dibagi dengan waktu total transfer, lalu dikonversi ke kilobit per detik (1 byte = 8 bit, 1 kB = 1024 byte).  

## Congestion Control pada TCP

Gunakan alat plotting Time-Sequence-Graph (Stevens) untuk melihat grafik nomor urut berbanding waktu dari segmen yang dikirim oleh klien ke server gaia.cs.umass.edu. Dapatkah Anda mengidentifikasi di mana fase “slow start” TCP dimulai dan berakhir, dan pada bagian mana algoritma ”congestion avoidance” mengambil alih? Berikan komentar tentang bagaimana data yang diukur berbeda dari perilaku ideal TCP yang telah kita pelajari.
    ![](../assets/week%206/14.png)
dari grafik di atas terlihat adanya slow start



  


