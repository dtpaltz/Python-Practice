# function to find the once
# appearing element in array
def findSingle(ar, n):
    res = ar[0]

    # Do XOR of all elements and return
    for i in range(1, n):
        print("  {0:b}".format(res))
        print("^ {0:b}".format(ar[i]))
        res = res ^ ar[i]
        print("= {0:b}   ==   {1}".format(res, res))
        print('----------')

    return res


# Driver code
ar = [3, 5, 2, 4, 5, 3, 4]
print("Element occurring once is", findSingle(ar, len(ar)))



