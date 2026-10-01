huruf = str(input("Masukkan huruf : "))
match huruf :
    case "a" | "A":
        print("Sangat Baik")
    case "b" | "B":
        print("Baik")
    case "c" | "C":
        print("Cukup")
    case "d" | "D":
        print("Kurang")
    case "e" | "E" :
        print("Sangat Kurang")