N = int(input("Please input an odd number N = "))
triangle = ""

while N % 2 == 0:
    print("Your number is not odd")
    N = int(input("Please input an odd number N = "))

blank = (N - 1) // 2
star = "*"
k = 1

while k < N + 1:
    triangle = triangle + "\n" + blank * " " + k * "*" + blank * " "
    k += 2
    blank -= 1

print(triangle)