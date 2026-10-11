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

""" def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    result = [[0]*rows for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            result[j][i]=matrix[i][j]
    return result
 """
""" def upper_triangle(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j>=i:
                print(matrix[i][j],end=" ")
            else:
                print("*",end=" ")
        print()

def lower_triangle(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j<=i:
                print(matrix[i][j],end=" ")
            else:
                print("*",end=" ")
        print()
 """

""" size = int(input("enter the size of matrix"))
for i in range(size):
    for j in range(size):
        if i==j:
            print(1,end=" ")
        else:
            print(0,end=" ")
    print()
 """

""" def ninty(matrix):
    for i in range(len(matrix)):
        for j in range(i+1,len(matrix)):
            temp = matrix[i][j]
            matrix[i][j]=matrix[j][i]
            matrix[j][i]=temp
    for i in range(len(matrix)):
        left = 0
        right = len(matrix[i])-1
        while left<right:
            temp = matrix[i][left]
            matrix[i][left]=matrix[i][right]
            matrix[i][right]=temp
            left+=1
            right-+1
    return matrix
 """

""" def second_diagonal(matrix):
    for i in range(len(matrix)):
        print(matrix[i][len(matrix)-1-i],end=" ")


row = int(input("enter the row number"))
col = int(input("enter the coloumn number"))
matrix = []
for i in range(row):
    rows = []
    for j in range(col):
        value = int(input(f"enter the element at index positions at  {[i]}{[j]} "))
        rows.append(value)
    matrix.append(rows)

print(matrix) """
""" traverse(matrix) """
""" print(transpose_squre(matrix)) """
""" print(transpose(matrix)) """
""" upper_triangle(matrix)
lower_triangle(matrix)
 """
""" print(ninty(matrix)) """
""" second_diagonal(matrix) """


""" def multiple(matrix):
    for i in range(len(matrix)):
        matrix[i]= matrix[i]*10
    return matrix

print(multiple([2,5,7,10,12])) """

""" def getunsorted(matrix):
    for i in range(0,len(matrix)-1):
        minimum = matrix[i]
        if minimum> matrix[i+1]:
            return matrix[i+1]
    return -1

print(getunsorted([10,20,30,40,50,49,70]))
 """

""" def countsced(matrix):
    count = 0
    for i in range(len(matrix)-1):
        minimum= matrix[i]
        if minimum>matrix[i+1]:
            count+=1
    return count
print(countsced([10,20,15,18,16,17,12,11]))
 """

def shift(matrix):
    for i in range(len(matrix)-1):
        temp = matrix[i]
        matrix[i] = matrix[i+1]
        matrix[i+1]=temp

    return matrix

print(shift([10,20,30,40,50]))


