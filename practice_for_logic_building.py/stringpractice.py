strings = input("enter the string :- ")

#traversal and counting problem 

""" def vowel(strings):
    count = 0
    for i in strings:
        if i in "aeiou":
            count+=1
    return count

print(vowel(strings)) """

""" def constant(strings):
    count = 0
    for i in strings:
        if i not in "aeiou":
            count+=1
    return count

print(constatn(strings)) """

""" def digits(strings):
    count = 0
    for i in strings:
        if i.isdigit() :
            count+=1
    return count

print(digits(strings)) """

""" def spacecount(strings):
    return strings.count(" ")
print(spacecount(strings)) """

""" def specail_charaters(strings):
    upper = 0
    lower =0
    specil =0
    digits=0
    for i in strings:
        if i.isupper():
            upper+=1
        elif i.islower():
            lower+=1
        elif i.isdigit():
            digits+=1
        else:
            specil+=1
    return upper , lower , specil , digits
print(specail_charaters(strings))
 """

""" def reverse_word(strings):
    word = strings.split()
    return word[: :-1]
    
print(reverse_word(strings)) """


""" def reverse_each_word(strings):
    word = strings.split()
    reverse = word[::-1]
    return " ".join(reverses[::-1] for reverses in reverse)
print(reverse_each_word(strings)) """