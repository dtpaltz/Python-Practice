import math

# Task 1
# Create an algorithm in which given a coin cent value it returns a total number of coins needed to reach that amount.
# Using quarter=25, dime=10, nickel=5, penny=1...
# Then one solution for 31 = 1 quarter + 1 nickel + 1 penny = 3 coins


def num_coins(cents):
    coins = [25, 10, 5, 1]
    if cents < min(coins):
        return 0
    total_count = 0
    for c in coins:
        total_count += cents // c
        cents %= c
    return total_count


#print(num_coins(31))


# Task 2
# The algorithm is Task 1 is kinda greedy, it returns A solution, but not necessarily the best one.
# Now consider that you cannot utilize nickels=5, now the algorithm is very sub-optimal
# Example: 31 cents = 1 quarter + 6 pennies = 7 coins
# Better: 3 dimes + 1 penny = 4 coins
#
# Re-work the algorithm to return the minimum number of coins needed to reach the amount given.


def min_coin_change(n, coins_available, coins_seen):
    if sum(coins_seen) == n:
        yield coins_seen
    elif sum(coins_seen) > n:
        pass
    elif coins_available:
        for c in min_coin_change(n, coins_available[:], coins_seen + [coins_available[0]]):
            yield c

        for c in min_coin_change(n, coins_available[1:], coins_seen):
            yield c


n = 31
coins = [1, 5, 10, 25]
solutions = [s for s in min_coin_change(n, coins, [])]
for s in solutions:
    print(s)

print("Optimal solution = {}".format(min(solutions, key=len)))

# print(min_coin_change([25, 10, 1], 31))

