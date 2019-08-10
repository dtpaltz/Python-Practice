
x = ''.join(list(map(str, ['a', 4, 'b', 6])))

x = ''.join([x for x in map(str, ['a', 4, 'b', 6])])
# print ', '.join(str(x) for x in list_of_ints)


def compress_string(s: str):
    compressStr = ""
    n = len(s)
    runCount = 0

    for i, c in enumerate(s):
        runCount += 1

        if i + 1 >= n or c != s[i + 1]:
            compressStr = "".join([compressStr, c, str(runCount)])
            runCount = 0

    if len(compressStr) < n:
        return compressStr
    else:
        return s


print(compress_string("aabcccccaaa"))

