#problem statment :- Take the hour of the day (0–23) and print “Good Morning”, “Good Afternoon”, “Good 
#Evening”, or “Good Night”.





#solution


def greet(hour):
    if 5 <= hour < 12:
        print("Good Morning")
    elif 12 <= hour < 17:
        print("Good Afternoon")
    elif 17 <= hour < 21:
        print("Good Evening")
    else:
        print("Good Night")

# Input
hour = int(input("Enter hour (0-23): "))

# Check valid hour
if 0 <= hour <= 23:
    greet(hour)
else:
    print("Invalid hour!")