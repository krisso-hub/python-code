# Generate password of any lenght with letters, symbols and numbers
import random
password_list = []

# alphanumeric and symbols in list variable
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
symbols = ['@', '#', '%', '&' '*', '!', '^', '?']

#User gives the numbers of letter, numbers and symblos
print('Password Generator ....................................')
print('Specify the numbers of letters, numbers and symbols....')
num_letters = eval(input('Enter how many letters do you want: '))
num_numbers = eval(input('Enter how many numbers do you want: '))
num_symbols = eval(input('Enter how many symbols do you want: '))

for letter in range(1, num_letters +1):
    nums_letter = random.choice(letters)
    password_list.append(nums_letter)

for no in range(1, num_numbers+1):
    number = str(random.choice(numbers))
    password_list.append(number)

for sym in range(1, num_symbols+1):
    symbol = str(random.choice(symbols))
    password_list.append(symbol)

#shuffle the list of password generated
random.shuffle(password_list)
password = ''.join(password_list)

print(password)




