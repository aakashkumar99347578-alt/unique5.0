# create an array and print alternate 

size = int(input("enter the size of array "))
l=[]
for i in range(size):
    number = int(input(f"enter the elemetn at index{i} "))
    l.append(number)
def alternate(arr):
    for i in arr[ : :2]:
        print(i)

alternate(l)