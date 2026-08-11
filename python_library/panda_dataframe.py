import numpy as np
import pandas as pd

# CREATING DATA FRAME ->
print("------------------------creating data frame---------------------------------")

# using lists ->

print("--------------------using list-------------------")
student_data = [
    [100,80,10],
    [90,70,7],
    [120,100,14],
    [80,50,2]
]
print(pd.DataFrame(student_data,columns=['iq','marks','package']))

# using dicts ->

print("--------------------dicts---------------------------")
student_dict = {
    'name':['aakash','ankit','rupesh','rishabh','amit','ankita'],
    'iq':[100,90,120,80,0,0],
    'marks':[80,70,100,50,0,0],
    'package':[10,7,14,2,0,0]
}

students = pd.DataFrame(student_dict)
students.set_index('name',inplace=True)
print(students)

# using read_csv ->

print("--------------using read_csv------------------------")
movies = pd.read_csv(r'C:\Users\aakas\OneDrive\Desktop\uniques 5.0\unique5.0\python_library\movies.csv')
ipl = pd.read_csv(r'unique5.0/python_library/ipl-matches.csv')
print(movies)
print(ipl)

# DATA FRAME ATTRIBUTES AND METHODS ->
print("---------------------------------DATA FRAME ATTRIBUTES AND METHODS----------------------------")

#shape -> shape return the how many row and coloumn in data frame.

print("----------------------------------------------shape----------------------------------------------")
print(movies.shape)
print(ipl.shape)

#dtype ->

print("---------------------------------------------dtype--------------------------------------")
print(ipl.dtypes)
print(movies.dtypes)

# index ->

print("--------------------------------------------------index------------------------------------------")
print(ipl.index)
print(movies.index)

# coloums -> coloums return the all coloumn name in data frame.

print("--------------------------coloums---------------------------------------")
print(ipl.columns)
print(movies.columns)

# info -> info return the how many non-null values in every coloumn.

print("-----------------------------------info------------------------------------------")
print(movies.info())
print(ipl.info())

# isnull -> isnull returns the boolen data where any non_null place then give True other wise give False.

print(movies.isnull().sum())
print(ipl.isnull().sum())

# duplicated -> duplicated return the boolen data if in data frame have duplicaed row.

print("-------------------------------------duplicated------------------------------------------")
print(movies.duplicated().sum())
print(students.duplicated().sum())
print(students)

# rename -> change the column name if you want to change parment then use implace keyboard.

print("---------------------------------------rename--------------------------------------")
students.rename(columns={'marks':'percent','package':'lpa'},inplace=True)
print(students)

# SINGLE COLS FROM A DATA FRAME->
print("------------------------------------------single cols from a data frame------------------------------------")

# single cols ->

print("--------------------------single coloums------------------------------------------------------------------")
print(movies['title_x'])
print(ipl['Venue'])

# multiple cols ->

print("--------------------------------multiple coloums------------------------------------------")
print(movies[['year_of_release','actors','title_x']])
print(ipl[['Team1','Team2','WinningTeam']])

# Selecting rows from a DataFrame->

# iloc - searches using index positions
# loc - searches using index labels

# single rows ->

print("---------------------------------single row----------------------------------------")
print(movies.iloc[5])

# multiple row ->

print("---------------------------multiple row---------------------------------------")
print(movies[ :5])

# fancy indexing ->

print("------------------------------fancy indexing-------------------------------")
print(movies.iloc[[0,4,5]])

# loc ->

print("------------------------------------------------loc------------------------------------------------------")
print(students)
print(students.loc['nitish'])
print(students.loc['nitish':'rishabh':2])
print(students.loc[['nitish','ankita','rupesh']])


# selecting both row and coloumn .

print("----------------------------selecting both row and coloumn---------------------------------------")
print(movies.iloc[0:3,0:3])
print(movies.loc[0:2,'title_x':'poster_path'])


