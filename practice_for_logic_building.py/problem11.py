#problem statment :-Take three sides and check if they form a valid triangle.



#solution

def check_valid_trangle(side1,side2,side3):

    if ((side1+side2)>side3) and ((side3+side1)>side2) and ((side2+side3)>side1):

        print(side1,side2,"and",side3,"are make a valid traingle")
    

    else:
        print(side1,side2,"and",side3,"are not make a valid traingle")

check_valid_trangle(1,2,3)
check_valid_trangle(3,4,5)