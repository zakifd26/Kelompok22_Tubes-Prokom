import tkinter as tk
from PIL import ImageTk, Image
import csv
from tkinter import messagebox
import random
import string
import datetime

def welcome_message():
    new_window = tk.Toplevel(window)
    new_window.title("ToneTix")
    new_window.geometry("600x400")

    welcome_label = tk.Label(new_window, text="SELAMAT DATANG DI TONETIX!", font=("Arial", 18, "bold"))
    welcome_label.pack()

    description_label = tk.Label(new_window, text="Kami adalah platform penjualan tiket konser terbaik untukmu!", font=("Arial", 14), fg="red")
    description_label.pack()

    additional_label = tk.Label(new_window, text="Tonetix menyediakan tiket konser untuk berbagai genre musik populer,\n dengan kualitas suara dan pengalaman konser yang tak terlupakan.\n Dengan Tonetix, Anda dapat menjelajahi dan membeli tiket untuk konser-konser terbaik\n dari musisi dan band favorit Anda.", font=("Arial", 10))
    additional_label.pack()

    genre_label = tk.Label(new_window, text="Pilih nomor genre musik yang Anda minati:", font=("Arial", 12, "bold"))
    genre_label.pack()

    genre_options = [
        "Jazz",
        "Rock",
        "Pop",
        "Dangdut"
    ]

    for i, option in enumerate(genre_options, start=1):
        genre_button = tk.Button(new_window, text=f"{i}. {option}", width=12, bg="grey", fg="white", command=lambda opt=option: genre_selected(opt, new_window))
        genre_button.pack(pady=3)

    exit_button = tk.Button(new_window, text="Keluar", width=12, bg="red", fg="white", command=keluar)
    exit_button.pack()

    additional_label2 = tk.Label(new_window, text="\nUntuk membeli tiket, silakan pilih nomor genre musik yang Anda minati.\nKami akan membantu Anda mendapatkan pengalaman konser yang luar biasa!", font=("Arial", 10))
    additional_label2.pack()

def genre_selected(genre, window):
    if genre == "Jazz":
        show_jazz_concerts(window)
    elif genre == "Rock":
        show_rock_concerts(window)
    elif genre == "Pop":
        show_pop_concerts(window)
    elif genre == "Dangdut":
        show_dangdut_concerts(window)
    elif genre == "Keluar":
        keluar()

