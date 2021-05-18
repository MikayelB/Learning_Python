print("Input a number between 1 and 1000")
N = int(input("N = "))

while N < 1 or N > 1000:
    print("Out of range, please input again")
    N = int(input("N = "))

number = 0
thesum = 0

while number < N:
    duplicate = number

    while duplicate > 0:
        reminder = duplicate % 10

        if reminder == 7:
            thesum = thesum + number
            break
        duplicate = duplicate // 10

    if duplicate > 0:
        number = number + 1
        continue

    number = number + 1
print(thesum)
