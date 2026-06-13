#problem statment:- take a temperature value and print “Cold”, “Warm”, or “Hot” using range conditions.

#solution

def tem(temperature):

    if temperature>25:
        print(temperature,"is a hot temperature")
    elif 20<temperature<25:
        print(temperature,"is a warm temperature")
    else:
        print(temperature,"is a cold temperature")



tem(56)
tem(22)
tem(10)