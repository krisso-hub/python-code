number_elements = 5 # Number of elements
sum = 0 # sum of the elements
numbers = []

for i in range(number_elements):
    element = eval(input("Enter any number: "))
    numbers.append(element)
    sum += element
    average = sum/number_elements

count = 0 # the number of elements above average
for i in numbers:
    if i > average:
        count += 1
print('The average of the numbers is ', average)
print("the list is", numbers)
print('The numbers of elements bigger than average is', count)
