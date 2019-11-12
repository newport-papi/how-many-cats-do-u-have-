print('How many cats do you have?')
numCats = input()
tup1 = (1, 2, 3)
try:
    if int(numCats) >= 4:
        print('That is a lot of cats.')
    elif int(numCats) == 1:
        print('Nothing wrong with just one cat.')
    elif int(numCats) == 2:
        print('Thats not that many cats.')
    elif int(numCats) == 3:
        print('Thats getting up there.')
    elif int(numCats) == 0:
        print('Not a cat person?')
    elif int(numCats) < 0:
        print('How could you have less then zero cats?')
        
except ValueError:
    print('You did not enter a number.')
    
