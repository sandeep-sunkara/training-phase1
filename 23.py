# take num input from user check if the sum of fact of that num is greater than the org num or not if yes prnt abundant else no
a=int(input("num:"))
sum=0
for i in range(1,a//2+1):
    if(a%i==0):
        sum=sum+i
print("the sum is :",sum)
if(sum>a):
    print("abundant")
else:
    print("no")