

def are_permutations(str1, str2):
    if len(str1) != len(str2):
        return False

    char_tally = [0] * 128

    for c in str1:
        char_tally[ord(c)] += 1

    for c in str2:
        char_tally[ord(c)] -= 1
        if char_tally[ord(c)] < 0:
            return False

    return True


# print(are_permutations("HeLlo", "Hello"))



def is_palindrome_permutation(s: str):
    char_tally = {}

    for c in s:
        if c not in char_tally:
            char_tally[c] = 0
        char_tally[c] += 1

    single_char_count = 0
    for c, t in char_tally.items():
        if t > 1 and t % 2 != 0:
            return False
        else:
            single_char_count += int(t == 1)

    return single_char_count <= 1



t_s = "tactcoapapa"
print(is_palindrome_permutation(t_s))























