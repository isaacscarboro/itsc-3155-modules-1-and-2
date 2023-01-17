myString = input('Enter a string: ')
newString = ""
for x in range(len(myString)):
    newString = newString + myString[(len(myString)) - x - 1]
print(newString)
