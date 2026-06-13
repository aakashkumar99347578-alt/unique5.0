#problem statmen:-If the sides form a valid triangle, determine whether it is equilateral, isosceles, or 
#scalene


#solution



def check_valid_trangle(side1,side2,side3):

    if ((side1+side2)>side3) and ((side3+side1)>side2) and ((side2+side3)>side1):

        print(side1,side2,"and",side3,"are make a valid traingle")


        if (side1==side2==side3):
            print(side1,side2,side3,"are make equilateral triangle")


        elif (side1==side2 or side1==side3 or side2==side3):
            print(side1,side2,side3,"are make isosceles triangle")

            
        else:
            print(side1,side2,side3,"are make scalene triangle")
    

    else:
        print(side1,side2,"and",side3,"are not make a valid traingle")