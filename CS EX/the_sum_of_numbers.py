def thesum(something):
    thesum = 0
    for item in something:
        thesum += item
    return thesum

def main():
    mylist = []
    N = 1
    print("Please input 10 numbers:")
    while N <= 10:
        number = int(input())
        mylist.append(number)
        N += 1

    print(thesum(mylist))

main()