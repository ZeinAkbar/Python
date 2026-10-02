def tambah(a, b):
    return a + b


def kurang(a, b):
    return a - b


def kali(a, b):
    return a * b


def bagi(a, b):
    return a / b

print("==== Aplikasi Matematika ====")

while True:
    print()
    print("=== Pilih Operasi ===")
    print("1. Tambah")
    print("2. Kurang")
    print("3. Kali")
    print("4. Bagi")
    print("5. Exit")

    pilihan = input("Masukkan Pilihan Operasi : ")

    match pilihan:
        case "1":
            print()
            print("Anda Memilih Penjumlahan")

            a = int(input("Masukkan Angka Pertama : "))
            b = int(input("Masukkan Angka Kedua : "))
            hasil = tambah(a,b)

            print(f"Hasil Penjumlaham : {hasil}")
            
        case "2":
            print()
            print("Anda Memilih Pengurangan")

            a = int(input("Masukkan Angka Pertama : "))
            b = int(input("Masukkan Angka Kedua : "))
            hasil = kurang(a,b)

            print(f"Hasil Pengurangan : {hasil}")

        case "3":
            print()
            print("Anda Memilih Perkalian")

            a = int(input("Masukkan Angka Pertama : "))
            b = int(input("Masukkan Angka Kedua : "))
            hasil = kali(a,b)

            print(f"Hasil Perkalian : {hasil}")
            
        case "4":
            print()
            print("Anda Memilih Pembagian")

            a = int(input("Masukkan Angka Pertama : "))
            b = int(input("Masukkan Angka Kedua : "))
            hasil = bagi(a,b)

            print(f"Hasil Pembagian : {hasil}")
        case "5":
            print("Program Selesai")
            break
            
        case _:
            print("Pilihan Tidak Tersedia")