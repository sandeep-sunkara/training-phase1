#CHECK  a given yr is leap or not
#conditions:
#if yr is divisible by 4 and not div by 100 or if div by 400 then it is call leap
year=int(input("enter year:"))
if year%4==0 and year%100!=0:
    print("leap year")
elif year%400==0:
    print("leap year")
else:
    print("not leap")