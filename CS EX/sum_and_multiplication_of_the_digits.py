N = int(input("Please input a number"))
mysum = 0
myproduct = 1
while N > 0:
    duplicate = N
    remainder = N % 10
    while duplicate > 0:
        mysum = mysum + remainder
        myproduct = myproduct * remainder
        duplicate = (duplicate - remainder) // 10
        remainder = duplicate % 10
    if mysum == myproduct:
        print(N)
        N = N - 1
        mysum = 0
        myproduct = 1
    else:
        N = N - 1
        mysum = 0
        myproduct = 1