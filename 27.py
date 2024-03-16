# a=1578
# c=str(a)
# b=len(c)
# sum=0
# while(b!=0):
#     sum=sum+(a%10)**b
#     a=a//10
#     b-=1
# print(sum)
a=1578
n=a
count=0
sum=0
while(a!=0):
    a=a//10
    count=count+1
print(count)
while(count!=0):
    sum=sum+((n%10)**count)
    n=n//10
    count-=1
print(sum)