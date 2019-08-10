


def alternatingCharacters(s):
    count = 0
    for c in range(len(s)):
        if c > 0 and s[c] == s[c - 1]:
            count += 1
    return count





