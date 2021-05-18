def Reversed(somelist):
    reversedone = []
    for index in range(len(somelist) - 1, -1, -1):
        reversedone.append(somelist[index])
    return reversedone

def main():
    k = 1
    firstlist = []
    print("Please input ten numbers: ")
    while k <= 10:
        N = int(input())
        firstlist.append(N)
        k = k + 1
    print(Reversed(firstlist))

main()