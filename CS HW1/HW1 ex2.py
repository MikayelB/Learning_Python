N = int(input("Insert a number from 1 to 1000"))

while N < 1 or N > 1000:
     print("This number isn't between 1 and 1000, insert one from 1 to 1000")
     N = int(input())

if N > 1:
  if N < 1000:
    total = 0
    for k in range (1,N):
      x = k
      while x != 0:
        if x%10 == 7:
          total = total + x
          x = 0
        x = x / 10
    print(total)