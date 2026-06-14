#problem statment:-   Print a line of n stars recursively. 



#solution

def print_stars(n):
    if n == 0:
        return
    print("*", end="")
    print_stars(n - 1)

n = int(input("Enter number of stars: "))
print_stars(n)