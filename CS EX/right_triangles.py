def DrawSecondTriangle(rows):
    for currentrow in range(rows-1, -1, -1):
        print(currentrow * " " + (rows - currentrow) * "*")

def DrawFirstTriangle(rows):
    for currentrow in range(1, rows + 1):
        print(currentrow * "*")

def main():
    N = int(input("Please input the height of a triangle: "))
    DrawFirstTriangle(N)
    DrawSecondTriangle(N)


main()