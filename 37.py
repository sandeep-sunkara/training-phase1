def count(c):
    if c==0:
        return 0
    return 1+count(c//10)
def arm(n):
    if n==0:
        return 0
    return ((n%10)**cou)+arm(n//10)

n=int(input())
cou=(count(n))
print(cou)
if(arm(n)==n):
    print(n,"is armstrong")
else:
    print(n,"is not armstrong")