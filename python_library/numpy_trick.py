import numpy as np
a=np.random.randint(1,100,15)
b=np.random.randint(1,100,24).reshape(6,4)
print(a)

# np.sort -> return a sorted copy of an array 

print("--------np.sort-----------")

print(np.sort(a))
print(np.sort(a)[::-1])
print("------------2D ARRAY SORTING----------")
print(np.sort(b,axis=0))
print(np.sort(b,axis=1))

# np.append -> the numpy.append()appends values along the mentioned axis at the end of the array 

print("--------np.append-------------")

print(np.append(a,200))
print("------------2D ARRAY APPEND METHOD ------------")
print(np.append(b,np.random.random((b.shape[0],1)),axis=1))


# np.concatenate -> numpy.concatenate() function concatenate a sequence of arrays along an existing axis.

c = np.arange(6).reshape(2,3)
d = np.arange(6,12).reshape(2,3)

print(c)
print(d)

print(np.concatenate((c,d),axis=0))
print(np.concatenate((c,d),axis=1))

# np.unique -> With the help of np.unique() method, we can get the unique values from an array given as parameter in np.unique() method.

print("-------np.unique-----------")

e=np.array([1,1,2,2,3,3,4,5,6,4,5,6])
print(np.unique(e))

# np.expand_dims -> With the help of Numpy.expand_dims() method, we can get the expanded dimensions of an array

print("------------------np.expand_dims-------------------------")
print(a)
print(a.shape)
print(np.expand_dims(a,axis=0))
print(np.expand_dims(a,axis=0).shape)

# np.where -> The numpy.where() function returns the indices of elements in an input array where the given condition is satisfied.

print("---------------------np.where --------------------")
print(a)
    
    # find all indices with value greater than 50

print(np.where(a>50))

    # replace all values >50 with 0

print(np.where(a>50,0,a))

print(np.where(a%2==0,0,a))

#np.argmax -> The numpy.argmax() function returns indices of the max element of the array in a particular axis.

print("-----------np.argmax-----------------------------")
print(a)
print(b)
print(np.argmax(a))
print(np.argmax(b,axis=0))
print(np.argmax(b,axis=1))

# np.argmin -> the numpy.argmin() function return indices of the minimum element of the array in a particular axis.

print("----------------np.argmin------------------")
print(a)
print(b)
print(np.argmin(a))
print(np.argmin(b,axis=0))
print(np.argmin(b,axis=1))

#np.cumsum -> numpy.cumsum()function is used when we want to compute the cumulative sum of array elements over a given axis.

print("------------------np.cumsum--------------------")
print(a)
print(b)
print(np.cumsum(a))
print(np.cumsum(b,axis=0))
print(np.cumsum(b,axis=1))

# np.cumprod -> numpy.cumprod() function is used when we want to compute the cumulative product of array elements over a given axis.

print("------------------np.cumprod--------------------")
print(a)
print(b)
print(np.cumprod(a))
print(np.cumprod(b,axis=0))
print(np.cumprod(b,axis=1))

# np.percentile -> numpy.percentile()function used to compute the nth percentile of the given data (array elements) along the specified axis.

print("------------------np.percentile-----------------------")
print(a)
print(b)
print(np.percentile(a,75))
print(np.median(a))

# np.histogram -> Numpy has a built-in numpy.histogram() function which represents the frequency of data distribution in the graphical form.

print("-------------------np.histogram------------------------")
print(a)
print(b)
print(np.histogram(a,bins=[0,50,100]))

# np.corrcoef -> return person product-moment correlation coefficients.

print("--------------np.corrcoef-------------------")
salary = np.array([20000,40000,25000,35000,60000])
experience = np.array([1,3,2,4,2])

print(np.corrcoef(salary,experience))

# np.isin -> With the help of numpy.isin() method, we can see that one array having values are checked in a different numpy array having different elements with different sizes.

print("------------------------np.isin-------------------------")
print(a)
items=[10,20,30,40,50,60,70,80,90,100]

print(a[np.isin(a,items)])

# np.flip -> The numpy.flip() function reverses the order of array elements along the specified axis, preserving the shape of the array.

print("-------------------np.flip--------------------------")
print(a)
print(b)
print(np.flip(a))
print(np.flip(b,axis=0))
print(np.flip(b,axis=1))

# np.put -> The numpy.put() function replaces specific elements of an array with given values of p_array. Array indexed works on flattened array.

print("----------------np.put--------------------------")
print(a)
np.put(a,[0,1],[110,50]) # perament change in array a.
print(a)

#np.delete -> The numpy.delete() function returns a new array with the deletion of sub-arrays along with the mentioned axis.

print("-------------------np.delete----------------------")
print(a)
print(np.delete(a,[0,2,4]))

# np.union1d ->

m = np.array([1,2,3,4,5])
n = np.array([3,4,5,6,7])
print("---------------np.union1d-----------------")
print(np.union1d(m,n))

# np.intersect1d ->

print("---------------np.intersect1d-------------------")
print(np.intersect1d(m,n))

# np.setdiff1d ->

print("----------------np.setdiff1d-------------------")
print(np.setdiff1d(m,n))

# np.setxor1d ->

print("------------------np.setxor1d---------------------")
print(np.setxor1d(m,n))

# np.clip -> numpy.clip() function is used to Clip (limit) the values in an array.

print("----------------np.clip----------------")
print(a)
print(np.clip(a,a_min=25,a_max=75))
