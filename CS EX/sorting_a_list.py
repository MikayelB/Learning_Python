mylist = []
secondlist = []
for i in range(0 , 10):
    mylist.append(int(input("Please input a number: ")))
print(mylist)
n = 0
minnum = mylist[0]
while n < 10:
    for character in mylist:
        if minnum > character:
            minnum = character
        else:
            continue
    secondlist.append(minnum)
    mylist.remove(minnum)
    print(minnum)
    print(mylist)
    if mylist == []:
        break
    else:
        minnum = mylist[0]
    n += 1

print (secondlist)