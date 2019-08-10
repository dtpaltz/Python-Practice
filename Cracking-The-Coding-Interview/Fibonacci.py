

def fib_standard(i: int):
    if i == 0:
        return 0
    if i == 1:
        return 1

    return fib_standard(i - 1) + fib_standard(i - 2)


# print(fib_standard(50))


def fib(i):
    return fib_memo(i, [0] * (i + 1))


def fib_memo(i, memo):
    if i in (0, 1):
        return i

    if memo[i] == 0:
        memo[i] = fib_memo(i - 1, memo) + fib_memo(i - 2, memo)

    return memo[i]


print(fib(500))


