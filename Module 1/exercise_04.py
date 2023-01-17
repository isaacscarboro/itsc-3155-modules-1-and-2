x = int(input('Enter a number: '))
theList = list()
total = 0
for y in range (x):
    temp = float(input('Enter a number ' + str(y +1) + ': '))
    theList.append(temp)
    total = total + temp
print('List: '+ str(theList))

print('Average:' + str(total / x)) 
    
