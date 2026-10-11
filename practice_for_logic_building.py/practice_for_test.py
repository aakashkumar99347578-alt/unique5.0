""" def traverse(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j],end=" ")
        print()
 """

""" def transpose_squre(matrix):
    for i in range(len(matrix)):
        for j in range(i+1,len(matrix)):
            temp = matrix[i][j]
            matrix[i][j]=matrix[j][i]
            matrix[j][i]=temp
    return matrix

 """

def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    result = [[0]*rows for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            result[j][i]=matrix[i][j]
    return result



row = int(input("enter the row number"))
col = int(input("enter the coloumn number"))
matrix = []
for i in range(row):
    rows = []
    for j in range(col):
        value = int(input(f"enter the element at index positions at  {[i]}{[j]} "))
        rows.append(value)
    matrix.append(rows)

print(matrix)
""" traverse(matrix) """
""" print(transpose_squre(matrix)) """
print(transpose(matrix))
