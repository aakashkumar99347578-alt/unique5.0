#problem statment :- Take coordinates (x, y) and determine which quadrant the point lies in. 

#solution 


x=float(input("enter the x coordinates"))

y=float(input("enter the y coordinates"))

if x>0 and y>0:
    print(x,"and",y,"lies in first quadreant")

elif x<0 and y<0:
    print(x,"and",y,"lies in third quadreant")

elif x>0 and y<0:
    print(x,"and",y,"lies in fourth quadreant")

else:
    print(x,"and",y,"lies in second quadreant")