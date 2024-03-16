# write a function which takes two arguments a and b type cast the value of sencond argument into int then multiply both arguments and print the 
# last digit of result

def hey(a,b):
    c=int(b)
    d=a*c
    ld=d%10
    print("last digit =",ld)
a=int(input())
b=float(input())
hey(a,b)
