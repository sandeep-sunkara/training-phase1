#palindrome or not
def pal(n):
    if n==0:
        return 0
    else:
       
        return n%10*10+pal(n%10)
n=int(input())
a=1
if n==pal(n):
    print(pal(n))
    print("it is palimdrome")
else:
    print("not")
    print(pal(n))


# a="hey"
# print(a[1])