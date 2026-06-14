#problem statment:-  Print numbers from 10 down to 1. and Print the table of a given number (n × 1 to n × 10).


#solution 

for number in range(10,0,-1):
    print(number) 


num=int(input("enter the number you want to print table"))

for i in range(1,11):
    print(num*i)