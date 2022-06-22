from func import *


up = 0
down = 0
n = 0
m = 0
print("Enter data for binary numbers:")

m,down,up = input_data(m,down,up)
list_bin = GenerateBinNumbers(m,down,up)
print("Randomly generated binary numbers:")
PrintArray(list_bin)

print("Enter data for hex numbers:")
n,down,up = input_data(n,down,up)
list_hex = GenerateHexNumbers(n,down,up)
print("Randomly generated hex numbers:")
PrintArray(list_hex)

print("Those numbers in decimal system:")
print("Binary array into decimal:")
PrintArrayDec(list_bin)
print("Hex array into decimal:")
PrintArrayDec(list_hex)


print("Incremented and Decremented numbers:")
Increment_Decrement(list_bin,list_hex)
print("Those numbers in decimal system:")
print( "Binary array into decimal:")
PrintArrayDec(list_bin)
print( "Hex array into decimal:")
PrintArrayDec(list_hex)

print("The biggest number in decimal system: " + str(FindTheBiggestDecNumber(list_bin,list_hex)))
list_max = IndexesOfBiggest(list_bin,list_hex)
print("Searched number in its system/s:")
print(str(list_max[0]) + " is the biggest number and it was written in " + list_max[1] + " system")