## Laporan Prakktikum Jaringan Komputer Modul 7 Terkait SOCKET PROGRAMMING: MEMBUAT APLIKASI JARINGAN 

## Tujuan Praktikum
1. Mahasiswa bisa membuat program berbasis socket UDP
2. Mahasiswa bisa membuat program berbasis socket TCP


1. TCP Server (tcp-server.py)

Cara Kerja:

1.Server membuat socket menggunakan protokol TCP (SOCK_STREAM).
2.Server melakukan binding ke port 12000 agar dapat menerima koneksi dari client.
3.Server menjalankan fungsi listen() untuk menunggu koneksi masuk.
4.Ketika ada client yang terhubung, fungsi accept() akan membuat socket baru khusus untuk komunikasi dengan client tersebut.
5.Server menerima pesan dari client menggunakan recv().
6.Pesan yang diterima diubah menjadi huruf kapital menggunakan fungsi upper().
7.Hasilnya dikirim kembali ke client menggunakan send().
8.Jika client mengirim pesan "exit", server akan berhenti dan menutup socket.

2. TCP Client (tcp-client.py)

Cara Kerja:

1.Client membuat socket TCP menggunakan SOCK_STREAM.
2.Client melakukan koneksi ke server menggunakan connect().
3.Pengguna memasukkan pesan melalui keyboard.
4.Pesan dikirim ke server menggunakan send().
5.Client menunggu balasan dari server menggunakan recv().
6.Balasan dari server ditampilkan ke layar.
7.Jika pengguna mengetik "exit", client akan keluar dan menutup socket.   


3. UDP Server (udp-server.py)

Cara Kerja:

1.Server membuat socket UDP menggunakan SOCK_DGRAM.
2.Server melakukan binding pada port 12000.
3.Server menunggu paket data dari client menggunakan recvfrom().
4.Saat paket diterima, server mengambil isi pesan dan alamat pengirim.
5.Pesan diubah menjadi huruf kapital menggunakan upper().
6.Hasilnya dikirim kembali ke client menggunakan sendto().
7.Jika menerima pesan "exit", server akan berhenti dan menutup socket.


4. UDP Client (udp-client.py)

Cara Kerja:

1.Client membuat socket UDP menggunakan SOCK_DGRAM.
2.Pengguna memasukkan pesan melalui keyboard.
3.Pesan dikirim ke server menggunakan sendto().
4.Client menunggu balasan server menggunakan recvfrom().
5.Balasan yang diterima ditampilkan ke layar.
6.Jika pengguna mengetik "keluar", client akan ditutup.
7.Jika pengguna mengetik "exit", perintah dikirim ke server untuk mematikan server sekaligus menutup client.



Contoh Ouput
TCP
![](../assets/week%207/1.png)
![](../assets/week%207/2.png)

UDP
![](../assets/week%207/3.png)
![](../assets/week%207/4.png)