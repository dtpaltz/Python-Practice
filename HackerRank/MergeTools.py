# https://www.hackerrank.com/challenges/merge-the-tools/problem




def remove_duplicate_characters(s):
    seen = set()
    result = ""
    for c in s:
        if c not in seen:
            result += c
        seen.add(c)
    return result

def merge_the_tools(s, k):
    lines = [s[i:i + k] for i in range(0, len(s), k)]
    unique_lines = list(map(remove_duplicate_characters, lines))
    for l in unique_lines:
        print(l)


t_s = 'AABCAAADA'
t_k = 3
merge_the_tools(t_s, t_k)


