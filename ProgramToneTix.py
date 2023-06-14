import csv
import random
import sys
from datetime import datetime

def welcome_message():
    print("==============================================================")
    print("                  SELAMAT DATANG DI TONETIX!")
    print("      Kami adalah platform penjualan tiket konser terbaik untukmu!")
    print("==============================================================")
    print("Tonetix menyediakan tiket konser untuk berbagai genre musik populer,")
    print("dengan kualitas suara dan pengalaman konser yang tak terlupakan.")
    print("Dengan Tonetix, Anda dapat menjelajahi dan membeli tiket untuk")
    print("konser-konser terbaik dari musisi dan band favorit Anda.")
    print("==============================================================")
    print("Untuk membeli tiket, silakan pilih nomor genre musik yang Anda minati.")
    print("Kami akan membantu Anda mendapatkan pengalaman konser yang luar biasa!")
    print("==============================================================")
    print()
    
def show_genre_menu():
    print("Pilih nomor genre musik yang Anda minati:")
    print("1. Jazz")
    print("2. Rock")
    print("3. Pop")
    print("4. Dangdut")
    print("5. Keluar")
    print("\n===============================")
    
def get_genre_choice():
    choice = input("\nMasukkan nomor genre musik yang Anda pilih: ")
    return choice

def show_jazz_concerts():
    with open('konser_jazz.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        print()
        print("Daftar Konser Jazz yang Tersedia:")
        print("=========================================")
        count = 1
        concerts = []  # List untuk menyimpan data konser
        for row in reader:
            concerts.append(row)  # Menambahkan data konser ke list
            print("Nomor Konser :", count)
            print("Nama Konser  :", row[0])
            print("Venue        :", row[1])
            print("Lokasi       :", row[2])
            print("Tanggal      :", row[3])
            print("Harga        : - VIP     : Rp. ",row[7])
            print("               - Reguler : Rp. ",row[8])
            print("=========================================")
            count += 1
        return concerts
    
def choose_jazz_concert(concerts):
    choice = input("\nMasukkan nomor konser yang Anda pilih: ")
    try:
        choice = int(choice)
        if 1 <= choice <= len(concerts):
            chosen_concert = concerts[choice - 1]
            print()
            print("Anda memilih konser:", chosen_concert[0])
            print("Line-up:")
            print("- Line-up 1 :", chosen_concert[4])
            print("- Line-up 2 :", chosen_concert[5])
            print("- Line-up 3 :", chosen_concert[6])
            print("Harga Tiket:")
            print("- VIP     : Rp.", chosen_concert[7])
            print("- Reguler : Rp.", chosen_concert[8])
            print()

            buy_ticket = input("Apakah Anda ingin membeli tiket? (ya/tidak): ")
            if buy_ticket.lower() == "ya":
                ticket_type = input("Pilih jenis tiket (VIP/Reguler): ")
                if ticket_type.lower() == "vip":
                    buy_vip_ticket(chosen_concert)
                elif ticket_type.lower() == "reguler":
                    buy_reguler_ticket(chosen_concert)
                else:
                    print("Jenis tiket yang Anda pilih tidak valid.")
            else:
                view_other_concerts = input("Apakah Anda ingin melihat konser yang lain? (ya/tidak): ")
                if view_other_concerts.lower() == "ya":
                    print("Kembali ke menu awal :")
                else:
                    print("Terima kasih telah menggunakan ToneTix!")
                    sys.exit()
        else:
            print("Nomor konser yang Anda pilih tidak valid.")
    except ValueError:
        print("Input yang Anda masukkan bukan nomor konser yang valid.")

def show_rock_concerts():
    with open('konser_rock.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        print("Daftar Konser Rock yang Tersedia:")
        print("=========================================")
        count = 1
        concerts = []  # List untuk menyimpan data konser
        for row in reader:
            concerts.append(row)  # Menambahkan data konser ke list
            print("Nomor Konser :", count)
            print("Nama Konser  :", row[0])
            print("Venue        :", row[1])
            print("Lokasi       :", row[2])
            print("Tanggal      :", row[3])
            print("Harga        : - VIP     : Rp. ",row[7])
            print("               - Reguler : Rp. ",row[8])
            print("=========================================")
            count += 1
        return concerts

def choose_rock_concert(concerts):
    choice = input("\nMasukkan nomor konser yang Anda pilih: ")
    try:
        choice = int(choice)
        if 1 <= choice <= len(concerts):
            chosen_concert = concerts[choice - 1]
            print()
            print("Anda memilih konser:", chosen_concert[0])
            print("Line-up:")
            print("- Line-up 1 :", chosen_concert[4])
            print("- Line-up 2 :", chosen_concert[5])
            print("- Line-up 3 :", chosen_concert[6])
            print("Harga Tiket:")
            print("- VIP     : Rp.", chosen_concert[7])
            print("- Reguler : Rp.", chosen_concert[8])
            print()

            buy_ticket = input("Apakah Anda ingin membeli tiket? (ya/tidak): ")
            if buy_ticket.lower() == "ya":
                ticket_type = input("Pilih jenis tiket (VIP/Reguler): ")
                if ticket_type.lower() == "vip":
                    buy_vip_ticket(chosen_concert)
                elif ticket_type.lower() == "reguler":
                    buy_reguler_ticket(chosen_concert)
                else:
                    print("Jenis tiket yang Anda pilih tidak valid.")
            else:
                view_other_concerts = input("Apakah Anda ingin melihat konser yang lain? (ya/tidak): ")
                if view_other_concerts.lower() == "ya":
                    print("Kembali ke menu awal :")
                else:
                    print("Terima kasih telah menggunakan ToneTix!")
                    sys.exit()
        else:
            print("Nomor konser yang Anda pilih tidak valid.")
    except ValueError:
        print("Input yang Anda masukkan bukan nomor konser yang valid.")
        
    
    
 
