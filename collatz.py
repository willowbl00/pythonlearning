print('Type a number. We will run Collatz against it until it arrives at 1.')
number = int(input())

def collatz(number):
    while number > 1:
        if number % 2 == 0: #This means it's an even number
            print(number)
            number = number // 2
        else:
            print(number)
            number = 3 * number + 1
    if number == 1:
        print(number)
collatz(number)

