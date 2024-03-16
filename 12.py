a=int(input("enter"))
flag=0

for i in range(2,a+1):
 if(a==i):
  print("prime")
  break
 elif a%i==0:
  print("not prime")
  break
 
