import csv
class register:
    def reg(self):
        f=open("custdata.csv","a",newline="")
        a=csv.writer(f)
        print("enter your details:")
        self.uname=input("enter username:")
        self.phno=int(input("enter phone number:"))
        self.adress=input("enter address:")
        self.pin=input("Enter your area Pin:")
        self.password=input("Enter your password:")
        a.writerow([self.uname,self.phno,self.adress,self.pin,self.password])
        print("Registration successful")
    def login(self,uname,password):
        with open("custdata.csv","r",newline="") as file:
            read=csv.DictReader(file)
            for row in read:
                if row['uname']==uname and row['password']==password:
                    return True
        




# class auth:
#     def __init__(self,a,b): 
#         self.a=a
#         self.b=b
#     def registration
#     def autentication(self) :
#         if(self.a==self.b):
#             print("login successful")
#             return True
#         else:
#             print("check your credentials and try again")