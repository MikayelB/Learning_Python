def isequal(number):
    print("Is your number ", number, " ?")
    answer = input("Please wright yes or no: ")
    if answer == "yes":
        return True
    return False

def islowerthan(number):
    print("Is you number lower then ", number, " ?")
    answer = input("Please wright yes or no: ")
    if answer == "yes":
        return True
    return False

def ishigherthan(number):
    print("Is your number higher than ", number, " ?")
    answer = input("Please wright yes or no: ")
    if answer == "yes":
        return True
    return False

def main():
    a = 1
    b = 100
    c = (a + b)//2
    print("Memorize a number in range (1, 100)")

    while a // 2 != b // 2:

        if isequal(c):
            print(c)
            break
        elif islowerthan(c):
            b = c
        elif ishigherthan(c):
            a = c
        c = (a + b) // 2

main()