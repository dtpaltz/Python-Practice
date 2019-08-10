# given a list of integers, and each integer H represents a tower with height H at that position.
# Starting at index 0 (first tower), and at each step, the amount of step available depend on the height of the
# current tower.
#
# Example: given a list of towers [4, 5, 6, 2, 1, 3]. Standing on the first tower the height is 4, then from there
# the next step could be at most 4 steps away to any index in [1, 2, 3, 4].
#
# Starting at index 0, is_hoppable returns TRUE if there is a series of steps that can be taken to reach outside the
# list, FALSE otherwise


def is_hoppable(towers: list):
    current = 0
    while True:
        if current >= len(towers):
            return True
        if towers[current] == 0:
            return False
        current = next_step(current, towers)


def next_step(curr_pos: int, towers: list):
    curr_height = towers[curr_pos]
    tower_map = []
    for idx, height in enumerate(towers):
        tower_map.append((idx, height))
    start = curr_pos + 1
    stop = start + curr_height
    if stop - 1 >= len(towers):
        return stop
    possible_next_steps = tower_map[start:stop]
    max_range_possible_next_steps = list(map(lambda s: (s[0], sum(s)), possible_next_steps))
    max_range = max(max_range_possible_next_steps)[1]
    for step in reversed(max_range_possible_next_steps):
        if step[1] == max_range:
            return step[0]
    return max_range_possible_next_steps[-1][0]


ts = [4, 2, 0, 0, 2, 0]
print(is_hoppable(ts))
