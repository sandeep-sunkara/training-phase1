#addition of min and max replace max num with sum and min num is subtra
mylist=[12,42,23,96,7,18,10,133]
print(mylist)
a=mylist[0]
b=mylist[0]
minid=0
maxid=0
for i in range (0,len(mylist)):
    if(a>mylist[i]):
        a=mylist[i]
        minid=i
    if(b<mylist[i]):
        b=mylist[i]
        maxid=i
print(a+b)
print(b-a)
mylist[minid]=b-a
mylist[maxid]=a+b
print(mylist)