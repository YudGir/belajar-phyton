class Matkul:

    def __init__(self, namaMatkul, jumlahSKS, durasi, rateoflearning, kelastambahan):
        self.nama = namaMatkul
        self.banyak = jumlahSKS
        self.durasi = durasi
        self.tingkat = rateoflearning
        self.adakelastambahan = kelastambahan
    
    #getter:
    def printNamaMatkul(self):
        return self.nama
    
    #setter:
    def changeItsSKS(self, value):
        self.banyak = value
    
    def ubahMatkulKelasTambahan(self, binarycode):
        tempVariable = self.adakelastambahan + binarycode
        if (0 <= tempVariable < 2):
            self.adakelastambahan += binarycode
        else:
            print("Do you mean 1 (ada)? It's already assigned.")
        
matkul1 = Matkul("Linear Algebra", 2, 60, 'Intermediate', 0)
matkul1.printNamaMatkul()