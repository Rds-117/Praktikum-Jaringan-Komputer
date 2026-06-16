# Laporan Modul 5 UDP

## A. Pengantar
UDP (User Datagram Protocol) adalah protokol pada lapisan transport yang digunakan untuk komunikasi data melalui jaringan komputer. UDP banyak dimanfaatkan pada aplikasi yang membutuhkan kecepatan transmisi tinggi dan toleran terhadap kehilangan data, seperti streaming video, komunikasi real-time, serta proses pencarian DNS. Berbeda dengan TCP, UDP tidak melakukan pemeriksaan koneksi maupun pengiriman ulang paket yang hilang, sehingga proses pengiriman data dapat berlangsung lebih cepat. Namun, konsekuensinya adalah paket data dapat hilang, tiba tidak berurutan, atau tidak sampai ke tujuan. Selain itu, karakteristik UDP yang ringan dan tidak memerlukan proses verifikasi koneksi juga dapat dimanfaatkan dalam beberapa jenis serangan jaringan, seperti Distributed Denial of Service (DDoS).

Anda dapat mengunduh file berisi trace penangkapan paket UDP yang telah disediakan (buka link http://gaia.cs.umass.edu/wireshark-labs/wireshark-traces.zip kemudian ekstrak file dengan nama http-ethereal-trace-5).
1. Pilih satu paket UDP yang terdapat pada trace Anda. Dari paket tersebut, berapa banyak “field” yang terdapat pada header UDP? Sebutkan nama-nama field yang Anda temukan!
    ![](../assets/week%205/1.png)
Berdasarkan gambar di samping, paket UDP yang dipilih memiliki empat field utama, yaitu Source Port, Destination Port, Length, dan Checksum. Source Port dan Destination Port menunjukkan port pengirim dan penerima, Length menunjukkan ukuran paket UDP, sedangkan Checksum digunakan untuk memeriksa integritas data selama transmisi.

2. Perhatikan informasi “content field” pada paket yang Anda pilih di pertanyaan 1. Berapa panjang (dalam satuan byte) masing-masing “field” yang terdapat pada header UDP?
Pada gambar terlihat header UDP memiliki empat field, yaitu Source Port, Destination Port, Length, dan Checksum. Karena ukuran total header UDP adalah 8 byte, maka masing-masing field memiliki panjang 2 byte (16 bit).

3. Nilai yang tertera pada ”Length” menyatakan nilai apa? Verfikasi jawaban Anda melalui paket UDP pada trace.
Field Length menyatakan panjang total segmen UDP yang terdiri dari header dan data (payload). Pada trace terlihat nilai Length = 58 byte dan UDP payload = 50 byte. Karena ukuran header UDP adalah 8 byte, maka:

58 byte = 8 byte (header) + 50 byte (payload)

Hal ini membuktikan bahwa nilai Length menunjukkan ukuran total segmen UDP.

4. Berapa jumlah maksimum byte yang dapat disertakan dalam payload UDP? (Petunjuk: jawaban untuk pertanyaan ini dapat ditentukan dari jawaban Anda untuk pertanyaan 2)

Field Length pada header UDP berukuran 16 bit, sehingga nilai maksimum yang dapat direpresentasikan adalah 65.535 byte. Karena header UDP selalu berukuran 8 byte, maka ukuran maksimum payload UDP adalah:

65.535 − 8 = 65.527 byte

Jadi, jumlah maksimum data yang dapat dimuat dalam payload UDP adalah 65.527 byte.

5. Berapa nomor port terbesar yang dapat menjadi port sumber? (Petunjuk: lihat petunjuk pada pertanyaan 4)

Pada gambar terlihat nilai Source Port = 4334, namun karena field port pada UDP berukuran 16 bit, maka rentang nilai port yang dapat digunakan adalah 0–65.535. Dengan demikian, nomor port terbesar yang dapat menjadi port sumber adalah 65.535.

6. Berapa nomor protokol untuk UDP? Berikan jawaban Anda dalam notasi heksadesimal dan desimal. Untuk menjawab pertanyaan ini, Anda harus melihat ke bagian ”Protocol” pada datagram IP yang mengandung segmen UDP.
    ![](../assets/week%205/2.png)
erdasarkan gambar di samping, terlihat bahwa nilai Protocol pada header IP untuk paket UDP adalah 17 dalam notasi desimal. Jika dilihat pada representasi heksadesimal di sisi kanan, nilai tersebut ditampilkan sebagai 0x11. Dengan demikian, angka 17 dan 0x11 sama-sama menunjukkan bahwa paket tersebut menggunakan protokol UDP.

7. Periksa pasangan paket UDP di mana host Anda mengirimkan paket UDP pertama dan paket UDP kedua merupakan balasan dari paket UDP yang pertama. (Petunjuk: agar paket kedua merupakan balasan dari paket pertama, pengirim paket pertama harus menjadi tujuan dari paket kedua). Jelaskan hubungan antara nomor port pada kedua paket tersebut!
    ![](../assets/week%205/3.png)
Berdasarkan gambar di samping, tanda panah menunjukkan arah komunikasi antara pengirim dan penerima. Panah ke kanan menandakan adanya permintaan (request) yang dikirim dari host lokal 192.168.1.102 menuju 192.168.1.104. Sebaliknya, panah ke kiri menunjukkan adanya respons (response) yang dikirim dari 192.168.1.104 kembali ke host 192.168.1.102 sebagai balasan atas permintaan yang sebelumnya diterima.