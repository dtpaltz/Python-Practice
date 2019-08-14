# https://www.hackerrank.com/challenges/the-minion-game/problem

vowels = ['a', 'e', 'i', 'o', 'u']


def minion_game(s):
    s = s.lower()
    kevsc = 0
    stusc = 0
    for i in range(len(s)):
        if s[i] in vowels:
            kevsc += (len(s)-i)
        else:
            stusc += (len(s)-i)

    if kevsc > stusc:
        print("Kevin", kevsc)
    elif kevsc < stusc:
        print("Stuart", stusc)
    else:
        print("Draw")


t_s = 'banana'
minion_game(t_s)

