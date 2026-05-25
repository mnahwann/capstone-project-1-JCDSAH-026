from datetime import datetime  # mengambil fitur waktu/tanggal dari python

books = { #DataDummy berupa dictionary books: untuk menyimpan data buku perpus; Primary Key: kode buku; value: dictionary berisi detail buku
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

def show_all_books(): # Function Read: menampilkan seluruh data buku    
    if len(books) == 0: # cek apakah ada data
        print("Tidak Ada Data Buku!")
    else:
        print("\n=== DAFTAR BUKU ===")        
        for kode in books: # looping dictionary
            print(f"""
Kode Buku : {kode}
Judul     : {books[kode]['judul']}
Penulis   : {books[kode]['penulis']}
Stok      : {books[kode]['stok']}
Tahun     : {books[kode]['tahun']}
Genre     : {books[kode]['genre']}
            """)
def add_book(): # Function Create: menambahkan buku
    print("\n=== TAMBAH BUKU ===")    
    kode = input("Masukkan kode buku (0 untuk cancel): ").upper() # USER INPUT PRIMARY KEY # .upper()-> mengubah huruf yg diinput menjadi upper case
    if kode == "0":
        print("Penambahan buku dibatalkan.")
        return    
    if kode in books: # CEK DATA DUPLIKAT
        print("Data yang diinput sudah ada!")
    else:        
        judul = input("Masukkan judul buku: ") # USER INPUT DATA BUKU
        penulis = input("Masukkan nama penulis: ")
        stok = int(input("Masukkan stok buku: "))
        tahun = int(input("Masukkan tahun terbit:"))
        genre = input("Masukkan genre buku:")        
        checker = input("Apakah data ingin disimpan? (y/n): ").lower() # SAVE DATA CHECKER  # .lower()-> mengubah huruf yg diinput menjadi lower case
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
def update_book(): # Function Update: memperbarui buku
    print("\n=== PERBARUI DATA BUKU ===")    
    kode = input("Masukkan kode buku (0 untuk cancel): ").upper() # User input primary key
    if kode == "0":
        print("Pembaruan data buku dibatalkan.")
        return    
    if kode in books: # Cek ketersediaan data        
        print(f"""
Kode Buku : {kode}
Judul     : {books[kode]['judul']}
Penulis   : {books[kode]['penulis']}
Stok      : {books[kode]['stok']}
Tahun     : {books[kode]['tahun']}
Genre     : {books[kode]['genre']}
            """) # Tampilkan data terdahulu
                
        kolom = input("""
Kolom yang ingin diperbarui:
judul
penulis
stok
tahun
genre
Masukkan nama kolom: """).lower() # Pilih kolom yang mau di-update
        
        if kolom in books[kode]: # Validasi nama kolom            
            value_baru = input("Masukkan data baru: ") # Input value Baru            
            if kolom == "stok" or kolom == "tahun":
                value_baru = int(value_baru) # Casting Integer            
            checker = input("Apakah Anda ingin memperbarui data ini? (y/n): ").lower() # Checker Update
            if checker == "y":
                books[kode][kolom] = value_baru
                print("Data telah berhasil diperbarui.")
            else:
                print("Pembaruan data buku dibatalkan.")
        else:
            print("Kolom tidak valid!")
    else:
        print(
            "Kode buku yang anda cari tidak ditemukan,\nSilakan input kode buku yang valid!"
        )
def delete_book(): # Function Delete: menghapus entri buku
    print("\n=== HAPUS DATA BUKU ===")    
    kode = input("Masukkan kode buku yang ingin dihapus (0 untuk cancel): ").upper() # User input primary key
    if kode == "0":
        print("Penghapusan data dibatalkan.")
        return    
    if kode in books: # Cek ketersediaan data        
        print(f""" 
Kode Buku : {kode}
Judul     : {books[kode]['judul']}
Penulis   : {books[kode]['penulis']}
Stok      : {books[kode]['stok']}
Tahun     : {books[kode]['tahun']}
Genre     : {books[kode]['genre']}
            """) # Tampilkan data        
        checker = input("Apakah Anda yakin ingin menghapus data buku ini? (y/n): ").lower() # Checker Delete
        if checker == "y":
            del books[kode]
            print("Data buku telah berhasil dihapus.")
        else:
            print("Penghapusan data buku dibatalkan.")
    else:
        print(
            "Data buku yang anda cari tidak tersedia,\nSilakan input kode buku yang valid!"
        )
def borrow_book(): # Function Borrow: peminjaman buku
    print("\n=== PEMINJAMAN BUKU ===")    
    cart = [] # Cart Sementara    
    id_peminjam = input("Masukkan ID Peminjam: ")  # User input data peminjam
    nama_peminjam = input("Masukkan Nama Peminjam: ")    
    tanggal_pinjam = datetime.now() # Tanggal Pinjam
    while True:        
        show_all_books() # Tampilkan daftar buku        
        kode_buku = input("Masukkan kode buku yang ingin dipinjam: ").upper() # User input kode buku
        if kode_buku in books: # Validasi kode buku            
            if books[kode_buku]["stok"] > 0: # Cek Stok                
                if kode_buku in cart:
                    print("Buku sudah ada di keranjang!")
                else:
                    cart.append(kode_buku) # Masukkan ke cart
                    print("Buku berhasil dimasukkan ke keranjang peminjaman.")
            else:
                print("Stok buku habis!")
        else:
            print("Kode buku tidak ditemukan!")        
        lagi = input("Apakah Anda ingin menambah buku lain? (y/n): ").lower() # Tambah buku lagi?
        if lagi == "n":
            break
        elif lagi == "y":
            continue
        else:
            print("Input tidak valid!")
    while True:
        print("\n========= KERANJANG PEMINJAMAN =========") #Menampilkan isi cart
        for item in cart:
            print(f"""
    Kode Buku   : {item}
    Judul       : {books[item]['judul']}
                  """)
        cart_menu = input("""
1. Hapus Buku dari keranjang
2. Finalisasi Peminjaman
3. Batalkan Peminjaman      
                           """)
        if cart_menu == "1": #Hapus buku dari cart
            kode_hapus = input("Masukkan kode buku yang ingin dihapus dari keranjang: ").upper()
            if kode_hapus in cart:
                cart.remove(kode_hapus)
                print("Buku berhasil dihapus dari keranjang.")
            else:
                print("Anda hanya dapat menghapus buku yang telah dimasukkan ke keranjang!")
        elif cart_menu == "2": #Lanjut finalisasi peminjaman
            break
        elif cart_menu == "3": #Cancel peminjaman
            print("Peminjaman dibatalkan.")
            return
        else:
            print("Menu tidak valid!")    
    if len(cart) == 0: # Validasi cart kosong
        print("Tidak ada buku yang dipinjam.")
        return
    else:        
        checker = input("Finalisasi peminjaman? (y/n): ").lower() # Checker Finalisasi Peminjaman
        if checker == "y":
            for item in cart:
                books[item]["stok"] -= 1            
            print("\n=== STRUK PEMINJAMAN ===") # Cetak Struk peminjaman

            print(f"ID Peminjam    : {id_peminjam}")
            print(f"Nama           : {nama_peminjam}")
            print(f"Tanggal Pinjam : {tanggal_pinjam}")
            print("\nDaftar Buku:")            
            for item in cart: # Loop cart
                print(f"- {books[item]['judul']}")
            print("\nCatatan: ")
            print("- Batas Peminjaman buku adalah 7 hari.")
            print("- Keterlambatan pengembalian buku dikenakan denda sebesar Rp 10.000/hari.")
            print("- Menghilangkan atau merusak buku wajib mengganti sesuai harga buku asli!")
            print("\n=== TERIMA KASIH SUDAH MEMINJAM BUKU, SELAMAT MEMBACA! ===")
        else:
            print("Peminjaman dibatalkan.")
while True: # WhileTrue: digunakan agar program terus berjalan sampai user memilih exit  
    menu = input("""
                 
========= APLIKASI PEMINJAMAN BUKU PERPUSTAKAAN =========
                 
1. Tampilkan Koleksi Buku
2. Tambah Entri Data Buku Baru
3. Perbarui Entri Data Buku
4. Hapus Buku
5. Peminjaman Buku
6. Exit
                 
Silakan Pilih Menu Utama [1-6]: """) # user menginput menu-> user memilih menu aplikasi   
    if menu == "1": # MENU 1_READ: menampilkan seluruh data buku
        while True:
            read_menu = input("""
========= TAMPILKAN KOLEKSI BUKU =========
                              
1. Tampilkan Semua Buku
2. Cari Buku Berdasarkan Kode
3. Kembali Ke Menu Utama

Silakan Pilih Sub-Menu [1-3]: """)

            if read_menu == "1": # MENU 1_READ: menampilkan seluruh data buku
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
    elif menu == "2": # MENU 2_CREATE:menambahkan data buku baru ke dictionary books
        while True:
            create_menu = input("""
========= MENAMBAHKAN ENTRI DATA BUKU =========
                                
1. Tambah Buku Baru
2. Kembali ke Menu Utama
                                
Silakan Pilih Sub-Menu [1-2]: """)
            if create_menu == "1":
                add_book()
            elif create_menu == "2":
                break
            else:
                print("Menu tidak valid!")        
    elif menu == "3": # MENU 3_UPDATE: memperbarui/mengubah data buku
        while True:
            update_menu = input("""
========= PERBARUI ENTRI DATA BUKU =========
                                
1. Perbarui Data Buku
2. Kembali ke Menu Utama
                                
Silakan Pilih Sub-Menu [1-2]: """)
            if update_menu == "1":
                update_book()
            elif update_menu == "2":
                break
            else:
                print("Menu tidak valid!")        
    elif menu == "4": # MENU 4_DELETE: menghapus data buku dari dictionary
        while True:
            delete_menu = input("""
========= MENGHAPUS DATA BUKU =========
                                
1. Hapus Data Buku
2. Kembali ke Menu Utama
                                
Silakan Pilih Sub-Menu [1-2]: """)
            if delete_menu == "1":
                delete_book()
            elif delete_menu == "2":
                break
            else:
                print("Menu tidak valid!")        
    elif menu == "5": # MENU 5_ borrow_book -> proses peminjaman buku dari pov pustakawan selaku user yg memfasilitasi peminjam
        borrow_book()      
    elif menu == "6": # MENU 6_EXIT-> menghentikan program
        print("Program Ditutup. Terima Kasih.")
        break