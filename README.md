# APLIKASI PERPUSTAKAAN

## 1. Deskripsi Aplikasi

Aplikasi Perpustakaan merupakan aplikasi desktop berbasis Python yang dirancang untuk membantu pengelolaan data perpustakaan secara terkomputerisasi. Aplikasi ini menggunakan konsep Model-View-Controller (MVC) untuk memisahkan pengelolaan data, tampilan antarmuka, dan proses pengendalian aplikasi.

Aplikasi ini menggunakan database MySQL sebagai tempat penyimpanan data dan CustomTkinter untuk membangun tampilan antarmuka. Dengan adanya aplikasi ini, proses pengelolaan data buku dapat dilakukan dengan lebih mudah dan terstruktur.

## 2. Struktur Direktori MVC

Struktur direktori proyek aplikasi perpustakaan adalah sebagai berikut:

```text
AplikasiPerpustakaan/
│
├── models/
│   └── buku_model.py
│
├── views/
│   └── buku_view.py
│
├── controllers/
│   └── buku_controller.py
│
├── tests/
│   ├── test_buku.py
│   └── test_auth.py
│
├── .github/
│   └── workflows/
│       └── ci_pipeline.yml
│
├── env/
├── dist/
├── build/
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

**Keterangan:**

- **Models:** Mengelola data dan komunikasi dengan database MySQL.
- **Views:** Mengatur tampilan antarmuka aplikasi menggunakan CustomTkinter.
- **Controllers:** Menghubungkan Models dan Views serta mengatur alur proses aplikasi.
- **Tests:** Menyimpan file pengujian untuk memastikan fungsi aplikasi berjalan dengan baik.
- **.github/workflows:** Menyimpan konfigurasi otomatisasi CI menggunakan GitHub Actions.
- **main.py:** File utama untuk menjalankan aplikasi.

## 3. Instalasi dan Konfigurasi Database MySQL

### A. Persiapan

Sebelum menjalankan aplikasi, pastikan perangkat telah memiliki:
1. Python.
2. Visual Studio Code.
3. Git.
4. Laragon.
5. MySQL.

### B. Mengaktifkan Database

1. Buka aplikasi Laragon.
2. Jalankan layanan MySQL.
3. Buka phpMyAdmin atau MySQL melalui terminal.
4. Buat database sesuai nama database yang digunakan dalam konfigurasi proyek.
5. Pastikan tabel yang dibutuhkan aplikasi sudah tersedia.

### C. Instalasi Dependensi

Buka terminal pada direktori proyek, kemudian jalankan:

```bash
python -m venv env
```

Aktifkan virtual environment pada Windows:

```bash
env\Scripts\activate
```

Instal seluruh dependensi:

```bash
pip install -r requirements.txt
```

## 4. Cara Menjalankan Aplikasi

Setelah proses instalasi selesai, lakukan langkah berikut:

1. Pastikan Laragon dan MySQL sudah berjalan.
2. Pastikan konfigurasi koneksi database sudah sesuai.
3. Aktifkan virtual environment.
4. Buka terminal pada direktori utama proyek.
5. Jalankan perintah:

```bash
python main.py
```

6. Tunggu hingga tampilan aplikasi perpustakaan muncul.

## 5. Pengujian Otomatis

Aplikasi menggunakan Pytest untuk menjalankan pengujian otomatis dan Flake8 untuk memeriksa kualitas penulisan kode.

Jalankan pengujian menggunakan:

```bash
pytest -v
```

Jalankan pemeriksaan kode menggunakan:

```bash
flake8 models/ controllers/ --count --select=E9,F63,F7,F82 --show-source --statistics
```

Proses CI juga dijalankan secara otomatis melalui GitHub Actions setiap kali terdapat perubahan kode yang dikirim ke repositori.

## 6. Pemaketan Aplikasi

Aplikasi dikemas menggunakan PyInstaller agar dapat dijalankan sebagai aplikasi desktop Windows tanpa harus menjalankan perintah Python secara manual.

Perintah pemaketan:

```bash
pyinstaller --noconfirm --onefile --windowed --name "AplikasiPerpustakaan" main.py
```

File aplikasi hasil pemaketan dapat ditemukan pada folder:

```text
dist/AplikasiPerpustakaan.exe
```

File tersebut dapat digunakan untuk menjalankan aplikasi pada komputer Windows dengan tetap memperhatikan kebutuhan database dan dependensi eksternal.