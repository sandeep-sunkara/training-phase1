#program to check type of triangle where take i/p from user for 3 sides and classify accordingle into equl,iso,scaleint 

a=int(input("1st:"))
b=int(input("2nd:"))
c=int(input("3rd:"))

if a==b and b==c:
    print("equilateral")
elif a==b or b==c or a==c:
    print("isoceles")
else:
    print("Scalance")