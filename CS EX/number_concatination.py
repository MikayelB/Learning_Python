def Concatenate(num1, num2):
    num1 = num1 * (10 ** len(str(num2)))
    concat = num1 + num2
    return concat

def main():
    Number1 = int(input("Please input the first number: "))
    Number2 = int(input("Please input the second number: "))
    print(Concatenate(Number1, Number2))


main()