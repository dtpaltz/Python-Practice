


def breakingRecords(scores):
    records = [scores[0], scores[0]]
    counts = [0, 0]
    for s in scores:
        if s > records[0]:
            counts[0] += 1
            records[0] = s
        if s < records[1]:
            counts[1] += 1
            records[1] = s
    return counts



print(breakingRecords([10, 5, 20, 20, 4, 5, 2, 25, 1]))
print(breakingRecords([3, 4, 21, 36, 10, 28, 35, 5, 24, 42]))