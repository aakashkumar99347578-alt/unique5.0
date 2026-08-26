import numpy as np
import pandas as pd

print("-----------------------this is a train data frame ----------------------------------------------------")
train = pd.read_csv(r'C:\Users\aakas\OneDrive\Desktop\uniques 5.0\unique5.0\python_library\train - train.csv')
print(train)

# QUESTION PRACTICE 
# Q-1: Using groupby make groups using the "Pclass" column and find out the average age and total number of missing values in the "Age" column for every group.

print("-------------------------------------QUESTION 1------------------------------------------------")
print((train.groupby('Pclass')['Age'].sum())//(train.groupby('Pclass')['Age'].count()))
print(train.groupby('Pclass')['Age'].apply(lambda x :x.isnull().sum()))
print(train.groupby('Pclass')['Age'].mean())

# Q-2: Using groupby make groups using the "Pclass" column and fill every group's "Embarked" column's missing values with the mode value of that group. After that, print every group's "Embarked" column's value counts in ascending order.

print("-------------------------------QUESTION 2 --------------------------------------")

# Q-3: Make groups based on "Embarked" column. And for each of this embarked group, make another group based on "Pclass" and find out the average fare (round off up to 2 decimal places) for each "Pclass" for each group of "Embarked".

print("-------------------------------QUESTION 3----------------------------------------")
print(train.groupby(['Embarked','Pclass'])['Fare'].mean())

