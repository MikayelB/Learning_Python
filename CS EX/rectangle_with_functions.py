def printBorderRow(columns):
    for currentcolumn in range(0, columns):
        print("*", end = "")

def printMiddleRow(columns):
    for currentcolumn in range(0, columns):
        if (currentcolumn == 0 or currentcolumn == columns - 1):
            print("*", end = "")
        else:
            print(" ", end = "")

def printRectEmptyMiddle(cols, rows):
    for currentrow in range(0, rows):
        if (currentrow == 0 or currentrow == rows - 1):
            printBorderRow(cols)
        else:
            printMiddleRow(cols)
        print("\n", end = "")

def main():
    columns = 6
    rows = 4
    printRectEmptyMiddle(columns, rows)

main()