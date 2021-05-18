def isequal(answer):
    if answer == "yes":
        return True
    return False

def islowerthan(answer):
    if answer == "yes":
        return True
    return False

def main():
    a = 1
    b = 100
    c = (a + b)//2
    print("Memorize a number in range (1, 100)")

    while a // 2 != b // 2:
        answer1 = input("Is your number equal to {}: ".format(c))
        if isequal(answer1):
            print(c)
            break
        answer2 = input("Is your number lower than {}: ".format(c))
        if islowerthan(answer2):
            b = c
        else:
            a = c
        c = (a + b) // 2

main()