# Creating numpy array 

# 1D
import numpy as np
a=np.array([1,2,3])
print(a)

# 2D
b = np.array([[1,2,3],[4,5,6]])
print(b)

# 3D
c = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(c)


# dtype -> dtype use for convert data type in exiting array elemen 

a=np.array([1,2,3],dtype=float)
print(a)


# np.arange -> np.range use for enter the elment in numpy array , in np.arange (start,end,jump)

a=np.arange(1,11,2)
print(a)

# with reshape -> reshape use for making matrix array only possible combination

a=np.arange(16).reshape(2,2,2,2)
print(a)

a=np.arange(16).reshape(4,4)
print(a)

# np.ones -> np.ones((number of row , number of coloum)) ,np.ones making array with only 1 number in float format

a=np.ones((3,2))
print(a)

# np.zeros -> np.zeros((number of row , number of coloum)), np.zeros making array with only 0 number in float data type

print(np.zeros((3,4)))

# np.random -> np.random.random((number of row , number of coloum)) , np.random.random automatic genrate matrix array between 0 to 1 in decimal format 

print(np.random.random((2,2)))

print(np.random.random((2,2))*100)

# np.linespace -> np.linespace(start,end,how many number you want) , np.linespace when you want to print in give range , equal distace point 

print(np.linspace(-10,10,10))

print(np.linspace(-10,10,10,dtype=int))

print(np.linspace(-10,10,13))

print(np.linspace(-10,10,12,dtype=int))


# np.identity -> np.identity(number of row) , np.identity print the identity matrix

print(np.identity(3,dtype=int))

print(np.identity(3))


# Array attributes

a1 = np.arange(10,dtype=np.int32)
a2 = np.arange(12,dtype=float).reshape(3,4)
a3 = np.arange(8).reshape(2,2,2)

print(a1)
print(a2)
print(a3)

# ndim -> matrix of array how many dimension in exits

print(a1.ndim)
print(a2.ndim)
print(a3.ndim)


# shape -> shape tell about format of array of matrix

print(a1.shape)
print(a2.shape)
print(a3.shape)

# size -> size tell about the how many number in array

print(a1.size)
print(a2.size)
print(a3.size)

# itemsize -> itemsize tell about how many memory occupied by array

print(a1.itemsize)
print(a2.itemsize)
print(a3.itemsize)

# dtype -> dtype tell about data type of array 

print(a1.dtype)
print(a2.dtype)
print(a3.dtype)

# astype -> astype convert data type of array elements

print(a3.astype(np.int32))

# Array opertions

a1 = np.arange(12).reshape(3,4)
a2 = np.arange(12,24).reshape(3,4)

print(a1)
print(a2)

# arithmetic -> in numpy array all arithmetics opertions you can forms 

print(a1**2)

# relational -> all relational opertors forms on numpy array

print(a2==15)

# Vector opertions
# arithmetic

print(a1*a2)

# Array functions

print(a1)
print(a2)

# max -> max give the max number in array 

print(np.max(a1))
print(np.max(a2))


# min -> min give the minimum number in array 

print(np.min(a1))
print(np.min(a2))

# prod -> prod give the product of all number in array 

print(np.prod(a1))
print(np.prod(a2))

# mean

print(np.mean(a1))
print(np.mean(a2))

# median

print(np.median(a1))
print(np.median(a2))

#std

print(np.std(a1))
print(np.std(a2))

# var

print(np.var(a1))
print(np.var(a2))

# axis -> 0-> coloum , 1-> row , axis work with all like max , min , prod , mean , median ,std ,var ..........

print(np.max(a1,axis=0))
print(np.max(a1,axis=1))

# trigonometri functions

print(np.sin(a1))
print(np.sin(a2))


# dot product -> multiple of matrix only possible condition 

a2 = np.arange(12).reshape(3,4)
a3 = np.arange(12,24).reshape(4,3)


print(np.dot(a2,a3))

# log and exponents

print(np.exp(a1))

# round 

a=np.random.random((2,3))*100
print(a)

print(np.round(a))

# floor

print(np.floor(a))

# ceil

print(np.ceil(a))

# iterating

a1 = np.arange(10)
a2 = np.arange(12).reshape(3,4)
a3 = np.arange(8).reshape(2,2,2)

for i in a1:
    print(i)

for i in a2:
    print(i)

for i in a3:
    print(i)

# nditer -> use on when matrix dimension more than one and you want to print every element then

for i in np.nditer(a3):
  print(i)

# transpose -> transpose conver every row into coloumn

print(a2)
print(np.transpose(a2))

# ravel -> ravel convert multidimesional array into in 1D array 

print(a3.ravel())

# Stacking 

a4 = np.arange(12).reshape(3,4)
a5 = np.arange(12,24).reshape(3,4)

print(a4)
print(a5)

# horizontal stacking -> in horizontal stacking merge two or more than two matrix in horizonally 

print(np.hstack((a4,a5)))

# vertical stacking -> vertical stacking merge two or more than two matrix in vertically 

print(np.vstack((a4,a5)))

# Splitting 

# horizontal splitting -> np.hsplit(name of matrix , how many parts you want to split , and make sure only possible number enter ) , hsplit divide the matrix by verticle line 

print(np.hsplit(a4,2))

# vertical splitting -> np.vsplit(name of matrix , how many parts you want to split , and make sure only possible number enter ) , vertical split just opposite 

print(np.vsplit(a5,3))

