

def print_rangoli(size):
    start = 96 + size
    lines = []

    for i in range(1, size + 1):
        s = ''
        for j in range(i):
            c = chr(start - j)
            if j > 0:
                s += '-'
            s += c
        s += s[:-1][::-1]
        lines.append(s)

    w = len(lines[len(lines) - 1])
    lines += lines[:-1][::-1]

    for i in range(len(lines)):
        l = lines[i]
        d = (w - len(l)) // 2
        dashes = '-' * d
        print(dashes, l, dashes, sep='')




print_rangoli(5)

