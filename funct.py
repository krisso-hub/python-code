
def make_pizza(size, *toppings):
    print(f'\nMaking a {size}-inch pizza with the following toppings:')
    for topping in toppings:
        print(topping)

size = 10
toppings = ['cheese','mayornise']

make_pizza(size, *toppings)
make_pizza(12, 'tomatoes', 'ketchup', 'soy sauce')