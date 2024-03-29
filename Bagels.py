# this is first project in the book


"""Bagles
A deductive logic game where you must guess numbers based on clues
"""

import random

NUM_DIGITS = 3
MAX_GUESSES = 10


def main():
    print('''Bagels, a deductive logic game
    I am thinking of a {} digit numbers wit no repeated digits.
    Try to guess what it is. Here are some clues:
    When I say: That means
    Pico: one digit is correct but in wrong position.
    Fermi: one digit is correct and in right position.
    Bagels:No digit is correct
    For example, if the correct secret number is 248 and your guessis 
    843, the clue would be Fermi Pico.'''.format(NUM_DIGITS))

    while True:
        # This stores the secret number player needs to guess
        secretNum = getSecretNum()
        print("I have thought up a number")
        print('You have {} guesses to get it'.format(MAX_GUESSES))

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Guess #{}:'.format(numGuesses))
                guess = input('> ')

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break
            if numGuesses > MAX_GUESSES:
                print('you run out of guesses.')
                print('The answer was{}'.format(secretNum))
        print('Do you want to play again?(yes or no)')
        if not input('>').lower().startswith('y'):
            break
    print('Thanks for playing')


def getSecretNum():
    numbers = list('0123456789')
    random.shuffle(numbers)
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum


def getClues(guess, secretNum):
    if guess == secretNum:
        return 'you got it'

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Fermi')
        elif guess[i] in secretNum:
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels'
    else:
        clues.sort()
        return ' '.join(clues)


if __name__ == '_main_':
    main()
