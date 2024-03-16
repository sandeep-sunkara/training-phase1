# write a prog to fing the 2nd smallest negative number from list without using pre defined

list1=[22,-1,42,65,1,-4, 6]
l=len(list1)
a=list1[0]
b=9999
for i in range(0,l):
    if (list1[i]<a) and a<b:
        b=a
        a=list1[i]
    # elif(b>list1[i] and b>a):
    #     b=list1[i]
print(b)
# for i in list1[]:


 




