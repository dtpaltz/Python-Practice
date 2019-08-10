





def gradingStudents(grades):
    result = []
    for g in grades:
        delta = (5 - g % 5)
        new_grade = (g + delta)
        if new_grade >= 40 and delta < 3:
            result.append(new_grade)
        else:
            result.append(g)
    return result





g1 = [73, 67, 38, 33]

gradingStudents(g1)



