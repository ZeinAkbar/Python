hari = str(input("Masukkan hari : "))
match hari :
    case "senin" | "Senin":
        print("Seragam almamater")
    case "selasa" | "Selasa":
        print("Putih abu")
    case "rabu" | "Rabu":
        print("Baju muslim biru")
    case "kamis" | "Kamis":
        print("HW")
    case "jumat" | "Jumat" | "jum'at" | "Jum'at":
        print("Baju Jurusan")
    case _:
        print("Seragam tidak ditemukan")