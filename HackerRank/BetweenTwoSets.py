
def gcd(a, b):
    """Compute the greatest common divisor of a and b"""
    while b > 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    """Compute the lowest common multiple of a and b"""
    return a * b / gcd(a, b)


def ar_gcd(a):
    """Compute the greatest common multiple of an array"""
    x = a[0]
    for i in a[1:]:
        x = x * i / lcm(x, i)
    return x


def ar_lcm(a):
    """Compute the lowest common multiple of an array"""
    x = a[0]
    for i in a[1:]:
        x = x * i / gcd(x, i)
    return x







def getTotalX(a, b):
    a_lcm = ar_lcm(a)
    b_gcd = ar_gcd(b)
    count = 0
    for i in range(1, 1000):
        x = (i * a_lcm)
        if x > b_gcd:
            break
        if b_gcd % x == 0:
            count += 1
    return count


a = [2, 4]
b = [16, 32, 96]

print(getTotalX(a, b))
