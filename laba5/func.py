from random import *
from TIntNumber import *

def input_data(size,down,up):
    while True:
        try:
            size = int(input("Enter amount of numbers: "))
        except:
            print("Incorrect value!")
        else:
            if size <= 0:
                print("Size connot be smaller then 0!")
            else:
                break
    while True:
        try:
            down = int(input("Enter down limit : "))
            break
        except:
            print("Incorrect value!")
    while True:
        try:
            up = int(input("Enter upper limit(bigger than down limit) : "))
        except:
            print("Incorrect value!")
        else:
            if up<down:
                print("Up limit smaller than down limit.")
            else:
                break

    return size,down,up

def GenerateBinNumbers(size,down,up):
    list_bin = []
    for i in range(0,size):
        object = TIntNumber2()
        object.set_number(object.ToBin(randint(down,up)))
        object.set_base(2)
        list_bin.append(object)
    return list_bin

def GenerateHexNumbers(size,down,up):
    list_hex = []
    for i in range(0,size):
        object = TIntNumber16()
        object.set_number(object.ToHex(randint(down,up)))
        object.set_base(16)
        list_hex.append(object)
    return list_hex

def Increment_Decrement(list_bin,list_hex):
    print("Decremented binary numbers:")
    for i in range(0,len(list_bin)):
        list_bin[i] -= 1
        print(str(list_bin[i]),end = "")
    print("")
    print("Incremented hex numbers:")
    for i in range(0,len(list_hex)):
        list_hex[i] += 1
        print(str(list_hex[i]),end = "")
    print("")
    print("___________________________________")

def PrintArrayDec(list):
    for i in range(0,len(list)):
        print(str(list[i].ToDecimal()) + " ",end = "")
    print("\n___________________________________")

def PrintArray(list):
    for i in range(0,len(list)):
        print(str(list[i]),end = "")
    print("\n___________________________________")

def FindTheBiggestDecNumber(list_bin,list_hex):
    max = list_bin[0].ToDecimal()
    for i in range(0,len(list_bin)):
        if list_bin[i].ToDecimal() > max:
            max = list_bin[i].ToDecimal()
    for i in range(0,len(list_hex)):
        if list_hex[i].ToDecimal() > max:
            max = list_hex[i].ToDecimal()
    return max

def IndexesOfBiggest(list_bin,list_hex):
    list_max = []
    max = FindTheBiggestDecNumber(list_bin,list_hex)
    for i in range(0, len(list_bin)):
        if list_bin[i].ToDecimal() == max:
            list_max.append(list_bin[i])
            list_max.append("binary")
    for i in range(0, len(list_hex)):
        if list_hex[i].ToDecimal() == max:
            list_max.append(list_hex[i])
            list_max.append("hex")
    return list_max