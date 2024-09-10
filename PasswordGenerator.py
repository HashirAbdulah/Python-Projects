import string
import random

length = int(input("Enter Password Length: "))
letters = string.ascii_letters
numbers = string.digits
punctuations = string.punctuation

plist=[]
plist.extend(letters)
plist.extend(numbers)
plist.extend(punctuations)

random.shuffle(plist)
print(''.join(plist[0:length]))
