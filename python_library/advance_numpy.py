import numpy as np

a=np.arange(24).reshape(6,4)

# Advanced indexing

# fancy indexing -> name of matrix[[only row]] , name of matrix[ :,[only coloum]]
print(a[:,[0,2,3]])

print(a[[ 0,2,3]])

# boolean indexing -> name of matrix[condition using on name of matrix]

print("---------------------boolen indexing----------------------------")

print(a[a>50])

print(a[(a%2==0)&(a>50)])

# Broadcasting rules

print("-------------BROADCASTING RULES--------------------")
a=np.arange(12).reshape(4,3)
b=np.arange(3)

print(a+b)


# Working with mathematical formulas

print("---------working with mathematical formulas-----------------------")

a=np.arange(10)
print(np.sin(a))

# sigmoid -> sigmoid is famous mathematical formula to give the ans between 0 to 1

print("--------SIGMOID--------------")

def sigmoid(array):
    return 1/(1+np.exp(-(array)))

print(sigmoid(a))

# working with missing values 

print("--------------WROKING WITH MISSING VALUES -----------------")

a=np.array([1,2,3,4,np.nan,6])
print(a)

print(a[~np.isnan(a)])

