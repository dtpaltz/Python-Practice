#https://leetcode.com/problems/palindrome-number/

def isPalindrome(x: int):
    temp = x
    rev = 0

    if x > 0:
        while temp != 0:
            rev = (rev * 10) + (temp % 10)
            temp = temp // 10

    return x == rev


ans = isPalindrome(1)
print(ans)
