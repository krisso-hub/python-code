
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ]

print("Type a Message to encode or decode")
direction = input('Do you want to "encode" or "decode"? ')    
text = input("Enter the your message: ").lower()
shift = eval(input("Enter your shift number: "))

def caeser(start_text, shift_no, direction):
    end_text = ""
    if direction == 'decode':
        shift_no *= -1
    for letter in start_text:
        position = letters.index(letter)
        new_position = position + shift_no
        end_text += letters[new_position]
    print(f'the {direction}d text is {end_text}')

    

def encrypt(plain_text, shift_no):
    coded_text = ""
    for letter in plain_text:
        position = letters.index(letter)
        new_position = position + shift_no
        coded_text += letters[new_position]
    print(f'The encrypted text is {coded_text}')

def decrypt(encrypt_text, shift_no):
    coded_text = ""
    for letter in encrypt_text:
        position = letters.index(letter)
        new_position = position - shift_no
        coded_text += letters[new_position]
    print(f'The decrypted text is {coded_text}')

if direction == 'encode':
    encrypt(plain_text= text, shift_no=shift)
elif direction == 'decode':
    decrypt(encrypt_text= text, shift_no= shift)
