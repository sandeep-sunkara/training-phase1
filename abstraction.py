#create a class ticket which will be the abstract class inside that create a function book ticket BOOK which will be the abstract method and has nothing in it
#creat a class makemytrip which will use the book ticket function from ticket class to take the details of such as name,phno,email,journey date and displays a msg saying a msg thankyou booking from mmt
#create a class IRCTC which will use the book ticket function from ticket class and take same details as makemytrip but in the end it will give an option to user to select wheather it is one way or round trip
#if the user option is round trip it again asks the user to enter return date as well and then print msg thank you for choosing irctc else print msg thank you for choosing irctc
#create a class indigo which takes all the details as irctc and just asks which mode of transport you want to go in train,flight or bus, then print hank you for choosing indigo
from abc import ABC,abstractmethod
class ticket:
    @abstractmethod
    def bookticket(self,name,phno,email,jdate):
        pass
class makemytrip(ticket):
    def bookticket(self,name,phno,email,jdate):
        self.name=name
        self.phno=phno
        self.email=email
        self.jdate=jdate
        print("thankyou for booking from mmt")
class irctc(makemytrip):
    def bookticket(self, name, phno, email, jdate):
        print("welcome to irctc:")
        self.jt=input("1.round trip or 2.oneway")
        if(self.jt=="1" or self.jt=="roundtrip"):
            self.rt=input("enter return date:")
            print("tq for choosing irctc")
            print()
        else:
            print("tq for choosing irctc")
            print()
class indigo(irctc):
    def bookticket(self, name, phno, email, jdate):
        print("welcome to indigo:")
        self.mot=input("enter mode of transport: 1.train 2.flight 2.bus")
        print("thank you for choosing indigo")

obj=indigo()
obj1=irctc()
obj2=makemytrip()
obj2.bookticket("sandeep",799,"sandeep@gmail","12-09-12")
obj1.bookticket("sandeep",799,"sandeep@","10-11")
obj.bookticket("sandeep",799,"sandeep@","10-11")