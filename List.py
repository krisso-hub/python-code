# cube list of numbers and print the output
list_numbers = []
numbers = list(range(3, 31, 3))
for number in numbers:
    list_numbers.append(number**3)

print(list_numbers)

# A list of multiples of three(3)
list_multiples = []
num = list(range(3, 30))
for number in num:
    list_multiples.append(number*3)
print(list_multiples)

#cube comprehention to generate list 
list_numbers = [number**3 for number in range(3, 31, 3)]
print(list_numbers)

#list slicing
foods = ["rice", "garri", "yam", "bacon", "beef steak" ]
print("the food from the beginning are: ") 
print(foods[:])
print("\n the first three food are:")
print(foods[:3])


#copying list to another list
my_foods = foods[:]

my_foods.append("moi moi")
print(my_foods)
print(my_foods)