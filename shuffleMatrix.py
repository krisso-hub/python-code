import random
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9],[4, 10, 15], [3,5,1]]

for row in range(len(matrix)):
    for column in range(len(matrix[row])):
        i = random.randint(0, len(matrix)- 1)
        j = random.randint(0, len(matrix[row])-1)

        #swap matrix[row][column], matrix[i][j]
        matrix[row][column], matrix[i][j] = \
        matrix[i][j],matrix[row][column]
print(matrix)