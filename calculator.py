from ArtASCII_images import calculate_image
from clear import clear, exit

def add(n1,n2):
    return n1 + n2
def subtrat(n1,n2):
    return n1 - n2
def multiply(n1,n2):
    return n1 * n2
def divide(n1,n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtrat,
    "*": multiply,
    "/": divide
}

def calculate():
    print('-------SIMPLE CALCULATION --------')
    print(calculate_image)
    num1 = eval(input("Enter your first number: "))
    for key in operations:
        print(key)
    should_continue = True
    while should_continue:
        symbol = input("Pick which operation you want: ")
        num2 = eval(input("Enter your second number: "))
        answer = operations[symbol](num1,num2)
        print(f'The result of {num1} {symbol} {num2} is {answer}')
        
        ans = input('Enter "yes" to continue or "no" start over or "bye" to end: ')
        if ans == 'yes':
            num1 = answer
        elif ans == 'no':
            should_continue = False
            clear()
            calculate()
        else:
            print("Bye for now")
            exit()

calculate()
