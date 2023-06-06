import csv

#Program ToneTixs
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
    print("Genre musik yang kami sediakan tiket konsernya:")
    print("1. Jazz")
    print("2. Rock")
    print("3. Pop")
    print("4. Dangdut")
    print("==============================================================")
    print("Tonetix adalah pintu masuk ke dunia hiburan yang memukau dan menghibur.")
    print("Nikmati performa musik yang spektakuler, suasana yang energik, dan")
    print("kenangan yang tak terlupakan bersama Tonetix.")
    print("==============================================================")
    print("Untuk membeli tiket, silakan pilih nomor genre musik yang Anda minati.")
    print("Kami akan membantu Anda mendapatkan pengalaman konser yang luar biasa!")
    print("==============================================================")
    print()

def get_genre_choice():
    genre_choice = input("Masukkan nomor genre musik yang Anda pilih: ")
    return genre_choice

def show_jazz_concerts():
    with open('konser_jazz.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  
        print("Daftar Konser Jazz yang Tersedia:")
        print("===============================")
        for row in reader:
            print("Nama Konser:", row[0])
            print("Venue :", row[1])
            print("Lokasi :",row[2])
            print("Tanggal :", row[3])
            print("===============================")

def show_rock_concerts():
    with open('konser_rock.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  
        print("Daftar Konser Rock yang Tersedia:")
        print("===============================")
        for row in reader:
            print("Nama Konser:", row[0])
            print("Venue :", row[1])
            print("Lokasi :",row[2])
            print("Tanggal :", row[3])
            print("===============================")          

def show_pop_concerts():
    with open('konser_pop.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  
        print("Daftar Konser Pop yang Tersedia:")
        print("===============================")
        for row in reader:
            print("Nama Konser:", row[0])
            print("Venue :", row[1])
            print("Lokasi :",row[2])
            print("Tanggal :", row[3])
            print("===============================")

def show_dangdut_concerts():
    with open('konser_dangdut.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  
        print("Daftar Konser Dangdut yang Tersedia:")
        print("===============================")
        for row in reader:
            print("Nama Konser:", row[0])
            print("Venue :", row[1])
            print("Lokasi :",row[2])
            print("Tanggal :", row[3])
            print("===============================")


# Program utama
if __name__ == "__main__":
    welcome_message()
    genre = get_genre_choice()
    
    if genre == "1":
        show_jazz_concerts()
    elif genre == "2":
        show_rock_concerts()
    elif genre == "3":
        show_pop_concerts()
    elif genre == "4":
        show_dangdut_concerts()
    else:
        print("Genre musik yang Anda pilih tidak valid.")
