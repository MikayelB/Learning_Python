mylist = []
for i in range(0 , 10):
    mylist.append(int(input("Please input a number")))
maxnum = mylist[0]
for character in mylist:
    if maxnum < character:
        maxnum = character
    else:
        continue
minnum = mylist[0]
for character in mylist:
    if minnum > character:
        minnum = character
    else:
        continue
print("minnum = " , minnum)
print("maxnum = " , maxnum)
print("mylist = " , mylist)