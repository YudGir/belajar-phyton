while True:
    try: 
        userInput = int(input("Input angka pembagi kamu di sini: "))
        hasilBagi = 100/userInput
    except ZeroDivisionError:
        print("Nggak bisa bagi nol!")
    except ValueError:
        print("Masukin angka, Bro!")
    else:
        print(f"Hasil bagi angka kamu dengan 100 adalah: {hasilBagi}")
        break
    finally:
        print("---Putaran Selesai---")