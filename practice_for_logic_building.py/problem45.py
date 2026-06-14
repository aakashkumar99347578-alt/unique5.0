#problem statment:- Count  many elements are positive, negative, or zero. and Count how many elements are even and odd.

#solution


n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    arr.append(int(input("Enter element: "))) # pyright: ignore[reportUnknownMemberType]
pos = neg = zero = even = odd = 0

for x in arr: # type: ignore
    if x > 0:
        pos += 1
    elif x < 0:
        neg += 1
    else:
        zero += 1

    if x % 2 == 0:
        even += 1
    else:
        odd += 1

print("Positive:", pos)
print("Negative:", neg)
print("Zero:", zero)
print("Even:", even)
print("Odd:", odd)