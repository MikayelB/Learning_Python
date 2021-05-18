bitString = []
complement = []
inputString = input("PLease input a binary number")
for bit in inputString:
    bitString.append(1 - int(bit))
carry = 1
sumlist = []
for index in range(len(bitString) - 1, 0, -1):
    if bitString[index] + carry == 2:
        sumlist.append(0)
        carry = 1
    elif bitString[index] + carry == 1:
        sumlist.append(1)
        carry = 0
    else:
        sumlist.append(0)
        carry = 0

if bitString[0] == 1 and carry == 1:
    sumlist.append(0)
    sumlist.append(1)
else:
    sumlist.append(bitString[0] + carry)
for place in range(len(sumlist) - 1, -1, -1):
    complement.append(sumlist[place])
print(complement)