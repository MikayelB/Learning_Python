def MultiplesOfTree(Number):
    sum1 = 0
    for number in range(0, Number):
        if number % 3 == 0:
            sum1 += number
    return sum1

def MultiplesOfFive(Number):
    sum2 = 0
    for number in range(0, Number):
        if number % 5 == 0:
            sum2 += number
    return sum2

def SumOfMultiples(n1, n2):
    thesum = n1 + n2
    print(thesum)

def main():
    thesum = 0
    N = int(input("Please input a number in range 1-1000: "))
    while N < 1 or N > 1000:
        N = int(input("Please input a number in range 1-1000: "))

    first = MultiplesOfFive(N)
    second = MultiplesOfTree(N)
    SumOfMultiples(first, second)

main()