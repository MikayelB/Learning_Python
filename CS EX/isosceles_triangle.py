def DrawTriangle2(columns):
    blank = columns // 2
    numofstars = 1
    while numofstars <= columns:
        print(blank * " " + numofstars * "*" + blank * " ")
        blank -= 1
        numofstars += 2

def DrawTriangle1(rows):
    columns = 2 * rows - 1
    DrawTriangle2(columns)


def main():
    Number = int(input("Please input a number: "))
    DrawTriangle1(Number)
    while Number % 2 == 0:
        Number = int(input("Please input an odd number for the second triangle: "))
    DrawTriangle2(Number)

main()