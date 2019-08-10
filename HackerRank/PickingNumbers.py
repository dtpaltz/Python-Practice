



def pickingNumbers(a):
    groups = {}

    for f in range(1, max(a)):
        this_filter = (f, f + 1)
        groups[f] = 0
        for n in a:
            if n in this_filter:
                groups[f] += 1

    #print(groups)
    return max(groups.values())









t1 = [4, 6, 5, 3, 3, 1]
t2 = [1, 2, 2, 3, 1, 2]
print(pickingNumbers(t1))
print(pickingNumbers(t2))