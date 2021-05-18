def checkdescending(somelist):
    for index in range(0, len(somelist) - 1):
        if somelist[index] > somelist[index + 1]:
            return True
        else:
            return False

def checkascending(somelist):
    for index in range(0, len(somelist)-1):
        if somelist[index] < somelist[index + 1]:
            return True
        else:
            return False

def main():
    N = 1
    thelist = []
    print("Please input 10 numbers: ")
    while N <= 10:
        number = int(input())
        thelist.append(number)
        N += 1
    if checkascending(thelist):
        print("Your numbers are in ascending order")
    elif checkdescending(thelist):
        print("Your numbers are in descending order")
    else:
        print("No")

main()