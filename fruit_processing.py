# processing list of fruits bought by client
# list of fruits 
fruit_orders = ['banana', 'pineaple', 'orange', 'guava']
fruit_processed = []

for fruit in fruit_orders:
    print(f'You ordered {fruit}')
print("\n")

# processing the fruits
while fruit_orders:
    fruit_processing = fruit_orders.pop()
    print(f'Your {fruit_processing} is being processed')
    fruit_processed.append(fruit_processing)
    
# Deliverying the processed fruits
print('\nThe following fruits have been processed\n')
for processed_fruit in fruit_processed:
    print(f'The fruit: {processed_fruit} is being delivered')
