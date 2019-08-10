# Add 1 to some number represented in a given array
# Return the result as an array


def add_one_rec(given_array, index):
    print('{0}  :  {1}'.format(given_array, index))

    if index < 0:
        given_array = [0] * (len(given_array) + 1)
        given_array[0] = 1
    else:
        n = given_array[index]
        if n > 9 or n == 0:
            print("Array Invalid!")
            given_array = [0] * (len(given_array))
        elif n == 9:
            given_array[index] = 0
            return add_one_rec(given_array, index - 1)
        elif n < 9:
            given_array[index] = n + 1

    return given_array


def add_one(given_array):
    return add_one_rec(given_array, len(given_array) - 1)


n0 = [5, 9, 9]
n1 = [9, 9, 9]
n2 = [1, 2, 9, 9]
n3 = [15, 10, 50]
n4 = [0, 9, 9]


print(add_one(n0))
print("----------------")
print(add_one(n1))
print("----------------")
print(add_one(n2))
print("----------------")
print(add_one(n3))
print("----------------")
print(add_one(n4))

print()
print('         '+'#')
