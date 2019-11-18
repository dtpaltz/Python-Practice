# This problem has been asked by Blue Origin.
#
# Given a numbers, determine if the number is a palindrome without using any String data types.
#
# For example, 12321 is a palindrome, but 12325 is not

def isNumberPalindrome(num: int):
    temp = num
    rev = 0
    print(num)

    while temp != 0:
        rev = (rev * 10) + (temp % 10)
        print(rev)
        temp = temp // 10

    if num == rev:
        print("number is a palindrome")
    else:
        print("number is not a palindrome")

    return num == rev


isNumberPalindrome(12321)

