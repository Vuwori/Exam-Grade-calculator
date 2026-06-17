#Exam grade calculator

import math

# asks for amount of assessments
assessment_number = int(input("how many assessments are in this module? : "))

# if assement is only 1 return the exact amount
if assessment_number == 1:
    grade1 = float(input("what was your grade? :"))
    print(f"your avergae grade for the module is {grade1}!")
    
# if greater than 1
elif assessment_number > 1:

    total = 0

    for i in range(1, assessment_number + 1):
        grade = int(input(f"what is your grade for assessment {i} ? : "))

        total += grade


    average_total = total / assessment_number
    print(f"your average grade for this module is {average_total} :) ")






    