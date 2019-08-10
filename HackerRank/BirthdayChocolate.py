
def birthday(s, d, m):
    count = 0
    for i in range(len(s)):
        total = sum(s[i:m + i])
        if total == d:
            count += 1
    return count





print(birthday([1, 2, 1, 3, 2], 3, 2))
print(birthday([1, 1, 1, 1, 1, 1], 3, 2))
print(birthday([4], 4, 1))
