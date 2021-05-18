def AskUserToInput():
    current_list = []
    number = int(input("Please input a number: "))
    while number != -1:
        number = int(input("Please input a number: "))
        current_list.append(number)
    return current_list

def CalcTheOccurrence(number):
    occurrence = 0
    for i in range(0, len(mylist)):
        if number == mylist[i]:
            occurrence += 1
    return occurrence

def main():

    for i in range(1, 11):
        occurrence = CalcTheOccurrence(i)
        print(i, "occurred", occurrence, "times")
mylist = AskUserToInput()
main()