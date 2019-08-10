import collections


def treasure_route(grid, start):
    width = len(grid[0])
    height = len(grid)
    goal = get_goal_location(grid)
    path_queue = collections.deque([[start]])
    visited = set([start])
    while path_queue:
        path = path_queue.popleft()
        row, col = path[-1]
        if (row, col) == goal:
            return report_solution(path)
        for row2, col2 in ((row - 1, col), (row, col + 1), (row + 1, col), (row, col - 1)):
            if 0 <= row2 < height and 0 <= col2 < width and str(grid[row2][col2]).lower() != 'd' and (row2, col2) not in visited:
                path_queue.append(path + [(row2, col2)])
                visited.add((row2, col2))
    report_solution([])


def get_goal_location(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if str(grid[i][j]).lower() == 'x':
                loc = (i, j)
                return loc


def print_grid(grid):
    s = [[str(e) for e in row] for row in grid]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print('\n'.join(table))


def report_solution(path):
    n = len(path)
    if n > 0:
        print(path)
        print("The minimum route takes {0} steps.".format(n - 1))
    else:
        print("No path found!")


gr = [
    ['O', 'O', 'O', 'O'],
    ['D', 'O', 'D', 'O'],
    ['O', 'O', 'O', 'O'],
    ['X', 'D', 'D', 'O'],
]

print_grid(gr)
treasure_route(gr, (0, 0))

