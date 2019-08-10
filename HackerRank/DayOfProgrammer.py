import datetime




def dayOfProgrammer(year):
    dop = None
    if year == 1918:
        dop = datetime.date(year, 9, 26)
    elif ((year <= 1917) & (year % 4 == 0)) or ((year > 1918) & (year % 400 == 0 or ((year % 4 == 0) & (year % 100 != 0)))):
        dop = datetime.date(year, 9, 12)
    else:
        dop = datetime.date(year, 9, 13)

    return dop.strftime("%d.%m.%Y")



print(dayOfProgrammer(1800))
print(dayOfProgrammer(2016))
print(dayOfProgrammer(2017))

