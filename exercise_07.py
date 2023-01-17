x = 0
myList = list()
evenList = list()
while str(x) != 'QUIT':
    x = input('Enter a number or QUIT to quit:' )
    if x != 'QUIT':
        myList.append(int(x))
        if int(x) % 2 == 0:
            if (int(x) in evenList) == False:
                evenList.append(int(x))
print('All Nums: ' + str(myList))

print('Even Nums: ' + str(evenList))
        
