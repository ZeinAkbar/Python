username = str(input("Masukkan Username : "))
password = str(input("Masukkan Password : "))

if (username == "zen" and password == "123"):

    saldo = 500000 

    print("Login Berhasil")
    print("-----RPL MOBILE BANKING-----")
    print("Saldo anda : " + str(saldo))
    print("1. Tarik tunai")
    print("2. Transfer")
    print("3. Top Up")

    transaksi = str(input("Pilih Transaksi : "))

    match transaksi :
            case "1" :
                tarik_saldo = int(input("Masukan Nominal : "))
                hasil = saldo - tarik_saldo
                print("Penarikan berhasil")
                print("anda menarik saldo : " + str(tarik_saldo) + " dari bank")
                print("sisa saldo anda : " + str(hasil))
            case "2" :
                jumlah_transfer = int(input("Masukan Nominal : "))
                hasil = saldo - jumlah_transfer
                print("Penarikan berhasil")
                print("anda men transfer : " + str(jumlah_transfer) + " dari bank")
                print("sisa saldo anda : " + str(hasil))
            case "3" :
                jumlah_topup = int(input("Masukan Nominal : "))
                hasil = saldo - jumlah_topup
                print("Penarikan berhasil")
                print("anda Top Up : " + str(jumlah_topup) + " dari bank")
                print("sisa saldo anda : " + str(hasil))

else :
    print("Login gagal")

