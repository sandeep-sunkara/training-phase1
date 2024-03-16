#writre a program in which take int input from user 
#if that int is divisible by 3 and 6 print good no. 
#if the int is divisible by 2&7 print avg no.
#if divisible by 4or9 print awesome 
#else bad

a=int(input("num:"))

if a%3==0 and a%6==0:
    print("good num")
elif a%2==0 and a%7==0:
    print("avg")
elif a%4==0 or a%9==0:
    print("awesome")
else:
    print("bad")
