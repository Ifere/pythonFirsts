#The Clair Vojans Game

#random module
import random as r
secretNumber = r.randint(1,20)

#Only 6 guesses allowed
for guessedNumber in range(1,6):

    try:
        number = int(input('Guess which number from 1-20 I picked => '))
        if secretNumber < number:
            print('Guess a little lower')
            print('You have ', str(6 - guessedNumber), ' guesses left!',end='\n\n')

        elif secretNumber > number:
            print('Guess a little higher')
            print('You have ', str(6 - guessedNumber), ' guesses left!',end='\n\n')
        else:
            if secretNumber == number:
                print('Wow, you read my mind')
                print('You got the answer in ',str(guessedNumber),' guess(es)!',end='\n\n')
                break
            else:
                print('You have ', str(6 - guessedNumber), ' guesses left!')
                print("You've run out of guesses ('x')")
                break
    except:
        if ValueError:
            print('Enter valid number within range!',end='\n\n')

/home/ifere/.PyCharm2018.3/config/scratches/guessTheNumber.py