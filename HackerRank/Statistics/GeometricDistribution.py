

def geometric(p, n, x):
    return p**x * (1-p)**(n-x)


numerator, denominator = [1, 3]
n = float(5)
p = numerator / denominator
print(round(geometric(p, n, 1), 3))

print(round(1 - (1 - (1 / 3))**5, 3))
