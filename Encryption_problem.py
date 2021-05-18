character = ""
previousone = ""
nextone = ""
while True:
    character = input("Input character ")

    if len(character) != 1:
        continue

    elif character == "a":
        if previousone == "o":
            print("O")
            print("A")
        else:
            print("A")
        nextone = ""

    elif character == "e":
        if previousone == "o":
            print("O")
            print("E")
        else:
            print("E")
        nextone = ""

    elif character == "i":
        if previousone == "o":
            print("O")
            print("I")
        else:
            print("I")
        nextone = ""

    elif character == "u":
        if previousone == "o":
            print("O")
            print("U")
        else:
            print("U")
        nextone = ""

    elif character == "x":
        if previousone == "o":
            print("O")
            print("boo")
        else:
            print("boo")
        nextone = ""

    elif character == "6" or character == "7" or character == "8" or character == "9":
        continue

    elif character == "o":
        if previousone == "o":
            print("O")
        previousone = character

    elif character == "k":
        if previousone == "o":
            previousone = ""
            print("good")
        else:
            print(character)

    elif character == "-":
        if previousone == "-":
            print("-")
        previousone = character

    elif character == "1":
        if previousone == "-":
            break
        else:
            print(character)

    else:
        nextone = ""
        previousone = ""
        print(character)