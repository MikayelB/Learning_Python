## First way
# def OddNumber(N):
#     if N % 2 == 1:
#         return True
#     else:
#         return False
#
# def CheckForPowerTwo(N):
#     while N != 1:
#         if OddNumber(N) == True:
#             return False
#         else:
#             N = N // 2
#     return True


# Second way
def CheckForPowerTwo(N):
    while N != 1:
        if N % 2 == 1:
            return False
        else:
            N = N // 2
    return True

def main():
    Number = int(input("Please input a number: "))
    if CheckForPowerTwo(Number):
        print ("It's a power of two")
    else:
        print("Not a power of two")


main()