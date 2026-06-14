#problem statment :- Count the number of digits in a given number.Count



#solution

count=0 

num=int(input("enter the big number for cpunt how many number in big number "))

for i in str(num):
    count+=1
print(count)