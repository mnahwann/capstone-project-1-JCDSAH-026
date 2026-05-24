from datetime import datetime  # mengambil fitur waktu/tanggal dari python

# DataDummy
# DictionaryBooks: untuk menyimpan data buku perpus
# key utama = kode buku
# value = dictionary berisi detail buku

books = {
    "BK001": {
        "judul": "Animal Farm",
        "penulis": "George Orwell",
        "stok": 5,
        "tahun": 2015,
        "genre": "Novel",
    },
    "BK002": {
        "judul": "Beyond Good and Evil: Prelude Menuju Filsafat Masa Depan",
        "penulis": "Friedrich Nietzsche",
        "stok": 2,
        "tahun": 2002,
        "genre": "Filsafat",
    },
    "BK003": {
        "judul": "Dan Kematian Makin Akrab",
        "penulis": "Subagio Sastrowardoyo",
        "stok": 1,
        "tahun": 1995,
        "genre": "Puisi",
    },
    "BK004": {
        "judul": "Derita Cinta Tak Terbalas: Proses Pencarian Makna Hidup",
        "penulis": "Stephanie Iriana",
        "stok": 5,
        "tahun": 2005,
        "genre": "Psikologi",
    },
    "BK005": {
        "judul": "Kita Hidup Hanya Sekali",
        "penulis": "Remy Sylado",
        "stok": 2,
        "tahun": 1977,
        "genre": "Novel",
    },
    "BK006": {
        "judul": "Melodia (Kumpulan Puisi 1959-2019)",
        "penulis": "Umbu Landu Paranggi",
        "stok": 3,
        "tahun": 2023,
        "genre": "Puisi",
    },
    "BK007": {
        "judul": "Risalah-Risalah",
        "penulis": "Al-Ghazali",
        "stok": 5,
        "tahun": 1997,
        "genre": "Tasawuf",
    },
    "BK008": {
        "judul": "Setelah Boombox Usai Menyalak",
        "penulis": "Herry Sutresna",
        "stok": 5,
        "tahun": 2016,
        "genre": "Musik",
    },
    "BK009": {
        "judul": "The Fall",
        "penulis": "Albert Camus",
        "stok": 4,
        "tahun": 2017,
        "genre": "Novel",
    },
    "BK010": {
        "judul": "Thinking, Fast and Slow",
        "penulis": "Daniel Kahneman",
        "stok": 5,
        "tahun": 2025,
        "genre": "Psikologi",
    },
}


# Function menampilkan seluruh data buku
def show_all_books():
    # cek apakah ada data
    if len(books) == 0:
        print("Tidak Ada Data Buku!")
    else:
        print("\n=== DAFTAR BUKU ===")

        # looping dictionary
        for kode in books:
            print(f"""
Kode Buku : {kode}
Judul     : {books[kode]['judul']}
Penulis   : {books[kode]['penulis']}
Stok      : {books[kode]['stok']}
Tahun     : {books[kode]['tahun']}
Genre     : {books[kode]['genre']}
            """)


# Function menambahkan buku
def add_book():
    print("\n=== TAMBAH BUKU ===")

    # USER INPUT PRIMARY KEY
    kode = input(
        "Masukkan kode buku (0 untuk cancel): "
    ).upper()  # .upper()-> mengubah huruf yg diinput menjadi upper case
    if kode == "0":
        print("Penambahan buku dibatalkan.")
        return

    # CEK DATA DUPLIKAT
    if kode in books:
        print("Data yang diinput sudah ada!")
    else:
        # USER INPUT DATA BUKU
        judul = input("Masukkan judul buku: ")
        penulis = input("Masukkan nama penulis: ")
        stok = int(input("Masukkan stok buku: "))
        tahun = int(input("Masukkan tahun terbit:"))
        genre = input("Masukkan genre buku:")

        # SAVE DATA CHECKER
        checker = input(
            "Apakah data ingin disimpan? (y/n)"
        ).lower()  # .lower()-> mengubah huruf yg diinput menjadi lower case
        if checker == "y":
            books[kode] = {
                "judul": judul,
                "penulis": penulis,
                "stok": stok,
                "tahun": tahun,
                "genre": genre,
            }
            print("Data telah berhasil disimpan.")
        else:
            print("Data batal disimpan.")


