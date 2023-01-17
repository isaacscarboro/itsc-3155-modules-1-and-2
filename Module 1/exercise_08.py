x = 0
myList = list()
oneList = list()

for x in range(10):
    y = int(input('Enter number ' + str(x+1) + ': '))

    if (int(y) in myList) == False:
         oneList.append(int(y))
    else:
         oneList.remove(int(y))
    myList.append(int(y))
print('Original List: '+ str(myList))
print('Nums that appear once: '+ str(oneList))
        
         
