# calculate the difference of  sum of nums that are divisible by 6 not div by 6 in the range of 1st 30 nums
sum1,sum2=0,0

for i in range(1,31):
    if(i%6==0):
        sum1=sum1+i
    else:
        sum2=sum2+i
orgsum=abs(sum2-sum1)
print(orgsum)