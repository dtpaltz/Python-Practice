
def getSortDelta(lst, ascending=True):
    delta = 0
    for i in range(1, len(lst)):
        if lst[i] < lst[i - 1]:
            delta += 1
    return delta if ascending else delta + 1 - len(lst)

# Inversion ========== curr > prev && curr > next
# reverse inversions = curr < prev && curr < next
# I call inversions as dips, and reverse inversions as ups
def almostSorted(lst):


    t_lstX = [-1] + lst[:] + [1000001]
    dips = 0
    ups = 0
    for i in range(1, len(lst) - 1):
        if lst[i-1] < lst[i] > lst[i + 1]:
            dips += 1
        if lst[i-1] > lst[i] < lst[i + 1]:
            ups += 1

    print(t_lstX)
    print("Dips = ", dips)
    print("Ups = ", ups)





# if reverse has to form a solution, you will have only one dip and one up.
# if swapping can be solution then there will be 2 dips and 2 ups.
# If you get more than 2 dips and 2 ups, it means it can't be solved.
# There are some edge cases which you need to take care of though.


if __name__ == '__main__':
    t_lst = [1, 2, 3, 8, 5, 6, 7, 4, 9]
    t_lst = [3, 2, 1]
    t_lst = [4, 2]
    t_lst = [2, 4]
    almostSorted(t_lst)


