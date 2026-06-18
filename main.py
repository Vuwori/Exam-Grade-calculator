#Exam grade calculator

import math

# asks for amount of assessments
while True:
    try:
        assessment_number = int(input("How many assessments are in this module? : "))

        # make sure number is not negative
        if assessment_number <= 0:
            print("Please enter a positive number.")
        else:
            break

    except ValueError:
        print("Invalid input. Please enter a whole number.")

# if assement is only 1 return the exact amount
if assessment_number == 1:
    grade1 = float(input("what was your grade? :"))
    print(f"your avergae grade for the module is {grade1}!")
    
# if greater than 1
elif assessment_number > 1:

    total = 0

    for i in range(1, assessment_number + 1):
        while True:
            try:
                grade = float(input(f"What is your grade for assessment {i}? : "))

                if grade < 0:
                    print("Grade cannot be negative.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a number.")

        total += grade


    average_total = total / assessment_number
    print(f"your average grade for this module is {average_total} :) ")






    