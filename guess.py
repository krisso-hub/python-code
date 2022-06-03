import random

secret_number = random.randint(1, 30)
number = 5
for guess_taken in range(1, 5):
    number -=1
    print("Guess a secret number")
    guess = int(input())

    if guess < secret_number:
        print(number)
        print('your guess number is low, try again')

    elif guess > secret_number:
        print(number)
        print('your guess number is high, try again')
    elif guess == secret_number:
        print(number)
        print(f'Yaa! you got the correct number {secret_number} in {guess_taken} guesses')
    else:
        print(f'Naa! You did not get the correct number in {guess_taken} guesses')

print(f'the secret number is {secret_number} and your number of attemps is exhausted, start all over')