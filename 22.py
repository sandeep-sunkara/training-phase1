# take int as input from user and check wheaterr if the num is divisible by sum of dig or not
a=int(input("numm: "))
x=a
sum=0
while(a!=0):
    sum=sum+a%10
    a=a//10
if(x%sum==0):
    print("divisible")
else:
    print("not divisible")
    