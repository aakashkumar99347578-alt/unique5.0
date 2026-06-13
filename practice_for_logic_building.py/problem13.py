#problem statment:-take marks (0–100) and print the corresponding grade (A/B/C/D/F).


#solution

def get_grade(marks):


    if marks >= 90:
        return "A"
    

    elif marks >= 80:
        return "B"
    

    elif marks >= 70:
        return "C"
    

    elif marks >= 60:
        return "D"
    

    else:
        return "F"
    


marks = float(input("Enter marks (out of 100): "))



if 0 <= marks <= 100:
    grade = get_grade(marks)
    print("Grade:", grade)

    
else:
    print("Invalid marks! Please enter marks between 0 and 100.")