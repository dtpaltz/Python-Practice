
def dynamicArray(n, queries):
    lastNumber = 0
    seqList =[]
    for i in range(n):
        seqList.append([])

    res = []

    for k, x, y in queries:
        index = ( x ^lastNumber ) % n
        if k == 1:
            seqList[index].append(y)
            # print(seqList)
        else:
            size = len(seqList[index])
            # print(seqList)
            # print(size)
            lastNumber = seqList[index][y % size]
            # print(lastNumber)
            res.append(lastNumber)

    return res



a1 = 2
a2 = [[1, 0, 5], [1, 1, 7], [1, 0, 3], [2, 1, 0], [2, 1, 1]]
print(dynamicArray(a1, a2))
