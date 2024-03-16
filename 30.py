#write a func to calvulate sumof 1st and last dig of num

def func(a):

    b=a%10
    while a!=0:
        a=a//10
        if(a!=0):
            c=a
    sum=b+c
    print(sum)
func(4056)