# Function Update Buku
def update_book():
    print("\n=== PERBARUI DATA BUKU ===")

    # User input primary key
    kode = input("Masukkan kode buku (0 untuk cancel): ").upper()
    if kode == "0":
        print("Pembaruan data buku dibatalkan.")
        return

    # Cek ketersediaan data
    if kode in books:

        # Tampilkan data terdahulu
        print(f"""
Kode Buku : {kode}
Judul     : {books[kode]['judul']}
Penulis   : {books[kode]['penulis']}
Stok      : {books[kode]['stok']}
Tahun     : {books[kode]['tahun']}
Genre     : {books[kode]['genre']}
            """)

        # Pilih kolom yang mau di-update
        kolom = input("""
Kolom yang ingin diperbarui:
judul
penulis
stok
tahun
genre
Masukkan nama kolom: """).lower()

        # Validasi nama kolom
        if kolom in books[kode]:

            # Input value Baru
            value_baru = input("Masukkan data baru: ")

            # Casting Integer
            if kolom == "stok" or kolom == "tahun":
                value_baru = int(value_baru)

            # Checker Update
            checker = input("Apakah Anda ingin memperbarui data ini? (y/n): ").lower()
            if checker == "y":
                books[kode][kolom] = value_baru
                print("Data telah berhasil diperbarui.")
            else:
                print("Pembaruan data buku dibatalkan.")
        else:
            print("Kolom tidak valid!")
    else:
        print(
            "Data buku yang anda cari tidak tersedia,\nSilakan input kode buku yang valid!"
        )


# FUNCTION menghapus entri buku
def delete_book():
    print("\n=== HAPUS DATA BUKU ===")

    # User input primary key
    kode = input("Masukkan kode buku yang ingin dihapus (0 untuk cancel): ").upper()
    if kode == "0":
        print("Penghapusan data dibatalkan.")
        return
    # Cek ketersediaan data
    if kode in books:

        # Tampilkan data
        print(f"""
Kode Buku : {kode}
Judul     : {books[kode]['judul']}
Penulis   : {books[kode]['penulis']}
Stok      : {books[kode]['stok']}
Tahun     : {books[kode]['tahun']}
Genre     : {books[kode]['genre']}
            """)

        # Checker Delete
        checker = input(
            "Apakah Anda yakin ingin menghapus data buku ini? (y/n): "
        ).lower()
        if checker == "y":
            del books[kode]
            print("Data buku telah berhasil dihapus.")
        else:
            print("Penghapusan data buku dibatalkan.")
    else:
        print(
            "Data buku yang anda cari tidak tersedia,\nSilakan input kode buku yang valid!"
        )


# Function Peminjaman Buku
def borrow_book():
    print("\n=== PEMINJAMAN BUKU ===")

    # Cart Sementara
    cart = []

    # User input data peminjam
    id_peminjam = input("Masukkan ID Peminjam: ")
    nama_peminjam = input("Masukkan Nama Peminjam: ")

    # Tanggal Pinjam
    tanggal_pinjam = datetime.now()

    while True:

        # Tampilkan daftar buku
        show_all_books()

        # User input kode buku
        kode_buku = input("Masukkan kode buku yang ingin dipinjam: ").upper()

        # Validasi kode buku
        if kode_buku in books:

            # Cek Stok
            if books[kode_buku]["stok"] > 0:

                # Masukkan ke cart
                cart.append(kode_buku)

                print("Buku berhasil dimasukkan ke keranjang peminjaman.")
            else:
                print("Stok buku habis!")
        else:
            print("Kode buku tidak ditemukan!")

        # Tambah buku lagi?
        lagi = input("Apakah Anda ingin menambah buku lain? (y/n): ").lower()
        if lagi == "n":
            break
        elif lagi == "y":
            continue
        else:
            print("Input tidak valid!")

    # Validasi cart kosong
    if len(cart) == 0:
        print("Tidak ada buku yang dipinjam.")

    else:
        # Checker Finalisasi Peminjaman
        checker = input("Finalisasi peminjaman? (y/n): ").lower()
        if checker == "y":
            for item in cart:
                books[item]["stok"] -= 1

            # Cetak Struk peminjaman
            print("\n=== STRUK PEMINJAMAN ===")

            print(f"ID Peminjam    : {id_peminjam}")
            print(f"Nama           : {nama_peminjam}")
            print(f"Tanggal Pinjam : {tanggal_pinjam}")

            print("\nDaftar Buku:")

            # Loop cart
            for item in cart:
                print(f"- {books[item]['judul']}")

            print("\nCatatan: ")
            print("- Batas Peminjaman buku adalah 7 hari.")
            print("- Denda Keterlambatan adalah Rp 10.000/hari.")
            print("- Menghilangkan atau merusak buku wajib mengganti sesuai harga buku")
            print("\n=== TERIMA KASIH SUDAH MEMINJAM BUKU, SELAMAT MEMBACA! ===")

        else:
            print("Peminjaman dibatalkan.")


