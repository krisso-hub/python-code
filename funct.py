# A function that greet users with a personalized message
def greet_user(names):
    for name in names:
        msg = f'hello, {name.title()}'
        print(msg)

usenames = ['sunday', 'mark', 'mary', 'mathew']
greet_user(usenames)


'''
simulating and processing 3D models from unfinished models
to finished models.
'''
def print_models(uncompleted_models, completed_models):
    while uncompleted_models:
        current_models = uncompleted_models.pop()
        print(f'printing model: {current_models}')
        completed_models.append(current_models)

def show_completed_models(completed_models):
    print('\nprinting completed models:')
    for completed_model in completed_models:
        print(completed_model)

uncompleted_models = ['dashcam', 'robokit', 'lcd']
completed_models = []

print_models(uncompleted_models, completed_models)
show_completed_models(completed_models)


