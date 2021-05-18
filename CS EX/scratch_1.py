def printmystr(mystr, makeuppercase):
    if makeuppercase:
        print(mystr.upper())
    else:
        print(mystr)
def main():
    printmystr("Tree", True)
    print("I am main function")

main()