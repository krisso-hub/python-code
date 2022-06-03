'''A silent bidding program that keeps tracks of bidders
   and the their bidding price and declare the highest
   bidder as the winner at the end of bidding
'''

from clear import clear
from ArtASCII_images import game

#Verifies who bid highest price 
def check_winner(bidders):
    winner = ''
    max_score = 0
    for bidding in bidders:
        if bidders[bidding] > max_score:
            max_score = bidders[bidding]
            winner = bidding
    print(f'{winner} is the winner with the winning price of ${max_score}')



bid = {}
should_continue = False
while not should_continue:
    print(game)
    print('The bidding is on-----------------')
    print('This is your time to bid -------')
    name = input("Whats your name?: ").capitalize()
    price = eval(input("How much do you want to bid?: $"))
    bid[name]= price

    result = input('Does any one still want to be bid "yes" or "no": ')
    if result == 'yes':
        clear()
    else:
        should_continue = True
        check_winner(bid)


