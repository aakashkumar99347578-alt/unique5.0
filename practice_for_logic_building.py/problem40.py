# problem statment :- Print a triangle of stars recursively (top-down). and Print a triangle of stars recursively (bottom-up). 



#solution


#Triangle of stars (Top-down recursion)

def print_row(n):
    if n == 0:
        return
    print("*", end="")
    print_row(n - 1)

def triangle_top(n):
    if n == 0:
        return
    print_row(n)
    print()
    triangle_top(n - 1)

n = int(input("Enter number of rows: "))
triangle_top(n)


#triangle of stars (bottom-top recursion)

def print_row(n):
    if n == 0:
        return
    print("*", end="")
    print_row(n - 1)

def triangle_bottom(n):
    if n == 0:
        return
    triangle_bottom(n - 1)
    print_row(n)
    print()

n = int(input("Enter number of rows: "))
triangle_bottom(n)