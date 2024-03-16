#calculate the sum of digits of a number 

a=int(input("...."))
sum=0
while(a>0):
    b=a%10
    sum=sum+b
    a=a//10
print(sum)