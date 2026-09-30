""""
def number(n):
    if n<1:
        return
    number(n-1)
    print(n,end=" ")

number(5)


def display_greeting(username):
    print(f"Hello {username}")

display_greeting(input("enter the name"))

def get_state(number):
     return number*2 ,number/2 # it will give ouput in tuples form

print(get_state(int(input("enter the number")))) 

def do_nothing():
    pass

result = do_nothing()
print(result) 

def process(a,b=2):
    return a*b+1

print(process(3))
print(process(2,6))  

total = 50
def upadate_total():
    total = total+10

upadate_total() 


total = 50
def upadate_total():
    global total
    total = total+10

upadate_total()
print(total)    

square = lambda x: x*x
print(square(10))

def sum_number(x,y):
    return x+y

print(sum_number(int(input("enter the first number")),int(input("enter the second number"))))

def maximum_number(x,y):
    if x>y:
        return x
    else:
        return y
print(maximum_number(int(input("enter the first number")),int(input("enter the second number"))))  

def number(num):
    sum = 0
    if type(num)==str:
        
        for i in num:
            sum+=int(i)
        return sum
    else:
        while num>0:
            rem = num%10
            sum +=rem
            num = num//10
        return sum

    
    
print(number(input("enter the number")))
print(number(123))   """



