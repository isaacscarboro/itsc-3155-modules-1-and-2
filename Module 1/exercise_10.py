myList = list()
tempList = list()
y = str(input('Enter a string: '))
x = 0
while x< len(y):
    for z in range(3):
            if(x < len(y)):
                tempList.append(y[x])
                x = x+1
           
    myList.append(str(tempList))
    tempList.clear()
print(str(myList))
