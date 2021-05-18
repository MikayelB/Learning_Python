
def isInRange(number, minvalue, maxvalue):
    if number < minvalue or number > maxvalue:
        return False
    else:
        return True

def doesContainDigit(number, digit):
    duplicate1 = number
    while duplicate1 > 0:
        remainder1 = duplicate1 % 10
        if remainder1 == digit:
            return True
        duplicate1 = duplicate1 // 10
    return False


def calcSumOfDigits(number):
    duplicate2 = number
    sumofdigits = 0
    while duplicate2 > 0:
        reminder2 = duplicate2 % 10
        sumofdigits = sumofdigits + reminder2
        duplicate2 = duplicate2 // 10
    return sumofdigits

def main():
    number = int(input("Input a number"))
    while number < 1 or number > 1000:
        print("Not in range")
        number = int(input("Input again"))
    if isInRange(number, 1, 1000):
        if doesContainDigit(number, 7):
            print(calcSumOfDigits(number))
        else:
            print("Doesn't contain the digit")
    else:
        print("Is out of range")
main()