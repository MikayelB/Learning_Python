def IsThisPrime(N):
    for number in range(2, N):
        if N % number == 0:
            return False
    return True

def AllPrimesBefore(N):
    for number in range(2, N):
        if IsThisPrime(number):
            print (number)
        else:
            continue

def main():
    Number = int(input("Please input a number: "))
    AllPrimesBefore(Number)


main()