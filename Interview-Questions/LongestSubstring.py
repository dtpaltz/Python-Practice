# This problem was recently asked by Microsoft:
#
# Given a string, find the length of the longest substring without repeating characters.

class Solution:
    @staticmethod
    def lengthOfLongestSubstring(s):
        seen = set()
        maxss = 0  # max substring length
        for ch in s:
            if ch in seen:
                seen = set(ch)
            else:
                seen.add(ch)

            if len(seen) > maxss:
                maxss = len(seen)

        return maxss


print(Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx'))

