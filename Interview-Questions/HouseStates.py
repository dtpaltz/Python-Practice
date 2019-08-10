# There are N houses all in a row competing with each other. Each house has a state of active=1 or inactive=0
# at any given time. The state for each house the next day will be inactive=0 if both adjacent homes have equal state.
#
# You are given a list of house states and a number of days (days >= 0). The task is to return the state of the
# houses after the given number of days.
#
# Assume the missing house states on either end of the list are always inactive=0


def future_competing_houses(states, days):
    n = len(states)
    states.insert(0, 0)
    states.append(0)
    next_state = [0] * len(states)
    for d in range(days):
        for i in range(1, n + 1):
            next_state[i] = int(states[i - 1] != states[i + 1])
        states = next_state[:]
    return states[1:n + 1]


t_arr = [1, 1, 0, 1, 0, 1, 0, 0, 0, 1]
print(future_competing_houses(t_arr, 1) == [1, 1, 0, 0, 0, 0, 1, 0, 1, 0])
