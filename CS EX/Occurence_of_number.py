mylist = [0,0,0,0,0,0,0,0,0,0]
while True:
    N = int(input("Input a number in range 1 - 10: "))

    if N == -1:
        break
    elif N > 10 or N < 1:
        print ("Out of range, input again")
    else:
        mylist[N-1] += 1

print(mylist)

