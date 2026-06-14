#problem statment:- Print the factorial of a given number.

#solution


num=int(input("enter the number want to print factorial :-> "))
factorail=1

while num>0:
    factorail*=num
    num-=1
print("factorail of",num,"is",factorail)

