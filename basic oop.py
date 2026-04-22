class Person:                   # can be called as 'class' or 'template'
    jumlah = 0                  # this is class variable
    
    def __init__(self, nama, birth, bar, cubit, defense):    # '__init__(self)' is the method constructor
        self.firstName = nama                                # class or template Person has two attributes (instance variables) in it:
        self.birthYear = birth                               # 'firstName' and 'lastName'
        self.barHealth = bar
        self.powerofCubit = cubit
        self.personDefense = defense
        Person.jumlah += 1
        print()     #membuat new line only
        # print(f"Menambahkan {nama} ")

    # ada 3 jenis method di python: 

    # 1 - method tanpa return (kek void)
    def siapa(self):
        print(f"nama: {self.name}")
    
    # 2 - method dengan argumen
    def nambah(self, angkaNambah):
        self.birthYear += angkaNambah
    
    # 3 - method dengan return
    def printName(self):
        self.firstName
    
    def cubit(self, orang):
        print(f"{self.firstName} mencubit {orang.firstName}")
        orang.kena_cubit(self, self.powerofCubit)
    
    def kena_cubit(self, orang):
        print(f"{self.firstName} dicubit {orang.firstName}")
        darah_berkurang = (self.personDefense / orang.powerofCubit)
        darah_sekarang = self.barHealth - darah_berkurang
        print(f"darah {self.firstName} berkurang {darah_berkurang}")
        print(f"darah {self.firstName} tinggal: {darah_sekarang}")

    

# person1 = Person()            # here, variable person1 is the 'object' of the class Person. 
                                # there are so many callings, like 'instance', 'instance variable', etc, but focus on 'object' only!
# print(person1)                # print: tipe data si person1 adalah class Person dan alamatnya di komputer

# person2 = Person()
# person3 = Person()

# person1.firstName = "Dhayu"
# person1.birthYear = 2005
# print(f"First name of person 1: {person1.firstName} and {person1.birthYear}")
# person2.firstName = "Loka"
# person2.birthYear = 2009
# print(f"First name of person 2: {person2.firstName} and {person2.birthYear}")
# person3.firstName = "Pab"
# person3.birthYear = 2010
# print(f"First name of person 3: {person3.firstName} and {person3.birthYear}") 

# if isinstance(person3, Person):     # utk check whether the variable 'person3' has type data with Person
#     print("Yes, it is!")
# if isinstance(person1, object):     # semua bentuk class yg ada di Python adalah turunan dari class 'object' 
#     print("Yes, it is!")

# person1 = Person("Yudha", 2008, 100, 20)
# print(f"Jumlah orang terdata sekarang: {Person.jumlah}")
# person2 = Person("Dhayu", 2009, 100, 10)
# print(f"Jumlah orang terdata sekarang: {Person.jumlah}")


Yudha = Person("Yudha", 2008, 100, 1, 20)
Dhayu = Person("Dhayu", 2009, 100, 10, 10)

Yudha.cubit(Dhayu)
print()
Dhayu.cubit(Yudha)