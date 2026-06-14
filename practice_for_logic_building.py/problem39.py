#problem statment:- Print a square of stars recursively (n×n). 

#solution


def print_row(n):
    if n == 0:
        return
    print("*", end="")
    print_row(n - 1)

def print_square(rows, n):
    if rows == 0:
        return
    print_row(n)
    print()   # new line
    print_square(rows - 1, n)

n = int(input("Enter size of square: "))
print_square(n, n)