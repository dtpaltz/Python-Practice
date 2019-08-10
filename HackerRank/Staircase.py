# Consider a staircase of size: n = 4
#     #
#    ##
#   ###
#  ####
#
# Observe that its base and height are both equal to n, and the image is drawn using # symbols
# and spaces. The last line is not preceded by any spaces.
#
# Write a program that prints a staircase of size n.


def staircase(n):
    staircase_str = ""

    for i in range(n):
        iter_str = '#' * (i + 1)
        just_iter_str = ' ' * ((n - i) - 1)
        staircase_str = staircase_str + just_iter_str + iter_str + '\n'

    print(staircase_str[:-1])


staircase(6)
