###positional arguments
# def posarg(a,b):
#     print("this is positional arguments program")
#     print("a:",a,"b:",b)
# posarg(10,20)

###default arguments
# def defarg(a=10,b=20):
#      print("this is default values program")
#      print("a:",a,"b:",b)
# defarg()
# defarg(15,30)

# def keyarg(a,b):
#     print("a:",a,"b:",b)    
# keyarg(b=11,a=12) 

###unknown arg
def unkarg(**name):
    print("name:",name["fname"])
    print("name:",name["lname"])
unkarg(fname="sandeep",lname="sunkara",)