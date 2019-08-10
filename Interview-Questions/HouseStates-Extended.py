import copy

class StateChanger:
    """House state changer

    Attributes:
        start_state (int[]): initial state to start from

    """
    def __init__(self, starting_state):
        """Initializes a new instance

        Args:
            starting_state (int[]): initial state to start from

        """
        self.start_state = starting_state

    def get_future_state(self, days):
        """Generates the future state after the given number of days

        Args:
            days (int): The first parameter.

        Returns:
            int[]: The future state after the given number of days

        """
        current_state = copy.copy(self.start_state)
        n = len(current_state)  # original length of the current_state list
        current_state.insert(0, 0)  # this will be easier to append inactive to both ends of the current_state lists
        current_state.append(0)  # since the ends will always be inactive, this is essentially employing a null-object pattern
        next_state = [0] * len(current_state)  # this list will contain the state of the next day
        for d in range(days):
            # for d days, update state with the next_state after it updates
            for i in range(1, n + 1):  # looping over the current_state excluding the first and last inactive elements
                # the next state for THIS cell = int value of the logical evaluation of the adjacent cells being different (False = 0, True = 1)
                next_state[i] = int(current_state[i - 1] != current_state[i + 1])
            current_state = copy.copy(next_state)  # now that next_state is updated, update current_state to be equal to the next_state
        return current_state[1:n + 1]  # return the current_state excluding the first and last inactive elements


def cellCompete(states, days):
    changer = StateChanger(states)
    return changer.get_future_state(days)




t_d = 7
t_states = [0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1]
print(cellCompete(t_states, t_d))








from fractions import gcd
from functools import reduce
def generalizedGCD(num, list):
    x = reduce(gcd, list)
    return x











