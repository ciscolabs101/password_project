#import regex module
import re

def passwordIsOk():
    """
    passwordIsOk accepts a string password input and will return true or 
    false if the below certain conditions
    
    """
    while True:
        password = input("Enter a password: ")
        if len(password) < 10: #inputed password must be at least 10 char str
            print("Password must have at least 10 characters")
        elif re.search('[0-9]', password) is None:
            print("Password must contain a number")
        elif re.search('[A-Z]', password) is None:
            print("Password must have at least a capital letter")
        elif re.search('[$, #, %, &, *]', password) is None:
            print("Password must contain one special character $, #, %, & or *") #searches if any of the listed special characters is entered
        elif re.search('[\s]', password): #searches for any white spaces entered in password
            print("Password cannot contain a white space")

        else:
            print("Your password meets the requirement proceed")
            break
passwordIsOk() 