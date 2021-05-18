def InversedNumber(Number):
    Inversed = 0
    while Number != 0:
        Inversed = Inversed * 10 + Number % 10
        Number = Number // 10
    return Inversed


def main():
    N = int(input("Please input anumber: "))
    print(InversedNumber(N))

main()