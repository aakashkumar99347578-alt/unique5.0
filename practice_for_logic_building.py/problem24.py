#problem statment:-  Take two angles of a triangle and compute the third angle. 

#solution

angle1 = float(input("Enter first angle: "))
angle2 = float(input("Enter second angle: "))

angle3 = 180 - (angle1 + angle2)

print("Third angle is:", angle3)

