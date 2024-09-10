import re


pattern =  r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

email = input("Enter Email Adress: ")

if re.match(pattern, email):
    print ("Valid Email Adress:")
else:
    print ("Invalid Email Address")

