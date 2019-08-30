

def isNumberPalindrome(num: int):
    temp = num
    rev = 0

    while temp != 0:
        print('calc')
        rev = (rev * 10) + (temp % 10)
        temp = temp // 10

    if num == rev:
        print("number is palindrome")
    else:
        print("number is not palindrome")



isNumberPalindrome(12321)

