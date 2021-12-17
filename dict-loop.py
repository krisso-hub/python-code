
user_01 = {
    'username': 'femi-bobo',
    'fname': 'femi',
    'lname': 'dana'
}

for key, value in user_01.items():
    print(f'\nkey: {key}')
    print(f'value: {value}')

favourite_langauge = {
    'james': 'python',
    'john': 'nodejs',
    'jane': 'Go',
    'janet': 'java',
    'johnson': 'javascript'
}

for name, lang in favourite_langauge.items():
    # print(f'\n the favorite languge of {name.title()} is {lang.title()}')
    print(f"\n{name.title()}'s favorite language is {lang.title()}")

for name in favourite_langauge.keys():
    print(f'\n hi {name.title()}')

    