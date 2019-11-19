# https://leetcode.com/problems/longest-common-prefix/
from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    if not strs:
        return ""

    prefix = strs[0]

    for s in strs:
        matchingPrefix = ""
        for index, c in enumerate(s):
            if len(prefix) > index and prefix[index] == c:
                matchingPrefix += c
            else:
                break
        prefix = matchingPrefix

    return prefix



args = ["dog", "racecar", "car"]
longestCommonPrefix([])
