email = input("Enter your Email Address: ")

def checkEmail(email):
    if len(email) < 6:
        print("Email must contain at least 6 characters")
        return False
    
    elif not (email[0].isdigit() or email[0].isalpha()):
        print("Email must start with a letter or digit")
        return False
    
    elif email.count("@") != 1:
        print("Email must contain exactly one '@' symbol")
        return False
    

    endings = [".com", ".org", ".edu", ".net", ".co", ".io", ".ai"]
    if not any(email.endswith(ending) for ending in endings):
        print("Email must end with one of the following: '.com', '.org', '.edu', '.net', '.co', '.io', '.ai'.")
        return False



    elif any(char.isspace() for char in email):
        print("Donot use Space")
        return False
    return True


if checkEmail(email):
    print("Valid Email Address")
else:
    print("Invalid Email Address")
