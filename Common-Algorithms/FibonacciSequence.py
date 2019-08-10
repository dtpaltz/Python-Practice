# The Fibonacci Sequence is the series of numbers:
#     0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
#
# The next number is found by adding up the two numbers before it.
#
# The 2 is found by adding the two numbers before it (1+1)
# The 3 is found by adding the two numbers before it (1+2), and the 5 is (2+3), and so on!


# This is the classic method
def fib_seq(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end='   ')
        a, b = b, a + b
    print()


fib_seq(10)


# This method yields a generator to save memory space
def fib_gen(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b


for item in fib_gen(10):
    print(item, end='   ')
print()
