# write a recursive prog to print rev of num
def revnum(n):
    if(n==0):
        return 0
    print(n%10,end="")
    return revnum(n//10)
revnum(123)