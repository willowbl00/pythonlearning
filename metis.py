#After each guess the program will say whether the answer is too low, too high, or
#correct, and after 10 guesses or one correct guess the game will end. At the end
#of the game the program will say the player has won or lost.

#generate random number
import random #imports ability to select random numbers
secret_number = random.randint(1,100) #generates a random number between 0 and 100)

#ask for a guess
for guesses_taken in range(1,10): #allows for 10 rounds of guessing
    print('Guess a number between 0 and 100.')
    guess = int(input()) #changes input to an integer
#compare guess to random number
    if guess < secret_number:
        print('Your guess was too low.')
    elif guess > secret_number:
        print('Your guess was too high.')
    else:
        break #no longer need to ask for guesses
#resolve due to correct guess or out of chances to guess
if guess == secret_number: #need to prompt program to respond if it IS correct
    print('You guessed right! This is a direct reflection of your moral character!')
else:
    print('Well. The number number was '+str(secret_number)) #converts secret number to a string so it can be appended
