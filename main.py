#Exam grade calculator

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

    

weighted_total = 0
total_weight = 0

# grades and the weights via loop
for i in range(1, assessment_number + 1):

    # grade validation
    while True:
        try:
            grade = float(input(f"What is your grade for assessment {i}? : "))

            if grade < 0:
                print("Grade cannot be negative.")
            elif grade > 100:
                print("Grade cannot be more than 100.")
            else:
                break

        except ValueError:
            print("Invalid input. Please enter a number.")

    # weight validation
    while True:
        try:
            weight = float(input(f"What is the weight (%) of assessment {i}? : "))

            if weight <= 0:
                print("Weight must be positive.")
            elif weight > 100:
                print("Weight cannot be more than 100.")
            else:
                break

        except ValueError:
            print("Invalid input. Please enter a number.")

    weighted_total += grade * weight
    total_weight += weight

# to check weights
if total_weight != 100:
    print(f"\nWarning: Total weight is {total_weight}% (not 100%).")

# calculate the average weight
weighted_average = weighted_total / total_weight

print(f"\nYour weighted average grade is {weighted_average:.2f}")





    