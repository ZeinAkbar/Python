username = str(input("Masukkan Username : "))
password = str(input("Masukkan Password : "))

if (username == "zen" and password == "123"):

    saldo = 500000 

    print()
    print("Login Berhasil")
    print("===== RPL MOBILE BANKING =====")
    print("Saldo anda : Rp" + str(saldo))

    while True:

        print()
        print("==== Menu Utama ====")
        print("1. Tarik Tunai")
        print("2. Transfer")
        print("3. Top Up")
        print("4. Cek Saldo")
        print("5. Keluar")

        transaksi = str(input("Pilih Transaksi: "))

        match transaksi:

            case "1":
                print()
                print("==== Tarik Tunai ====")

                tarik_saldo = int(input("Masukkan Nominal : "))
                
                if tarik_saldo <= saldo:
                    saldo = saldo - tarik_saldo

                    print("Penarikan Berhasil")
                    print("Anda Menarik : Rp" + str(tarik_saldo))
                    print("Sisa Saldo Anda : Rp" + str(saldo))

                else:
                    print("Saldo Tidak Mencukupi!")

            case "2":
                print()
                print("==== Transfer ====")

                nama_tujuan = str(input("Nama Penerima : "))
                jumlah_transfer = int(input("Jumlah Transfer : "))

                if jumlah_transfer <= saldo:
                    saldo = saldo - jumlah_transfer

                    print("Transfer Berhasil")
                    print("Anda Mentransfer : Rp" + str(jumlah_transfer))
                    print("Sisa Saldo Anda : Rp" + str(saldo))

                else:
                    print("Saldo Tidak Mencukupi!")

            case "3":
                print()
                print("==== Top Up ====")

                jumlah_topUp = int(input("Masukkan Nominal : "))
                saldo = saldo + jumlah_topUp

                print("Top Up berhasil")
                print("Jumlah Top Up : Rp" + str(jumlah_topUp))
                print("Saldo sekarang : Rp" + str(saldo))

            case "4":
                print()
                print("==== Cek Saldo ====")
                print("Saldo Anda : " + str(saldo))

            case "5":
                print()
                print("Terima kasih telah menggunakan")
                print("RPL Mobile Banking")
                break

            case _:
                print()
                print("Pilihan tidak tersedia!")

else:
    print("Login Gagal")
                
                



        
