#recursive fun for to calculate sum of dig of a number
def cou(n):
    if n==0:
        return 0
    return n%10+cou(n//10)
print(cou(1235))