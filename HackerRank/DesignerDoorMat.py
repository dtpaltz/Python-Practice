if __name__ == '__main__':
    n, m = [7, 21]

    top_lines = []
    end_lines = []

    for i in range(1, n):
        if i % 2 != 0:
            s = '.|.' * i
            top_lines.append(s)
            end_lines.insert(0, s)

    lines = [] + top_lines
    lines.append('WELCOME')
    lines += end_lines

    for i in range(len(lines)):
        l = lines[i]
        d = (m - len(l)) // 2
        dashes = '-' * d
        print(dashes, l, dashes, sep='')

