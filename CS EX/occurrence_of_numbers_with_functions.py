amountofnums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
def Count(N):
    global amountofnums
    amountofnums[N - 1] += 1

def main():

    while True:
        Number = int(input("Please input a number in range 0-10: "))
        if Number == -1:
            break
        while (Number < 1 or Number > 10) and Number != -1:
            print("Not in range")
            Number = int(input("Input again: "))

        Count(Number)
    print(amountofnums)

main()