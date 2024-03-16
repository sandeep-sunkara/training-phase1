# # #CAR SHOWROOM
# # #3 companies toyota,mahindra,mercedes
# # #take i/p from user for car company name and in input msg give user three companies this user i/p comp nmae goes as input/argument to
# # #model name,which welcomes the user accordingly to company name.ask the user to enter the specific model name for that company
# # #tge second function is variant according to the company name and car model the user should be asked to enter the varient he would like to choose from
# # #petrol,diesel
# # #the last disp function according to the car company car model and car varient 1st its ex-showroom price should be displayed and then its on road price
# # #whic is calculated as ex-showroom price + cgst+sgst+insurence.
# # #sgst ,cgst and insurence all the three have common value throughtout the carshowroom

# # print("avaliable companies:")
# # print("1.toyota")
# # print("2.mahindra")
# # print("3.mercedes")

# # class carshowroom:
# #     def toyota(self):
# #         print("welcome to toyota family:"'\n'"Avaliable models:"'\n'"1.A-model"'\n'"2.B-model")
# #         self.m=input("select a model:")
# #         return o.varient()
    
# #     def varient(self):
# #         v=input("petrol or diesel:")
        
# #     def mahindra(self):
# #         print("welcome to mahindra family:")
# #         print("Avaliable models:"'\n'"1.C-model"'\n'"2.D-model")
# #         m=input("select a model:")
# #     def mercedes(self):
# #         print("welcome to mercedes family:")
# #         print("Avaliable models:"'\n'"1.E-model"'\n'"2.F-model")
# #         m=input("select a model:")

# # a=input("Enter company name:")
# # o=carshowroom()
# # if(a=="toyota"):
# #     o.toyota()
# # elif(a=="mahindra"):
# #     o.mahindra()
# # elif(a=="mercedes"):
# #     o.mercedes()
# # user_input = input("Enter a string or an integer: ")
# # if (user_input=="sandeep"):
# #    print("hai")
# # else:
# #    print("oyr")
# cn=input()
# if isinstance(cn, str):
#     cn = cn.lower()
# print(cn)



import sys

highest_int_value = sys.maxsize
print("Highest integer value:", highest_int_value)
