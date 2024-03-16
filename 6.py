#program to check the onroad price of bike
#conditions:
#if price is >72000 and <150000then income taxes 10% of original price and insurence will be 15% of the actual price 
#if the price is >1,50,000 and less than 2,00,000 the tax would be 25% and insurence 20%
#if the price is >2,00,000 then 35% and insurence will be 28%
#else min price with us start from 72k enter valid value
#print onroad price of bike formula=actprice+tax+insurence

a=int(input("price:"))
if a>72000 and a<=150000:
    b=a+0.1*a+0.15*a
    print("onroad price is :",b)
elif a>150000 and a<=200000:
    b=a+0.25*a+0.20*a
    print("onroad price is :",b)
elif a>200000:
    b=a+0.35*a+0.28*a
    print("onroad price is :",int(b))
else:
    print("min price with us start from 72k enter valid value")