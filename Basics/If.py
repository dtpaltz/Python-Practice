# What values does IF determine true and false?

values = [None, False, "", '', [], (), {}, 0]

for v in values:
    if v:
        print(str(v) + " \t\t is True")
    else:
        print(str(v) + " \t\t is False")
