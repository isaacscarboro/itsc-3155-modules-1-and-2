x = int(input('Enter a row num from 1 to 5: '))
y = int(input('Enter a col num from 1 to 5: '))
for z in range (5):
    for c in range(5):
        if x == (z+1) and y == (c+1):
            print(' 1 ', end="")
        else:
            print(' 0 ', end="")
    print();
