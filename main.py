import os
import random

# pilihan_user = None
user_score = 0
komputer_score = 0

suit_objek = ["", "Batu", "Gunting", "Kertas"]

# DARI YOUTUBE
# while pilihan_user != 0:
#     os.system("cls")

#     print(f"Player [{user_score}]:[{komputer_score}]")
#     for i in range(1,4):
#         print(f"{i}. {suit_objek[i]}")
#     print(f"0. Keluar")
#     pilihan_user = int(input(">> "))
#     if pilihan_user != 0:

#         print(f"Kamu memilih {suit_objek[pilihan_user]}")

#         pilihan_komputer = random.randint(1, 3)
#         print(f"Komputer memilih {suit_objek[pilihan_komputer]}")

#         if pilihan_user == pilihan_komputer:
#             print("- HASIL SERI")
#         elif(pilihan_user == 1 and pilihan_komputer == 2) or (pilihan_user == 2 and pilihan_komputer == 3) or (pilihan_user == 3 and pilihan_komputer == 1):
#             print("USER MENANG")
#             user_score += 1
#         else:
#             print("KOMPUTER MENANG")
#             komputer_score += 1

#         input("Tekan enter untuk lanjut >> ")


#? HASIL MODIFIKASI
while True:
    os.system("cls")
    print("="*35)
    print(" "*4 + "PROGRAM GUNTING BATU KERTAS")
    print("="*35)
    print(f"Player [{user_score}]:Komputer[{komputer_score}]")
    for i in range(1,4):
        print(f"{i}. {suit_objek[i]}")
    pilihan_user = int(input(">> "))

    print(f"Kamu memilih {suit_objek[pilihan_user]}")

    pilihan_komputer = random.randint(1, 3)
    print(f"Komputer memilih {suit_objek[pilihan_komputer]}")

    if pilihan_user == pilihan_komputer:
        print("- HASIL SERI")
    elif(pilihan_user == 1 and pilihan_komputer == 2) or (pilihan_user == 2 and pilihan_komputer == 3) or (pilihan_user == 3 and pilihan_komputer == 1):
        print("USER MENANG")
        user_score += 1
    else:
        print("KOMPUTER MENANG")
        komputer_score += 1
    
    selesai = input("Apakah Sudah selesai (y/n)? ")
    if selesai.lower() == "y":
        print("TERIMAKASIH TELAH MENGGUNAKAN PROGRAM KAMI......\n")
        break