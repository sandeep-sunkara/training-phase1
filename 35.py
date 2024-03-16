#write the rcursive function to count no. of dig of a num

def cou(n):
    if n==0:
        return 0
    return 1+cou(n//10)
print(cou(0))
