def isequal(num1, num2):
    if num1 == num2:
        return True
    return False

def islow(num1, num2):
    if num1 < num2:
        return True
    return False

def ishigh(num1, num2):
    if num1 > num2:
        return True
    return False

def generatenumber(min, max):
    from random import randint
    number = randint(min, max)
    return number

def main():
    secret = generatenumber(1, 100)
    step = 0
    while step < 7:
        number = int(input("Please guess a number"))

        if isequal(number, secret):
            print("Correct")
        elif islow(number, secret):
            print("Low number")
        elif ishigh(number, secret):
            print("High number")

        step += 1
main()