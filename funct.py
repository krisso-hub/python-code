# A function that greet users with a personalized message
def greet_user(names):
    for name in names:
        msg = f'hello, {name.title()}'
        print(msg)

usenames = ['sunday', 'mark', 'mary', 'mathew']
greet_user(usenames)