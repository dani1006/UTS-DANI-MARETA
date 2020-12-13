# UTS-DANI-MARETA
# GAME KUIS SEDERHANA PERKALIAN MATEMATIKA

print("Game Matermatika")
def soal_pertama():
    X = int(input(" 4 * 5 = "))
    if (X == 20):
        print("Benar!! ")
    else:
        print("Yah salah")
def soal_kedua():
    Y = int(input(" 2 * 3 = "))
    if (Y == 6):
        print("Benar!! ")
    else:
        print("Yah salah")
def soal_ketiga():
    Z = int(input(" 8 * 9 = "))
    if (Z == 72):
        print("Benar!! ")
    else:
        print("Yah salah")
def soal_keempat():
    A = int(input(" 3 * 9 = "))
    if (A == 27):
        print("Benar!! ")
    else:
        print("Yah salah")
def soal_kelima():
    B = int(input(" 15 * 4 = "))
    if (B == 60):
        print("Benar!! ")
    else:
        print("Yah salah")
def soal_keenam():
    C = int(input(" 6 * 8 = "))
    if (C == 48):
        print("Benar!! ")
    else:
        print("Yah salah")
def soal_ketujuh():
    D = int(inpuy(" 9 * 12 = "))
    if (D == 108):
        print("Benar!! ")
    else:
        print("Yah salah")
def soal_kedelapan():
    E = int(input(" 3 x 1 = ")
    if (E == 3):
        print("Benar!! ")
    else:
        print("Yah salah")
def soal_kesembilan():
    F= int(input(" 4 x 24 = "))
    if (F== 96):
        print("Benar!! ")
    else:
        print("Yah salah")
def soal_kesepuluh():
    G= int(input(" 7 x 9 = "))
    if (G== 54):
        print("Benar!! ")
    else:
        print("Yah salah ")   
            
def show_menu():
    print()
    print("----Istirahat duluu----")
    print()
    print("Lanjut? ")
    print("1. Ya ")
    print("2. Tidak ")
    
    menu = int(input(" Pilih manu: "))
    print()
    
    if menu == 1:
        soal_keenam()
        soal_ketujuh()
        soal_kedelapan()
        soal_kesembilan()
        soal_kesepuluh()
    elif menu == 2:
        exit()
    else:
        print("wah ada yang salah!")
        
soal_pertama()
      
