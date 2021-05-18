def askUserToInput():
    number = int(input("Please input a number in range 1-2000: "))
    return number
def MaxNumber(numbers):
    maxnum = numbers[0]
    for i in range(0, len(numbers)-1):
        if numbers[i] <= numbers[i+1]:
            maxnum = numbers[i+1]
        else:
            maxnum = numbers[i]
            numbers[i+1] = numbers[i]
    return maxnum
def main():

    numbers = []
    step = 1
    while step <=100:
        number = askUserToInput()
        while number < 1 or number > 2000:
            print("Number is out of range")
            number = askUserToInput()
        numbers.append(number)
        step += 1
    print(MaxNumber(numbers))
main()