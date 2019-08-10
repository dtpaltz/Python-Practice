

def remove_alternating_duplicates(line: str):
    seen = {}
    ans = ''
    for c in line:
        if c not in seen:
            seen[c] = 0
        seen[c] += 1
        if seen[c] % 2 != 0:
            ans += c
    return ans







t_line = 'you got beautiful eyes'
print(remove_alternating_duplicates(t_line))






