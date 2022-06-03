cat_names = []

while True:
    print('Enter the names of your cat: ')
    cats = input()
    if cats == 'q':
        break
    cat_names.append(cats)

for cat in cat_names:
    print(cat)
print(cat_names)

