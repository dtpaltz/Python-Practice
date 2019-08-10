

def marcsCakewalk(calories):
    calories.sort(reverse=True)
    return sum(val * 2 ** idx for (idx, val) in enumerate(calories))



# print(calc_miles([5, 10, 7]))


cals = [7, 4, 9, 6]
print(marcsCakewalk(cals))





