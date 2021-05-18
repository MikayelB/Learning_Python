def isodd(n):
    if n%2 == 0:
        return False
    return True
step = 0
oddsums = 0
while step < 10:
    number = int(input("Pease input a number"))
    if isodd(number):
        oddsums += number
    step += 1
print(oddsums)