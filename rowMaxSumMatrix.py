matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9],[4, 10, 15], [3,5,1]]

maxRow = sum(matrix[0])
indexMaxRow = 0

for row in range(1, len(matrix)):
    if sum(matrix[row]) > maxRow:
        maxRow = sum(matrix[row])
        indexMaxRow = row
print('The row', indexMaxRow, 'has the maximum sum of', maxRow)
