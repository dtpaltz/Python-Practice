import math

def theLoveLetterMystery(s):
    needed_change_count = 0
    for i in range(len(s)):
        if (i + 1) > math.floor(len(s) / 2):
            break

        a = ord(s[i])
        b = ord(s[len(s) - 1 - i])
        needed_change_count += abs(a - b)

    return needed_change_count




theLoveLetterMystery("abc")
theLoveLetterMystery("abcba")
theLoveLetterMystery("abcd")
theLoveLetterMystery("cba")





