import sys
from needed_code import Spce


LoginStatus = False




def Login(): 
    global pswrd
    pswrd = str(input("Enter your password: "))
    



Login()


if pswrd == "Admin":
    print()
    print("Access Granted")
    LoginStatus = True 
else:
    tries = 0
    Totaltries = 3
    while(tries < Totaltries):
        tries += 1
        Spce("Try n")
        Login()
    print("Access Denied")
    sys.exit()

print("LoginStatus is: " + str(LoginStatus))