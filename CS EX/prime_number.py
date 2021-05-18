def IsThisPrime(N):
    for number in range(2, N):
        if N % number == 0:
            return False
    return True

def main():
    Number = int(input("Please input a number: "))
    if IsThisPrime(Number):
        print("It's a prime number")
    else:
        print("Not a prime number")

main()