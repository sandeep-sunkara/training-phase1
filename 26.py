#armsstrong
a=input("num:")
b=int(a)
e=int(a)
c=len(a)
sum=0
while(b!=0):
    sum=sum+(b%10)**c
    b=b//10
print(sum)
if(e==sum):
    print("arm")
else:
    print("not")

