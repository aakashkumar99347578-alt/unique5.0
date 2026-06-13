#problem statment :-  Take a character and check whether it’s uppercase, lowercase, a digit, or a special 
#character


#solutions



def check_uppercase_lowercase_digit_special_character(character):

    if (character.isupper()):
        print(character,"is a upper case ")


    elif (character.islower()):
        print(character,"is a lowercase")


    elif (character.isdigit()):
        print(character,"is digit")
    

    else:
        print(character,"is a special character")


check_uppercase_lowercase_digit_special_character("A")
check_uppercase_lowercase_digit_special_character("c")
check_uppercase_lowercase_digit_special_character("0")
check_uppercase_lowercase_digit_special_character("@")
