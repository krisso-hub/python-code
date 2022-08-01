import random
from ArtASCII_images import game
from clear import exit

hard_play = 5
soft_play = 10
print('----This guessing game---------')
print(game)
number_play = input("Type 'hard' or 'easy' for difficulty or easy play: ")

def check_guess(guess, secret_number,turns):
    if guess > secret_number:
        print('Your guess too high')
        print(f'You ve {turns} attemps remaining')
    elif guess < secret_number:
        print('Your guess is to low')
        print(f'You ve {turns} attemps remaining')
    elif guess == secret_number:
        print('Congrat you won')
def set_diculty():
    if number_play == "hard":
        return hard_play
    elif number_play == "easy":
        return soft_play

def guess_game():
    secret_number = random.randint(1, 100)
    guess = 0
    turns = set_diculty()
    print(f'For this game you have {turns} attempts to play')
    while guess != secret_number:
        turns -= 1
        guess = eval(input('Guess a number: '))
        check_guess(guess, secret_number,turns)
        if turns == 0 and guess != secret_number:
            print(f'You have {turns} live')
            print(f'The secret number is {secret_number}')
            print('You lost the game')
            should_continue = input('Type "yes" if want to continue otherwise "no": ')
            if should_continue == 'yes':
                guess_game()
            else:
                exit()
guess_game()
    
    



