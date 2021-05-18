print("Input a number between 1 and 1000")
N = int(input("N = "))

while N < 1 or N > 1000:
    print("Out of range, please input again")
    N = int(input("N = "))

allsum = 0

while N > 0:
    duplicate = N

    while duplicate > 0:
        reminder = duplicate % 10

        if reminder == 7:
            allsum = allsum + N
            break
        duplicate = duplicate // 10

    if duplicate > 0:
        N = N - 1
        continue

    N = N - 1

print(allsum)

