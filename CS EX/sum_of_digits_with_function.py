def SumOfDigits(N):
    thesum = 0
    while N != 0:
        thesum += N % 10
        N = N // 10
    return thesum
def main():
    N = int(input("Please input a number: "))
    print(SumOfDigits(N))

main()