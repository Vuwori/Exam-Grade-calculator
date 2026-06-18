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

    weighted_total = 0
    total_weight = 0

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

        while True:
            try:
                weight = float(input(f"What is the weight (%) of assessment {i}? : "))

                if weight <= 0:
                    print("Weight must be positive.")
                else:
                    break

            except ValueError:
                print("Invalid input. Please enter a number.")

        weighted_total += grade * weight
        total_weight += weight

    if total_weight != 100:
        print(f"\nWarning: Total weight is {total_weight}% (not 100%).")

    weighted_average = weighted_total / total_weight

    print(f"\nYour weighted average grade is {weighted_average:.2f}")





    