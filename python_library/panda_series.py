""""
What is Pandas:->
Pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool, built on top of the
Python programming language

Pandas Series->
A Pandas Series is like a column in a table. It is a 1-D array holding data of any type.




"""
import numpy as np
import pandas as pd

# series from list ->

print("------------------series from list --------------")
country = ["india","china","bhutna","usa","nepal"]
print(pd.Series(country))

# integers series->

print("---------------integers series----------------------")
runs = [13,24,56,78,100]
print(pd.Series(runs))

# custom inex ->

print("---------------custom index---------------")
marks = [67,57,89,100]
subjects = ['maths','english','science','hindi']
print(pd.Series(marks,index=subjects))

# setting name ->

print("-----------setting name------------")
print(pd.Series(marks,index=subjects,name="aakash ke marks"))

# series from dictionary ->

print("--------------series from dictionary---------------")
marks = {
    'maths':67,
    'english':57,
    'science':89,
    'hindi':100
}

marks_series = pd.Series(marks,name='aakash ke marks')
print(marks_series)

# SERIES ATTRIBUTES ->

print("-----------------SERIES ATTRIBUTES----------------------")

# size->

print("------------size of series-----------------")
print(marks_series.size)

# name-> name returns the series name 

print("---------------name------------------")
print(marks_series.name)

# is_unique -> is_unique return True when everu elment in series is unique other wise false

print("-------------------is_unique--------------------")
print(marks_series.is_unique)

# index-> index return the series index

print("---------------index--------------------")
print(marks_series.index)

# values -> values return the value of series

print("---------------values--------------")
print(marks_series.values)

# SERIES USING READ CSV FILE->
print("--------------------SERIES USING READ CSV FILE-------------------")

# with one coloum->

print("-------------------with one coloum----------------")
subs = pd.read_csv(r'C:\Users\aakas\OneDrive\Desktop\uniques 5.0\unique5.0\python_library\subs (1).csv')
print(subs)

# with two coloum->

vk = pd.read_csv(r'C:\Users\aakas\OneDrive\Desktop\uniques 5.0\unique5.0\python_library\kohli_ipl (1).csv',index_col="match_no").squeeze()
print(vk)
print(type(vk))

movies = pd.read_csv(r'C:\Users\aakas\OneDrive\Desktop\uniques 5.0\unique5.0\python_library\bollywood (1).csv',index_col="movie").squeeze()
print(movies)
print(type(movies))

# SERIES METHODS ->
print("-------------------SERIES MEHTODS-------------------")

# head-> head return top 5 data of any series if no parameters pass out if you want to pass any number parameter then return data according to parameters number

print("----------------------------head-----------------------------")
print(subs.head())
print(vk.head(3))

# tail -> tail return bottom 5 data of any series if no parameters out if you want to pass any number parameter then return data according to parameters number.

print("--------------------------tail---------------------------------")
print(movies.tail())
print(subs.tail(2))

# sample-> sample returns the random data from the exiting data.

print("------------------sample---------------------")
print(vk.sample(3))

# values_counts -> values_counts return the how many times reptea value in data.

print("----------------values_counts----------------")
print(movies.value_counts())

# sort_values -> 

print("----------------------sort_values---------------------------")
print(vk.sort_values())
print(vk.sort_values(ascending=False))

# sort_index->

print("------------------------sort_index------------------")
movies.sort_index(inplace=True)  # when i use inplace parameter is equal to True then it's change parament in data.
print(movies)

# SERIES MATH METHODS->

print("----------------------------SERIES MATH METHODS-------------------------")

# count,sum,prod->

print("----------------------------count,sum,prod-----------------------------")
print(vk.count)
print(subs.sum)

# mean -> median -> mode -> std -> var

print("--------------------------mean,median,mode,std,var---------------------------------")
print(subs.mean())
print(vk.median())
print(movies.mode())
print(subs.std())
print(vk.var())

# min/max->

print("----------------------------min/max----------------------------")
print(subs.max())
print(subs.min())

# describe->

print("---------------------describe----------------------")
print(subs.describe())

# SERIES INDEXING->
print("--------------------------SERIES INDEXING---------------------------")

# integer indexing -> only positive indexing are allowed  but in case when index is string then only neagtive indexing is allowed.

print("-------------------integer indexing---------------------------")
x = pd.Series([12,13,14,35,46,57,58,79,9])
print(x)
print(x[2])

# slicing ->

print("----------------------slicing------------------------")
print(vk[5:9])
print(vk[-5:])

# fancy indexing->

print("------------------------------fancy indexing-----------------------------")
print(vk[[1,3,5,7]])

# indexing with labels -> fancy indexing

print("--------------------indexing with labels---------------------")
print(movies['2 States (2014 film)'])

# EDITING SERIES ->
print("--------------------------editing series------------------------")

# using indexing

print("------------------------using indexing-----------------------")
marks_series[1]=100
print(marks_series)

# what if an index does not exist -> if an index does not exist then add the index with the value in series.

print("---------------------------what if an index does not exist------------------------")
print(marks_series)
marks_series['evs'] = 100
print(marks_series)


# using index label->

print("---------------using index label---------------------")
movies['2 States (2014 film)'] = 'Alia Bhatt'
print(movies)

# SERIES WITH PYTHON FUNCTIONALITIES->
print("---------------------------SERIES WITH PYTHON FUNCTIONALITIES-----------------------")

# len/type/dir/sorted/max/min

print("-------------------len/type/dir/sorted/max/min-----------------------------")
print(len(subs))
print(type(subs))
print(dir(subs))
print(sorted(subs))
print(min(subs))
print(max(subs))

# Arithmetic Operators(Broadcasting)-> when i add 100 then in existing data in every value add 100.

print("--------------------------Arithmetic operators---------------------------------")
100 + marks_series
print(marks_series)

# Relational Operators

print("--------------------ralational operators--------------------------")
print(vk[vk>=50])

# SOME IMPORTANT SERIES MATHODS->
print("----------------------------SOME IMPORTANT SERIES MATHODS------------------------")

# between

print("--------------------------between-------------------------")
print(vk.size)
print(vk[vk.between(51,99)].size)

#clip-> clip(first parameter, second parameter) it's returns if first parameter se less than hai koi value to uske equal ho jayayega and second parameter se koi big hai to uske equal ho jayega.

print("----------------------------clip----------------------------------")
print(subs.clip(100,200))

# drop_duplicates -> drop_duplicates reuturns remove duplicates ites from existing csv in drop_duplicates keep='first' or'last' parameter hota hai jo parameter pass karenge use rakhe ga aur uske uper se all duplicates item ko delete kar dega.

print("---------------------drop_duplicates--------------------------------")
temp = pd.Series([1,1,2,2,3,3,4,4])
print(temp)
print(temp.drop_duplicates(keep='first'))
print(temp.drop_duplicates(keep='last'))

# count -> count return the only how many values data exist but size return the size of data.

print("-----------------------count/size------------------------")
temp = pd.Series([1,2,3,np.nan,5,6,np.nan,8,np.nan,10])
print(temp)
print(temp.size)
print(temp.count())

# isnull

print("------------------isnull---------------------------------------------")
print(temp.isnull().sum())

# dropna -> dropna it return the data remove all duplicates from existing data.

print("-------------------dropna--------------------------")
print(temp.dropna())

# fillna -> fillna fill the value at null value position.

print("--------------------------------------fillna-------------------------------------")
print(temp.fillna(temp.mean()))

# apply -> apply allow to make own customize way that you should apply on data.

print("-----------------------------apply------------------------------")
print(movies)
print(movies.apply(lambda x:x.split()[0].upper()))