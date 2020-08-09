ects_earned = 138
points_earned = 44
points_max = 60
ects_required_for_ba = 180

ects_missing = ects_required_for_ba - ects_earned
courses_with_6_ects = ects_missing / 6
grade = points_earned / points_max * 5 + 1


def percentage_completed(a, b):
    c = round(a/b*100,2)
    return str(c)+"%"


def calculate_grade(a,b):
    return round(a / b * 5 + 1 , 2)


def multiple_of(a,b):
    return a%b == 0


def new_ects(n):
    global ects_earned
    if ects_earned >= ects_required_for_ba:
        return("Congratulations! Your degree is currently " + percentage_completed(ects_earned,ects_required_for_ba) + " complete. Have fun at your graduation ceremony!")
    else:
        n = float(n)
        if n == -1:
            return
        else:
            ects_earned += n
            print("Total ECTS earned: " + str(ects_earned))
        if ects_earned >= ects_required_for_ba:
            return new_ects(n)
        elif ects_missing < 30:
            print("Your degree is currently " + percentage_completed(ects_earned,ects_required_for_ba) + " complete. You are almost finished, keep it up!")
            return
        else:
            print("Your degree is still " + percentage_completed(ects_earned,ects_required_for_ba) + " complete. Still a long way to go!")
            return


# Task 7.1a)
def add_grade(filename, mode):
    new_file = open(filename + ".txt", mode)
    new_results = input('Do you want to add new exam results? ')
    while new_results == "Yes":
        lecture = input('Enter the name of the lecture: ')
        new_ects = input('Enter ECTS Points: ')
        points_max = float(input('Enter maximum Points: '))
        points_achieved = float(input('Enter achieved Points: '))
        grade = str(calculate_grade(points_achieved, points_max))
        new_file.write(new_ects + "\t" + grade + "\t" + lecture + "\n")
        new_results = input('Do you want to add new exam results? ')
    new_file.close()


print(new_ects(6))
add_grade('ECTS compilation', 'w')


# Task 7.1b)
def get_study_overview(file):
    content = [lines for lines in file.readlines() if lines.strip()]
    i = 0
    j = 0
    ects_so_far = 0
    sum_grades = 0.0
    while i <= len(content)-1:
        line = content[i]
        line = line.split("\t")
        ww = line[2]
        ww = ww[:-1]
        line[2] = ww
        grade = float(line[1])
        ects = float(line[0])
        if grade >= 4.0:
            print(line)
            ects_so_far += ects
            sum_grades += float(grade)
            j += 1
        i += 1
    average_grade = round(sum_grades / j, 2)
    ects_so_far = str(ects_so_far)
    print('You successfully added ', ects_so_far  ,' ECTS and you completed ', percentage_completed(float(ects_earned)+float(ects_so_far), ects_required_for_ba) ,' of your bachlor degree.'
          ' The average of all your passed Exams is:', float(average_grade) ,'(The sum is: ', sum_grades ,')')
    file.close()


content = open("ECTS compilation.txt")
get_study_overview(content)