import string
import random

length = int(input("Enter Password Length: "))
letters = string.ascii_letters
numbers = string.digits
punctuations = string.punctuation
passw = letters + numbers + punctuations
password = ""

if length < 8 :
    print("Password length should be at least 8 characters")
else:
    for i in range(length):
        password += random.choice(passw)

    print(password)
    
