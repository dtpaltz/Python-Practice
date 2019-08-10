


grades = {}

grades['d'] = 89
grades['c'] = 15
grades['g'] = 62
grades['y'] = 10
grades['x'] = 18
grades['o'] = 48
grades['f'] = 36
grades['a'] = 15
grades['e'] = 21
grades['m'] = 33

ss = sorted(set(grades.values()))[1]

for name, grade in sorted(grades.items()):
    if grade == ss:
        print(name)




