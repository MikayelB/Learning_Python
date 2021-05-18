N = int(input("Input a number: "))
mystr = ""
while N != 0:
    if N % 2 == 0:
        mystr = "0" + mystr
        N = N // 2
    else:
         mystr = "1" + mystr
         N = N // 2

print(mystr)
k = list(input())
print(k)