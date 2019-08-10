
def utopianTree(n):
    height = 1

    for i in range(1, n + 1):
        if i % 2 == 0:
            # even cycle tree grows by 1
            height += 1
        else:
            # odd cycle tree doubles
            height *= 2

    return height



print(utopianTree(0))
print(utopianTree(1))
print(utopianTree(4))












