


def getMoneySpent(keyboards, drives, b):
    r = 0
    for k in keyboards:
        for d in drives:
            s = k + d
            if  r < s <= b:
                r = s
    return r




