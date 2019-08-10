
def climbingLeaderboard(scores, alice):
    n = len(scores)
    m = len(alice)

    alice_ranks = []
    ranks = [1]

    for i in range(1, n):
        if scores[i] == scores[i - 1]:
            ranks.append(ranks[i - 1])
        else:
            ranks.append(ranks[i - 1] + 1)

    for i in range(m):
        alice_score = alice[i]
        if alice_score > scores[0]:
            alice_ranks.append(1)
        elif alice_score < scores[n - 1]:
            alice_ranks.append(ranks[n - 1] + 1)
        else:
            idx = binary_search(scores, alice_score)
            alice_ranks.append(ranks[idx])

    return alice_ranks


def binary_search(arr, key):
    lo = 0
    hi = len(arr) - 1

    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key < arr[mid - 1]:
            return mid
        elif arr[mid] > key >= arr[mid + 1]:
            return mid + 1
        elif arr[mid] < key:
            hi = mid - 1
        elif arr[mid] > key:
            lo = mid + 1

    return "ERR"











s = [100, 100, 50, 40, 40, 20, 10]
a = [5, 25, 50, 120]
print(climbingLeaderboard(s, a))
print("{0}  ---  expected".format([6, 4, 2, 1]))
print("-----------------------------------------------")
s = [100, 90, 90, 80, 75, 60]
a = [50, 65, 77, 90, 102]
print(climbingLeaderboard(s, a))
print("{0}  ---  expected".format([6, 5, 4, 2, 1]))



