# jadwalKuliah = ['ORII', 'APL', 'PJK', 'STI', 'ST', 'PAPL', 'MRV', 'ENG', 'KL', 'JK'] #this is list

# for jadwal in jadwalKuliah:
#     print(jadwal, end=' | ')

# print("\n") #---------------------------------------------------------------------------------

# frekuensi = (1, 2, 3, 4, 5) #this is tuple, not list
# product = 1

# for freq in frekuensi:
#     product = product * freq

# print(product)

# print("\n")  #---------------------------------------------------------------------------------

# a = 'ahahahaha lucu Banget Anak Panda itu kepAda Kucing'

# for an in a:
#     if an.isupper():
#         print(an, end="")

# print("\n")  #---------------------------------------------------------------------------------

# for i in range(5):
#     print("This is the: ", i, "time(s) to reprint!") #print for 5 times as asked

# print("\n")  #---------------------------------------------------------------------------------

# i = 6
# while(i > 3):
#     print("Hahaha ke-",i)
#     i -= 1

# print("\n")  #---------------------------------------------------------------------------------

# # n = 1
# # squares = [n**2 for n in range(11)]
# # print(squares)

# squares = []
# for n in range(10):
#     squares.append(n**2)
# print(squares)

print("\n")  #---------------------------------------------------------------------------------

import random

def play_slot_machine():
    """Simulasi mesin slot sederhana untuk latihan lokal"""
    # Menghasilkan angka acak (misal antara 0 sampai 5 dolar)
    return random.choices([0, 5, 5.5], weights=[80, 15, 5])[0]

def estimate_average_slot_payout(n_runs):
    total_payout = 0
    for i in range(n_runs):
        # Langsung jumlahkan, jangan simpan di list dulu
        total_payout += (play_slot_machine() - 1)
    return total_payout / n_runs
    
print(estimate_average_slot_payout(10000000))