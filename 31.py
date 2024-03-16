#login fun
def called():
    while True:
        name=input("name:")
        passw= input("pass:")
        if(name==passw):
            print("login successful")
            break
        else:
            print("Enter your credentials again")
called()

        