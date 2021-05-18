def CheckIfPalindrome(N):
    duplicate = N
    while duplicate != 0:
        if duplicate % 10 != duplicate // (10 ** (len(str(duplicate)) - 1)):
            return False
        duplicate = (duplicate % (10 ** (len(str(duplicate)) - 1))) // 10
        return True
def main():
    Number = int(input("Please input a number"))
    if CheckIfPalindrome(Number):
        print("It's a palindrom")
    else:
        print("Not a palindrom")

main()