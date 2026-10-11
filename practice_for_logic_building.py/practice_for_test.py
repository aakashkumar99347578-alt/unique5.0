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




row = int(input("enter the row number"))
col = int(input("enter the coloumn number"))
matrix = []
for i in range(row):
    rows = []
    for j in range(col):
        value = int(input(f"enter the element at index positions at  {[i]}{[j]} "))
        rows.append(value)
    matrix.append(rows)

""" print(matrix) """
""" traverse(matrix) """
""" print(transpose_squre(matrix)) """

