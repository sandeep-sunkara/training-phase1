#shift all the zeros to right and dont change order
l=[2,0,1024,0,40,230,0]
a=len(l)
l2=[]
count=0
for i in range(0,a):
    if(l[i]==0):
        count+=1
    else:
        l2.append(l[i])
for i in range(0,count):
    l2.append(0)
print(l2)

