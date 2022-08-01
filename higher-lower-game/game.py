from clear import clear
from art import logo, vs
from game_data import data
import random

# print the data in a formated way
def formated_accout(account):
    '''This return a neated formated data'''
    name_acount = account["name"]
    descr_acount = account["description"]
    country_account = account["country"]
    return f"{name_acount}, {descr_acount}, from {country_account}"

def check_follower(follow_a, follow_b, guess):
    if follow_a > follow_b:
        return guess == "a"
    else:
        return guess == "b"

score = 0
account_b = random.choice(data)
# print the image
continue_game = True
print(logo)
while continue_game:
    # generate random data
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)
    print(f'Compare A: {formated_accout(account_a)}')
    print(vs)
    print(f'Against B: {formated_accout(account_b)}')
    # ask user  to guess
    guess = input("Who has the highest followers, A or B: ").lower()

    # compare the guess with random data
    follow_a  =  account_a["follower_count"]
    follow_b  =  account_b["follower_count"]
    check_result = check_follower(follow_a, follow_b, guess)
    clear()
    # print the result of the comparison
    if check_result:
        # give a score if the guess is correct
        score +=2
        print(f"You got it right, your score: {score}")
        
    else:
        continue_game = False
        print(f"You got wrong, your finalscore: {score}")
   



