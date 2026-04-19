# matkul = "Kalkulus Lanjut (Susah)" #strings are sequences
# print(matkul[8]) #return: (space) (di antara s dan L)
# print(matkul[-7:]) #return: (Susah)
# print(matkul[:2]) #return: Ka
# print(matkul[9:]) #return: Lanjut (Susah)
# print(matkul[0:8]) #return: Kalkulus
# print(matkul[:-22]) #return: K
# print(f"How long is this string: {len(matkul)}")

# print([char + "!" for char in matkul])

# print("\n") #-----------------------------------------------------------------

# Matkul = "MRV adalah mata kuliah terseru di bidang AI"
# print(Matkul.index('AI')) #to find where it is in index
# print(Matkul.upper()) #ALL CAPS
# print(Matkul.lower()) #all lowercase
# print(Matkul.startswith('MRV')) #return: True
# print(Matkul.endswith('.')) #return: True

# resultSplit = Matkul.split()
# print(resultSplit)

# datestr = '1990-01-30'
# year, month, day = datestr.split('-')
# print("/".join([year, month, day]))
# print("😁".join([matkul.upper() for matkul in Matkul]))

# mtul = 'MRV'
# sem = 2
# print(mtul + ', matkul terseru semester ini!\n')
# print(mtul + ', matkul terseru di semester ' + str(sem) + ' ini!' )
# print("{}, matkul terseru di semester {} ini!".format(mtul, sem)) #.format helps us easier

# print("\n") #-----------------------------------------------------------------

# str = '''hey
# {0} is easy matkul
# in semester {1}
# so, basically {0} is easy peasy 
# in this {1}nd semester'''.format('MRV', 2)

# print(str)

# print("\n") #-----------------------------------------------------------------

# #       KEY:CORRESPONDING VALUE
# data = {'pertama':1, 'kedua':2, 'ketiga':3}     #dictionary: use KEY and ITS VALUE
# # print(data['HAHAHA'])
# # data['keempat'] = 4
# # data[200] = 'first'
# # print(data)

# mataKuliah = ['ORII', 'APL', 'PJK', 'STI', 'ST', 'PAPL', 'MRV', 'ENG', 'KL', 'JK']
# print(mataKuliah.split)
# initial_mataKuliah = {matkul: matkul[0] for matkul in mataKuliah}
# print(initial_mataKuliah)
# print("ORII" in initial_mataKuliah)
# print(" ".join(sorted(initial_mataKuliah.values()))) #.sorted -> utk mengurutkan | .values -> utk mengambil nilai corresponding value dari si key

# print("\n") #-----------------------------------------------------------------

# for i in data:
#     print("\"{}\" is the KEY which has a CORRESPONDING VALUE with: '{}' ".format(i, data[i]))

# print("\n") #-----------------------------------------------------------------

# def word_search(doc_list, keyword):
#     result = []
#     for i, doc in enumerate(doc_list):
#         tokens = doc.split()

#         normalized_data = []
#         for token in tokens:
#             normalized = token.rstrip('.-').lower()
#             normalized_data.append(normalized)
        
#         if keyword.lower() in normalized_data:
#             result.append(i)
    
#     return result


# def multi_word_search(doc_list, keywords):
#     final_result = {}

#     for kw in keywords:
#         indices = word_search(doc_list, kw)

#         final_result[kw] = indices
    
#     return final_result

# doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
# keyword = ['casino', 'car']
# print(multi_word_search(doc_list, keyword)) 


# def count_words(doc_list, keywords):
#     finalResult = {}

#     for keyword in keywords:
#         banyakMuncul = 0

#         for doc in doc_list:
#             tokens = doc.split()

#             for token in tokens:
#                 clean = token.rstrip(',!.').lower()
            
#                 if clean == keyword.lower():
#                     banyakMuncul += 1
            
#         finalResult[keyword] = banyakMuncul
#     return finalResult

# tweets = [
#     "Belajar Python itu seru!",
#     "Python adalah bahasa AI.",
#     "Seru banget belajar di Kaggle, Kaggle mantap!"
# ]
# target_words = ["python", "seru", "kaggle"]
# print(count_words(tweets, target_words))


# for key, value in data.items():   # .items -> utk ngambil si key dan si value
#     print("Key {} punya value {}".format(key.rjust(10), value)) # rjust itu hapus sebanyak 10 space dari KANAN (right)

# doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]


# def organisir_buku(buku_list):
#     hasilAkhir = {}

#     for buku in buku_list:
#         hasil1 = buku.split(' - ')
#         judul = hasil1[0]
#         kategori = hasil1[1]

#         if kategori not in hasilAkhir:
#             hasilAkhir[kategori] = []
        
#         hasilAkhir[kategori].append(judul)

#     return hasilAkhir

# # Formatnya: "Judul Buku - Kategori"
# buku_masuk = [
#     "Deep Learning - Teknologi",
#     "Filosofi Teras - Filsafat",
#     "Seni Berperang - Sejarah",
#     "Python 101 - Teknologi",
#     "Dunia Sophie - Filsafat"
# ]

# print(organisir_buku(buku_masuk))

#Final Chalans: The AI Fruit Shop

# def hitung_pendapatan(catatan):
#     hasilAkhir = {}
#     hasil1 = catatan_penjualan.split(', ')

#     for hasil in hasil1:
#         harga_buah = 0
#         hasil2 = hasil.split(':')

#         nama_buah = hasil2[0]
#         harga_buah = int(hasil2[1])

#         for i, buah in enumerate(nama_buah):
#             banyakBuahSama = 0
#             if buah.count(nama_buah) > 1:
#                 banyakBuahSama = buah[i].count
#             else:
#                 banyakBuahSama = 1

#                 if nama_buah not in hasilAkhir:
#                     hasilAkhir[nama_buah] = harga_buah
#                 else:
#                     hasilAkhir[nama_buah] = harga_buah * banyakBuahSama

#     return hasilAkhir

catatan_penjualan = "apel:5000, jeruk:3000, apel:5000, mangga:7000, jeruk:3000"

hasil1 = catatan_penjualan.split(', ')

for hasil in hasil1:
    harga_buah = 0
    hasil2 = hasil.split(':')

    nama_buah = hasil2[0]
    harga_buah = int(hasil2[1])

    # print(nama_buah)
    for i in enumerate (nama_buah):
        print(i)
    # Buah = nama_buah.
    # print(Buah)

# print(hitung_pendapatan(catatan_penjualan))