



def countingValleys(n, s):
    hae = 0
    valleys = 0
    for c in s:
        c = str.lower(c)
        if c == "u":
            hae += 1
            if hae == 0:
                valleys += 1
        if c == "d":
            hae -= 1
    return valleys




