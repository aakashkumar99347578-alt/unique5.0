def reverse_2d_array_inplace(matrix):
  
    start_row = 0
    end_row = 0

    for row in matrix:
        end_row += 1
    end_row -= 1  
    while start_row < end_row:
        temp = matrix[start_row]
        matrix[start_row] = matrix[end_row]
        matrix[end_row] = temp
        start_row += 1
        end_row -= 1

    for row in matrix:
        start_col = 0
        end_col = 0

        for element in row:
            end_col += 1
        end_col -= 1
        while start_col < end_col:
            temp = row[start_col]
            row[start_col] = row[end_col]
            row[end_col] = temp
            start_col += 1
            end_col -= 1
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

reverse_2d_array_inplace(matrix)
print(matrix)

