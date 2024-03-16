a=12345
mul=1
sum=0
print("digits are:")
 
while(a!=0):
    x=a%10
    a=a//10
    mul=mul*x
    sum=sum+x
    print(x)
print("mul of digits:",mul)
print("sum of digits:",sum)