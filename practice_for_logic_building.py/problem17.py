#problem satment :-Take two numbers and determine whether both are even, both are odd, or one is 
#even and one is odd.



#solution


def check_evne_odd(num1,num2):
    

    if num1%2==0:

        if num2%2==0:
            print(num1,"and",num2,"both are even number")
        else:
              print(num1,"is a even number but",num2,"is a odd number")
    else:
           print(num1,"and",num2,"both are odd number")