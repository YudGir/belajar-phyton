class Nasabah: # ini adalah class or template
    total_nasabah = 0 #ini adalah class variable

    def __init__(self, nama, saldo): #ini adalah method constructor
        self.namaNasabah = nama
        self.__saldoAwal = saldo
        Nasabah.total_nasabah += 1
        self._nomorRekening = Nasabah.total_nasabah
        print(f"Berhasil menambahkan nasabah baru dengan nama {self.namaNasabah}.")
        print(f"{self.namaNasabah} mempunyai nomor rekening: {self._nomorRekening}")
    
    def cek_saldo(self):
        return self.__saldoAwal

    def tambah_uang(self, tambahSaldo):
        self.__saldoAwal += tambahSaldo
        print(f"Berhasil menambah saldo dari pengguna {self.namaNasabah} sebanyak {tambahSaldo}.")
        print(f"Total saldo di rekening menjadi {self.__saldoAwal}.")
    
    def tarik_uang(self, tarikSaldo):
        if (self.__saldoAwal >= tarikSaldo):
            self.__saldoAwal -= tarikSaldo
            print(f"Berhasil menarik saldo dari rekening sebanyak {tarikSaldo}.")
            print(f"Sisa saldo menjadi {self.__saldoAwal}.")
        else: 
            print(f"Gagal menarik uang sebanyak {tarikSaldo} karena sisa saldo hanya {self.__saldoAwal}.")

user1 = Nasabah("Yudha", 5000)
user2 = Nasabah("Google AI", 100000) #waduh jauh sekali ya, iya dong MABROOO hihi luv uuuu :)
print()
user1.tambah_uang(2000)
print()
user1.tarik_uang(8000) # Harusnya gagal karena saldo cuma 7000
print()
user1.cek_saldo()
# Contoh cara panggil method yang ada return-nya:
print(f"Saldo akhir yang terdata: {user1.cek_saldo()}")
