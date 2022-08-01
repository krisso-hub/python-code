# Decide who should Rollercoster and ticket price



print('Rollercoster riding............................')
print('if you want to ride answer this questions......')
height = eval(input('Whats is your height? '))

bill = 0
if height > 1.8:
    print('Yea, you are qualified to ride Rollercoster')
    age = eval(input('Whats your age? '))
    if age < 12:
        bill = 5
        print('Your ticket price is $5')
    elif age < 18:
        bill = 8
        print('Your ticket price is $8')
    else:
        bill = 12
        print('Your ticket price is $12')
    add_photo = input('Extra $3 to take pictures? yes or no: ')
    if add_photo == 'yes':
        bill += 3
    print(f'Your total ticket price is ${bill}')

else:
    print('Sorry you cant ride Rollercoster, Your height is low')
