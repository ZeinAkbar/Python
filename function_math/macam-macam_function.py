#function + if
def cek_saldo(saldo, jumlah):
    if jumlah <= saldo:
        return "Saldo mencukupi"
    else:
        return "Saldo tidak mencukupi"


hasil = cek_saldo(500000, 100000)

print(hasil)

#function + list
def tampilkan_siswa(daftar_siswa):
    for siswa in daftar_siswa:
        print(siswa)


siswa = ["Zein", "Icat", "Kibo", "Rian"]

tampilkan_siswa(siswa)

#function Mengembalikan list
def angka_genap(angka):
    hasil = []

    for i in angka:
        if i % 2 == 0:
            hasil.append(i)

    return hasil


data = [1, 2, 3, 4, 5, 6, 7, 8]

genap = angka_genap(data)

print(genap)

#scope
nama = "Zein"

def siswa():
    nama = "Kibo"
    print(nama)

siswa()

print(nama)