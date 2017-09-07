print('Hello, you.')
print('What is your name?')
name = input()
print('And how many children do you have?')
kidCount = input()
if name == 'Dad':
    continue
while name == 'Mom':
    if int(kidCount) == 2:
        print('Hi, Mom.')
        break
    while int(kidCount) != 2:
        if int(kidCount) > 2:
            print('WHAT ARE YOU HIDING FROM ME')
        if int(kidCount) < 2:
            print('Are you forgetting someone, or are you not my real mom?')
        print('Let\'s try again. How many kids do you have?')
        kidCount = input()
else:
    print('Nice to meet you, ' + name)
