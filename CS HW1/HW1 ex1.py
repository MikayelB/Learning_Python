N = int(input("Insert an odd number"))
spase = (N-1) // 2
m = 1

while N % 2 == 0:
    print("Number not odd, insert an odd number")
    N = int(input("Insert an odd number"))

while m <= N:

    print('\n', spase * " ", m * "*", spase * " ")
    m += 2
    spase -= 1





