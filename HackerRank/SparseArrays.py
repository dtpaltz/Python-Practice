
def matchingStrings(strings, queries):
    string_dict = {}
    for s in strings:
        if s in string_dict:
            string_dict[s] += 1
        else:
            string_dict[s] = 1

    res = []
    for q in queries:
        if q in string_dict.keys():
            res.append(string_dict[q])
        else:
            res.append(0)

    return res


a1 = ['aba', 'baba', 'aba', 'xzxb']
a2 = ['aba', 'xzxb', 'ab']
print(matchingStrings(a1, a2))


a1 = ['abcde', 'sdaklfj', 'asdjf', 'na', 'basdn', 'sdaklfj', 'asdjf', 'na', 'asdjf', 'na', 'basdn', 'sdaklfj', 'asdjf']
a2 = ['abcde', 'sdaklfj', 'asdjf', 'na', 'basdn']
print(matchingStrings(a1, a2))
