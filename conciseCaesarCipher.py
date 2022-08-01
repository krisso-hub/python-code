

chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ]


#Generate caeser cipher chars
def caeser(start_text, shift_no, caeser_direction):
    end_text = ""
    if caeser_direction == 'decode':
        shift_no *= -1
    for char in start_text:
        if char in chars:
            position = chars.index(char)
            new_position = position + shift_no
            end_text += chars[new_position]
        else:
            end_text += char
    print(f'the {caeser_direction}d text is {end_text}')

import ArtASCII_images
print(ArtASCII_images.mystic)
should_continue = True
while should_continue:
    print("Type a Message to encode or decode")
    direction = input('Do you want to "encode" or "decode"? ')    
    text = input("Enter the your message: ").lower()
    shift = eval(input("Enter your shift number: "))
    shift = shift % 26
    caeser(start_text= text, shift_no= shift, caeser_direction= direction)
    result = input('Type "yes" if you want to continue of "no" to end: ')
    if result == 'no':
        should_continue = False
        print('Good Bye')




    