a=int(input())
n=a
num=0
while(a!=0):
    num=num*10+a%10
    a=a//10
if(n==num):
    print("pal")
else:
    print("no pal")