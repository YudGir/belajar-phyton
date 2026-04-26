# ENCAPSULATION (sebenernya) is specifically for private attributes, ya, walau sebenernya bisa juga buat non-private attributes.
class Matkul:

    def __init__(self, namaMatkul, jumlahSKS, durasi, rateoflearning, kelastambahan):
        self.__nama = namaMatkul
        self.__banyak = jumlahSKS
        self.__durasi = durasi
        self.tingkat = rateoflearning
        self.__adakelastambahan = kelastambahan
    
    @property
    #getter:
    def printNamaMatkul(self):
        return self.__nama
    
    #setter:
    def changeItsSKS(self, value):
        self.__banyak = value
    
    def ubahMatkulKelasTambahan(self, binarycode):
        tempVariable = self.__adakelastambahan + binarycode
        if (0 <= tempVariable < 2):
            self.__adakelastambahan += binarycode
        else:
            print("Do you mean 1 (ada)? It's already assigned.")

matkul1 = Matkul("Linear Algebra", 2, 60, 'Intermediate', 0)
print(matkul1.printNamaMatkul)