def show_jazz_concerts(window):
    new_window = tk.Toplevel(window)
    new_window.title("Daftar Konser Jazz")
    new_window.geometry("600x400")

    canvas = tk.Canvas(new_window)
    scrollbar = tk.Scrollbar(new_window, orient="vertical", command=canvas.yview)
    concert_frame = tk.Frame(canvas)

    concert_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=concert_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    with open('konser_jazz.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        print()
        count = 1
        concerts = []  
        for row in reader:
            concerts.append(row)
            concert_label = tk.Label(concert_frame, text=f"\nNomor Konser: {count}\nNama Konser: {row[0]}\nVenue: {row[1]}\nLokasi: {row[2]}\nTanggal: {row[3]}\nHarga:\n - VIP: Rp. {row[7]}\n       - Reguler: Rp. {row[8]}\n", font=("Arial", 12,"bold"), justify="center")
            concert_label.pack()
            concert_button = tk.Button(concert_frame, text="Pilih", width=12, bg="grey", fg="white", font=("Arial", 10), command=lambda info=row: buy_ticket(info))
            concert_button.pack()
            count += 1
        
        back_button = tk.Button(new_window, text="Kembali", width=12, bg="red", fg="white", command=lambda: back_to_welcome(new_window))
        back_button.pack() 

def show_rock_concerts(window):
    new_window = tk.Toplevel(window)
    new_window.title("Daftar Konser Rock")
    new_window.geometry("600x400")

    canvas = tk.Canvas(new_window)
    scrollbar = tk.Scrollbar(new_window, orient="vertical", command=canvas.yview)
    concert_frame = tk.Frame(canvas)

    concert_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=concert_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    with open('konser_rock.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        print()
        count = 1
        concerts = []  
        for row in reader:
            concerts.append(row)
            concert_label = tk.Label(concert_frame, text=f"\nNomor Konser: {count}\nNama Konser: {row[0]}\nVenue: {row[1]}\nLokasi: {row[2]}\nTanggal: {row[3]}\nHarga:\n - VIP: Rp. {row[7]}\n       - Reguler: Rp. {row[8]}\n", font=("Arial", 12,"bold"), justify="center")
            concert_label.pack()
            concert_button = tk.Button(concert_frame, text="Pilih", width=12, bg="grey", fg="white",font=("Arial", 10), command=lambda info=row: buy_ticket(info))
            concert_button.pack()
            count += 1
        
        back_button = tk.Button(new_window, text="Kembali", width=12, bg="red", fg="white", command=lambda: back_to_welcome(new_window))
        back_button.pack() 

def show_pop_concerts(window):
    new_window = tk.Toplevel(window)
    new_window.title("Daftar Konser Pop")
    new_window.geometry("600x400")

    canvas = tk.Canvas(new_window)
    scrollbar = tk.Scrollbar(new_window, orient="vertical", command=canvas.yview)
    concert_frame = tk.Frame(canvas)

    concert_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=concert_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    with open('konser_pop.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        print()
        count = 1
        concerts = [] 
        for row in reader:
            concerts.append(row)
            concert_label = tk.Label(concert_frame, text=f"\nNomor Konser: {count}\nNama Konser: {row[0]}\nVenue: {row[1]}\nLokasi: {row[2]}\nTanggal: {row[3]}\nHarga:\n - VIP: Rp. {row[7]}\n       - Reguler: Rp. {row[8]}\n", font=("Arial", 12,"bold"), justify="center")
            concert_label.pack()
            concert_button = tk.Button(concert_frame, text="Pilih", width=12, bg="grey", fg="white", font=("Arial", 10), command=lambda info=row: buy_ticket(info))
            concert_button.pack()
            count += 1
        
        back_button = tk.Button(new_window, text="Kembali", width=12, bg="red", fg="white", command=lambda: back_to_welcome(new_window))
        back_button.pack() 

def show_dangdut_concerts(window):
    new_window = tk.Toplevel(window)
    new_window.title("Daftar Konser Dangdut")
    new_window.geometry("600x400")

    canvas = tk.Canvas(new_window)
    scrollbar = tk.Scrollbar(new_window, orient="vertical", command=canvas.yview)
    concert_frame = tk.Frame(canvas)

    concert_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=concert_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    with open('konser_dangdut.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        print()
        count = 1
        concerts = []  
        for row in reader:
            concerts.append(row)
            concert_label = tk.Label(concert_frame, text=f"\nNomor Konser: {count}\nNama Konser: {row[0]}\nVenue: {row[1]}\nLokasi: {row[2]}\nTanggal: {row[3]}\nHarga:\n - VIP: Rp. {row[7]}\n       - Reguler: Rp. {row[8]}\n", font=("Arial", 12,"bold"), justify="center")
            concert_label.pack()
            concert_button = tk.Button(concert_frame, text="Pilih", width=12, bg="grey", fg="white", font=("Arial", 10), command=lambda info=row: buy_ticket(info))
            concert_button.pack()
            count += 1
        
        back_button = tk.Button(new_window, text="Kembali", width=12, bg="red", fg="white", command=lambda: back_to_welcome(new_window))
        back_button.pack() #baru ini yang diedit

def buy_ticket(concert_info):
    line_up_window = tk.Toplevel()
    line_up_window.title("Line-up Konser")
    line_up_window.geometry("600x400")

    label_font = ("Arial", 16, "bold")
    
    label_lineup1 = tk.Label(line_up_window, text=f"\nLine-up 1:\n{concert_info[4]}", font=label_font, justify="center")
    label_lineup1.pack(pady=10)
    label_lineup2 = tk.Label(line_up_window, text=f"\nLine-up 2:\n{concert_info[5]}", font=label_font, justify="center")
    label_lineup2.pack(pady=10)
    label_lineup3 = tk.Label(line_up_window, text=f"\nLine-up 3:\n{concert_info[6]}", font=label_font, justify="center")
    label_lineup3.pack(pady=10)
    
    # Membuat frame untuk tombol
    button_frame = tk.Frame(line_up_window)
    button_frame.pack(pady=25)
    
    # Membuat tombol untuk membeli tiket
    buy_button = tk.Button(button_frame, text="Beli Tiket", width=12, font=("Arial", 10), command=lambda: buy_ticket_confirmation(concert_info))
    buy_button.grid(row=0, column=0, padx=(0, 10))

    back_button = tk.Button(button_frame, text="Kembali", width=12, font=("Arial", 10), bg="red", fg="white", command=lambda: back_to_welcome(window))
    back_button.grid(row=0, column=1, padx=(10, 0))
    
 
    
def buy_ticket_confirmation(concert_info):
    # Menampilkan konfirmasi pembelian tiket
    confirmation_window = tk.Toplevel()
    confirmation_window.title("Konfirmasi Pembelian Tiket")
    confirmation_window.geometry("600x100")
    
    confirmation_label = tk.Label(confirmation_window, text="Apakah Anda ingin membeli tiket?", font=("Arial", 12))
    confirmation_label.pack(pady=20)
    
    # Membuat frame untuk tombol
    button_frame = tk.Frame(confirmation_window)
    button_frame.pack()
    
    def show_ticket_prices():
        ticket_prices_window = tk.Toplevel()
        ticket_prices_window.title("Harga Tiket")
        ticket_prices_window.geometry("600x300")

        vip_price_label = tk.Label(ticket_prices_window, text="\nHarga Tiket VIP:\n Rp {}".format(concert_info[7]), font=("Arial", 12))
        vip_price_label.pack(pady=10)

        regular_price_label = tk.Label(ticket_prices_window, text="Harga Tiket Reguler:\n Rp {}".format(concert_info[8]), font=("Arial", 12))
        regular_price_label.pack(pady=10)

        ticket_selection_label = tk.Label(ticket_prices_window, text="Pilih tiket yang ingin Anda beli:", font=("Arial", 12,"bold"))
        ticket_selection_label.pack(pady=10)

        # Membuat frame untuk tombol tiket
        ticket_button_frame = tk.Frame(ticket_prices_window)
        ticket_button_frame.pack()

        vip_ticket_button = tk.Button(ticket_button_frame, text="Tiket VIP", width=12, command=purchase_vip_ticket)
        vip_ticket_button.pack(side=tk.LEFT, padx=10)

        # Tombol untuk membeli tiket reguler
        regular_ticket_button = tk.Button(ticket_button_frame, text="Tiket Reguler", width=12, command=purchase_regular_ticket)
        regular_ticket_button.pack(side=tk.LEFT, padx=10)


    def purchase_vip_ticket():
        def cancel_purchase():
            purchase_window.destroy()

        purchase_window = tk.Toplevel()
        purchase_window.title("Pembelian Tiket VIP")
        purchase_window.geometry("600x400")

        nama_label = tk.Label(purchase_window, text="Nama:")
        nama_label.pack()
        nama_entry = tk.Entry(purchase_window, width=30)
        nama_entry.pack()

        nik_label = tk.Label(purchase_window, text="NIK:")
        nik_label.pack()
        nik_entry = tk.Entry(purchase_window, width=30)
        nik_entry.pack()

        email_label = tk.Label(purchase_window, text="Email:")
        email_label.pack()
        email_entry = tk.Entry(purchase_window, width=30)
        email_entry.pack()

        nomor_rekening_label = tk.Label(purchase_window, text="Nomor Rekening:")
        nomor_rekening_label.pack()
        nomor_rekening_entry = tk.Entry(purchase_window, width=30)
        nomor_rekening_entry.pack()

        jumlah_tiket_label = tk.Label(purchase_window, text="Jumlah Tiket:")
        jumlah_tiket_label.pack()
        jumlah_tiket_entry = tk.Entry(purchase_window, width=30)
        jumlah_tiket_entry.pack()

        def generate_kode_unik(length=9):
            characters = string.ascii_letters + string.digits
            kode_unik = ''
            for _ in range(length):
                if len(kode_unik) < length - 1:
                    kode_unik += random.choice(characters)
                else:
                    kode_unik += random.choice(string.digits)
            return kode_unik
        
        def lihat_tiket():
            tiket_window = tk.Toplevel()
            tiket_window.title("Tiket")
            tiket_window.geometry("600x350")
            tiket_window.configure(bg="skyblue")

            tiket_label = tk.Label(tiket_window, text="Tiket Anda", bg="skyblue", font=("Arial", 16, "bold"))
            tiket_label.pack(pady=10)

            nama = nama_entry.get()
            nik = nik_entry.get()
            email = email_entry.get()
            jumlah_tiket = int(jumlah_tiket_entry.get())
            kode_unik = generate_kode_unik()

            nama_label = tk.Label(tiket_window, text="Nama : {}".format(nama), bg="skyblue", font=("Arial", 12))
            nama_label.pack(pady=5, anchor="w")

            nik_label = tk.Label(tiket_window, text="NIK : {}".format(nik), bg="skyblue", font=("Arial", 12))
            nik_label.pack(pady=5, anchor="w")

            email_label = tk.Label(tiket_window, text="Email : {}".format(email), bg="skyblue", font=("Arial", 12))
            email_label.pack(pady=5, anchor="w")

            jumlah_tiket_label = tk.Label(tiket_window, text="Jumlah Tiket : {}".format(jumlah_tiket), bg="skyblue", font=("Arial", 12))
            jumlah_tiket_label.pack(pady=5, anchor="w")

            kode_unik_label = tk.Label(tiket_window, text="Kode Tiket : {}".format(kode_unik), bg="skyblue", font=("Arial", 12, "bold"))
            kode_unik_label.pack(pady=5, anchor="w") 

            printout_label = tk.Label(tiket_window, text="Silahkan tunjukkan E-Ticket ini di loket pembelian tiket untuk mendapatkan tiket Anda. \nTerima kasih. Selamat menikmati konser!", bg="skyblue", font=("Arial", 10, "italic"))
            printout_label.pack(pady=10)

            exit_button = tk.Button(tiket_window, text="Exit", width=12, bg="red", fg="white", command=keluar)
            exit_button.pack(pady=10)

        def submit_purchase():
            nama = nama_entry.get()
            nik = nik_entry.get()
            email = email_entry.get()
            nomor_rekening = nomor_rekening_entry.get()
            jumlah_tiket = int(jumlah_tiket_entry.get())
            tanggal_waktu = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            with open('pembelian_tiket.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([tanggal_waktu, nama, nik, email, nomor_rekening, jumlah_tiket,"VIP"])

            harga_tiket = int(concert_info[8])
            total_harga = harga_tiket * jumlah_tiket

            total_harga_label = tk.Label(purchase_window, text="Total Harga: Rp {}".format(total_harga), font=("Arial", 12, "bold"))
            total_harga_label.pack()

            nominal_pembayaran_label = tk.Label(purchase_window, text="Nominal Pembayaran : (Rp.) ")
            nominal_pembayaran_label.pack()

            nominal_pembayaran_entry = tk.Entry(purchase_window)
            nominal_pembayaran_entry.pack()

            def submit_payment():
                nominal_pembayaran = int(nominal_pembayaran_entry.get())

                if nominal_pembayaran == total_harga:
                    payment_success_window = tk.Toplevel()
                    payment_success_window.title("Pembayaran Berhasil")
                    payment_success_window.geometry("400x200")

                    success_label = tk.Label(payment_success_window, text="\nPembayaran telah diselesaikan.",font=("Arial", 12, "bold"))
                    success_label.pack()

                    lihat_tiket_button = tk.Button(payment_success_window, text="Lihat Tiket", width=12, command=lihat_tiket)
                    lihat_tiket_button.pack(side="bottom", anchor="s", pady=10)

                elif nominal_pembayaran > total_harga:
                    kembalian = nominal_pembayaran - total_harga
                    payment_success_window = tk.Toplevel()
                    payment_success_window.title("Pembayaran Berhasil")
                    payment_success_window.geometry("400x200")

                    success_label = tk.Label(payment_success_window, text="\nPembayaran telah diselesaikan.\nKembalian: Rp {}, \nKembalian akan dikirim ke Nomor Rekening Anda".format(kembalian),font=("Arial", 12, "bold"))
                    success_label.pack()

                    lihat_tiket_button = tk.Button(payment_success_window, text="Lihat Tiket", width=12, command=lihat_tiket)
                    lihat_tiket_button.pack(side="bottom", anchor="s", pady=10)
                else:
                    retry_payment_window = tk.Toplevel()
                    retry_payment_window.title("Pembayaran Belum Selesai")
                    retry_payment_window.geometry("400x200")

                    retry_label = tk.Label(retry_payment_window, text="\nPembayaran belum selesai.\n Mohon masukkan nominal pembayaran yang sesuai.",font=("Arial", 12, "bold"))
                    retry_label.pack()


            submit_button = tk.Button(purchase_window, text="Submit Pembayaran", width=20, command=submit_payment)
            submit_button.pack(pady=10)

        button_frame = tk.Frame(purchase_window)
        button_frame.pack(pady=10)

        submit_button = tk.Button(button_frame, text="Beli", width=12, command=submit_purchase)
        submit_button.pack(side=tk.LEFT, padx=5)

        cancel_button = tk.Button(button_frame, text="Cancel",bg="red", fg="white", width=12, command=cancel_purchase)
        cancel_button.pack(side=tk.LEFT, padx=5)
    

    def purchase_regular_ticket():
        def cancel_purchase():
            purchase_window.destroy()

        purchase_window = tk.Toplevel()
        purchase_window.title("Pembelian Tiket VIP")
        purchase_window.geometry("600x400")

        nama_label = tk.Label(purchase_window, text="Nama:")
        nama_label.pack()
        nama_entry = tk.Entry(purchase_window, width=30)
        nama_entry.pack()

        nik_label = tk.Label(purchase_window, text="NIK:")
        nik_label.pack()
        nik_entry = tk.Entry(purchase_window, width=30)
        nik_entry.pack()

        email_label = tk.Label(purchase_window, text="Email:")
        email_label.pack()
        email_entry = tk.Entry(purchase_window, width=30)
        email_entry.pack()

        nomor_rekening_label = tk.Label(purchase_window, text="Nomor Rekening:")
        nomor_rekening_label.pack()
        nomor_rekening_entry = tk.Entry(purchase_window, width=30)
        nomor_rekening_entry.pack()

        jumlah_tiket_label = tk.Label(purchase_window, text="Jumlah Tiket:")
        jumlah_tiket_label.pack()
        jumlah_tiket_entry = tk.Entry(purchase_window, width=30)
        jumlah_tiket_entry.pack()

        def generate_kode_unik(length=9):
            characters = string.ascii_letters + string.digits
            kode_unik = ''
            for _ in range(length):
                if len(kode_unik) < length - 1:
                    kode_unik += random.choice(characters)
                else:
                    kode_unik += random.choice(string.digits)
            return kode_unik
        
        def lihat_tiket():
            tiket_window = tk.Toplevel()
            tiket_window.title("Tiket")
            tiket_window.geometry("600x350")
            tiket_window.configure(bg="skyblue")

            tiket_label = tk.Label(tiket_window, text="Tiket Anda", bg="skyblue", font=("Arial", 16, "bold"))
            tiket_label.pack(pady=10)

            nama = nama_entry.get()
            nik = nik_entry.get()
            email = email_entry.get()
            jumlah_tiket = int(jumlah_tiket_entry.get())
            kode_unik = generate_kode_unik()

            nama_label = tk.Label(tiket_window, text="Nama : {}".format(nama), bg="skyblue", font=("Arial", 12))
            nama_label.pack(pady=5, anchor="w")

            nik_label = tk.Label(tiket_window, text="NIK : {}".format(nik), bg="skyblue", font=("Arial", 12))
            nik_label.pack(pady=5, anchor="w")

            email_label = tk.Label(tiket_window, text="Email : {}".format(email), bg="skyblue", font=("Arial", 12))
            email_label.pack(pady=5, anchor="w")

            jumlah_tiket_label = tk.Label(tiket_window, text="Jumlah Tiket : {}".format(jumlah_tiket), bg="skyblue", font=("Arial", 12))
            jumlah_tiket_label.pack(pady=5, anchor="w")

            kode_unik_label = tk.Label(tiket_window, text="Kode Tiket : {}".format(kode_unik), bg="skyblue", font=("Arial", 12, "bold"))
            kode_unik_label.pack(pady=5, anchor="w") 

            printout_label = tk.Label(tiket_window, text="Silahkan tunjukkan E-Ticket ini di loket pembelian tiket untuk mendapatkan tiket Anda. \nTerima kasih. Selamat menikmati konser!", bg="skyblue", font=("Arial", 10, "italic"))
            printout_label.pack(pady=10)

            exit_button = tk.Button(tiket_window, text="Exit", width=12, bg="red", fg="white", command=keluar)
            exit_button.pack(pady=10)

        def submit_purchase():
            nama = nama_entry.get()
            nik = nik_entry.get()
            email = email_entry.get()
            nomor_rekening = nomor_rekening_entry.get()
            jumlah_tiket = int(jumlah_tiket_entry.get())
            tanggal_waktu = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            with open('pembelian_tiket.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([tanggal_waktu, nama, nik, email, nomor_rekening, jumlah_tiket,"Reguler"])

            harga_tiket = int(concert_info[8])
            total_harga = harga_tiket * jumlah_tiket

            total_harga_label = tk.Label(purchase_window, text="Total Harga: Rp {}".format(total_harga), font=("Arial", 12, "bold"))
            total_harga_label.pack()

            nominal_pembayaran_label = tk.Label(purchase_window, text="Nominal Pembayaran : (Rp.) ")
            nominal_pembayaran_label.pack()

            nominal_pembayaran_entry = tk.Entry(purchase_window)
            nominal_pembayaran_entry.pack()

            def submit_payment():
                nominal_pembayaran = int(nominal_pembayaran_entry.get())

                if nominal_pembayaran == total_harga:
                    payment_success_window = tk.Toplevel()
                    payment_success_window.title("Pembayaran Berhasil")
                    payment_success_window.geometry("400x200")

                    success_label = tk.Label(payment_success_window, text="\nPembayaran telah diselesaikan.",font=("Arial", 12, "bold"))
                    success_label.pack()

                    lihat_tiket_button = tk.Button(payment_success_window, text="Lihat Tiket", width=12, command=lihat_tiket)
                    lihat_tiket_button.pack(side="bottom", anchor="s", pady=10)

                elif nominal_pembayaran > total_harga:
                    kembalian = nominal_pembayaran - total_harga
                    payment_success_window = tk.Toplevel()
                    payment_success_window.title("Pembayaran Berhasil")
                    payment_success_window.geometry("400x200")

                    success_label = tk.Label(payment_success_window, text="\nPembayaran telah diselesaikan.\nKembalian: Rp {}, \nKembalian akan dikirim ke Nomor Rekening Anda".format(kembalian),font=("Arial", 12, "bold"))
                    success_label.pack()

                    lihat_tiket_button = tk.Button(payment_success_window, text="Lihat Tiket", width=12, command=lihat_tiket)
                    lihat_tiket_button.pack(side="bottom", anchor="s", pady=10)
                else:
                    retry_payment_window = tk.Toplevel()
                    retry_payment_window.title("Pembayaran Belum Selesai")
                    retry_payment_window.geometry("400x200")

                    retry_label = tk.Label(retry_payment_window, text="\nPembayaran belum selesai.\n Mohon masukkan nominal pembayaran yang sesuai.",font=("Arial", 12, "bold"))
                    retry_label.pack()


            submit_button = tk.Button(purchase_window, text="Submit Pembayaran", width=20, command=submit_payment)
            submit_button.pack(pady=10)

        button_frame = tk.Frame(purchase_window)
        button_frame.pack(pady=10)

        submit_button = tk.Button(button_frame, text="Beli", width=12, command=submit_purchase)
        submit_button.pack(side=tk.LEFT, padx=5)

        cancel_button = tk.Button(button_frame, text="Cancel",bg="red", fg="white", width=12, command=cancel_purchase)
        cancel_button.pack(side=tk.LEFT, padx=5)

    # Membuat tombol untuk konfirmasi pembelian tiket
    confirm_button = tk.Button(button_frame, text="Ya", width=12, command=show_ticket_prices)
    confirm_button.pack(side=tk.LEFT, padx=30)

    # Membuat tombol untuk membatalkan pembelian tiket
    cancel_button = tk.Button(button_frame, text="Tidak", width=12, command=confirmation_window.destroy)
    cancel_button.pack(side=tk.LEFT, padx=10)

def keluar():
    window.destroy()

def back_to_welcome(window): 
    welcome_message()
    
# Membuat jendela utama
window = tk.Tk()
window.title("ToneTix")
window.geometry("600x400")

# Menambahkan gambar
image = Image.open("TampilanAwal.png")  
image = image.resize((597, 350), Image.ANTIALIAS)  
photo = ImageTk.PhotoImage(image)
label = tk.Label(window, image=photo)
label.grid(row=0, column=0, columnspan=2)

# Menambahkan tombol
masuk_button = tk.Button(window, text="Start", bg="grey", fg="white", command=welcome_message, width=12, height=1)
masuk_button.grid(row=1, column=1)  

keluar_button = tk.Button(window, text="Exit", bg="grey", fg="white", command=keluar, width=12, height=1)
keluar_button.grid(row=1, column=0, pady=10)  

# Menjalankan aplikasi
window.mainloop()
