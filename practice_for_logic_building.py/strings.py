""" s = input(" enter the any string ")
for i in s:
    print(i)
 """
""" def vowel(strings):
    for i in strings:
        if i in "aeiou":
            print(i)
vowel("aakash")
 """

""" def stringpalindrome(strings):
    if strings==strings[ : :-1]:
        print(strings,"is a palindrome stings")
    else:
        print(strings,"is a not palindrome strings")

stringpalindrome("jpk")
 """
""" def substring(strings):
    count = 0
    for i in range(len(strings)):
        count+=1
        print(strings[i: : ])
    return count
print(substring("ravi")) """

""" def substring(strings):
    count = 0
    for i in range(len(strings)):
        for j in range(i,len(strings)):
            count+=1
            print(strings[i : : ])
    return count
print(substring("ravi")) """

integer = int(input("enter the number"))
print(type(integer))
string = str(integer)
print(string)
print(type(string))

sum = 0
for i in range(len(string)):
    sub = string[i]
    sum+=int(sub)
    for j in range(i+1,len(string)):
        sub = sub+string[j]
        sum+=int(sub)
print(sum)