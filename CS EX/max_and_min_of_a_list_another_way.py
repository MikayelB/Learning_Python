mylist = []
for i in range(0 , 10):
    mylist.append(int(input("Please input a number")))
minnum = mylist[0]
maxnum = mylist[0]
for character in mylist:
    if maxnum < character:
        maxnum = character
    elif minnum > character:
        minnum = character
print(maxnum)
print(minnum)