# WhileTrue: digunakan agar program terus berjalan sampai user memilih exit
while True:
    # user menginput menu-> user memilih menu aplikasi

    menu = input("""
                 
=== APLIKASI PEMINJAMAN BUKU PERPUSTAKAAN ===
                 
1. Tampilkan Koleksi Buku
2. Tambah Buku
3. Perbarui Buku
4. Hapus Buku
5. Peminjaman Buku
6. Exit
                 
Pilih Menu: """)

    # MENU 1_READ: menampilkan seluruh data buku
    if menu == "1":
        while True:
            read_menu = input("""
=== MENU TAMPILKAN BUKU ===
1. Tampilkan Semua Buku
2. Cari Buku Berdasarkan Kode
3. Kembali Ke Menu Utama

Pilih Menu: """)

            if read_menu == "1":
                show_all_books()
            elif read_menu == "2":
                kode = input("Masukkan kode buku: ").upper()
                if kode in books:
                    print(f"""
Kode Buku : {kode}
Judul     : {books[kode]['judul']}
Penulis   : {books[kode]['penulis']}
Stok      : {books[kode]['stok']}
Tahun     : {books[kode]['tahun']}
Genre     : {books[kode]['genre']}
            """)
                else:
                    print("Kode buku tidak ditemukan!")
            elif read_menu == "3":
                break
            else:
                print("Menu tidak valid!")

        # MENU 2_CREATE:menambahkan data buku baru ke dictionary books
    elif menu == "2":
        while True:
            create_menu = input("""
=== MENU TAMBAH BUKU ===
                                
1. Tambah Buku Baru
2. Kembali ke Menu Utama
                                
Pilih menu: """)
            if create_menu == "1":
                add_book()
            elif create_menu == "2":
                break
            else:
                print("Menu tidak valid!")

        # MENU 3_UPDATE: mengubah data stok buku
    elif menu == "3":
        while True:
            update_menu = input("""
=== MENU UPDATE BUKU ===
                                
1. Update Data Buku
2. Kembali ke Menu Utama
                                
Pilih Menu: """)
            if update_menu == "1":
                update_book()
            elif update_menu == "2":
                break
            else:
                print("Menu tidak valid!")

        # MENU 4_DELETE: menghapus data buku dari dictionary
    elif menu == "4":
        while True:
            delete_menu = input("""
=== MENU HAPUS BUKU ===
                                
1. Hapus Data Buku
2. Kembali ke Menu Utama
                                
Pilih menu: """)
            if delete_menu == "1":
                delete_book()
            elif delete_menu == "2":
                break
            else:
                print("Menu tidak valid!")

        # PeminjamanBuku-> proses peminjaman buku oleh member perpustakaan
    elif menu == "5":
        borrow_book()

        # EXIT-> menghentikan program
    elif menu == "6":
        print("Program Ditutup. Terima Kasih.")
        break
