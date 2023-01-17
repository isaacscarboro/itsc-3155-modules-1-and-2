myString = input('Enter a string: ')
newString = ""
lowerCase = ""
upperCase = ""
for x in range(len(myString)):
    if myString[x] != ' ':
        
        if myString[x].isupper():
            upperCase = upperCase + myString[x]
        else:
            lowerCase = lowerCase + myString[x]
newString = lowerCase + upperCase
print(newString)
