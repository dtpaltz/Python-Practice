# return true value of there being a pair of values in the given array that sum to the target value


def has_pair_with_sum(data, sum):
    comp = set()  # seen complements
    for n in data:
        if n in comp:
            return True
        comp.add(sum - n)
    return False


print(has_pair_with_sum([1, 2, 3, 9], 8))

print(has_pair_with_sum([1, 2, 4, 4], 8))
