ects_earned = 138
points_earned = 44
points_max = 60
ects_required_for_ba = 180
var = 6


print("So far you earned", ects_earned, "ECTS points")
print("in the exam you got", points_earned, "of", points_max, "points.")

ects_missing = ects_required_for_ba - ects_earned
print("You have to book", ects_missing, "ECTS points for your bachelor degree.")

six_ects_courses = ects_missing / var
print("You have to book", six_ects_courses, "more for your bacehlor degree.")

grade = (points_earned / points_max) * 5 + 1
print("You have reached the grade %.2f in the exam." % (grade))

def percentage_completed(a, b):
    c = a / b * 100
    c = round(c)
    return str(c) + "%"

print("You have finished", percentage_completed(ects_earned, ects_required_for_ba) ,"of your bachelor degree.")

def calculate_grade(a,b):
    grade = a / b * 5 + 1
    return grade

print("In an other exam you have reached the grade: %.2f" % calculate_grade(67, 90))

def multiple_of(a, b):
    if a % b == 0:
        return True
    else:
        return False

print(multiple_of(ects_missing, 3))

#Exercise 4.1 c)
question = str(input("Do you want to add more ECTS Points? (Yes/No) "))

def new_ects(n):
    global ects_earned
    global ects_required_for_ba
    if question == "Yes":
        additional_points = int(input("Enter your new ECTS points: "))
        if additional_points < 0:
            additional_points = 0
        ects_earned += additional_points
        ects_missing = ects_required_for_ba - ects_earned
        if ects_earned >= 180:
            print("Congratulations, you reached your bachelor degree!")
        elif ects_earned >= 150:
            print("Your new amount of ECTS points is", ects_earned, "and you need", ects_missing ,"more to reach your bachelor degree. You are nearly done mate!")
        else:
            print("Your new amount of ECTS points is", ects_earned, "and you need", ects_missing ,"more to reach your bachelor degree. Still a long way to go my friend...")
        again = str(input("Do you want ot add more ECTS points? (Yes/No) "))
        while again == "Yes":
            additional_ects = int(input("Enter your new ECTS points: "))
            if additional_ects < 0:
                additional_ects = 0
            ects_earned += additional_ects
            ects_missing = ects_required_for_ba - ects_earned
            if ects_earned >= 180:
                print("Congratulations, you reached your bachelor degree!")
            elif ects_earned >= 150:
                print("Your new amount of ECTS points is", ects_earned ,"and you need", ects_missing ,"more to reach your bachelor degree. You are nearly done mate!")
            else:
                print("Your new amount of ECTS points is", ects_earned ,"and you need", ects_missing ,"more to reach your bachelor degree. Still a long way to go my friend...")
            again = str(input("Do you want ot add more ECTS points? (Yes/No) "))

print(new_ects(question))