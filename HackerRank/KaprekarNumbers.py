# https://en.wikipedia.org/wiki/Kaprekar_number

def kaprekarNumbers(p, q):
    kNumbers = []
    for n in range(p, q + 1):
        ss = getSplitSums(n ** 2)
        if n in ss:
            kNumbers.append(n)
    print(*kNumbers)

def getSplitSums(num):
    digits = [int(x) for x in str(num)]
    n = len(digits)

    if n < 3:
        return [sum(digits)]

    sums = []
    for l in range(1, n):
        a = int(''.join(str(i) for i in digits[0:l]))
        b = digits[l:]

        if not all(v == 0 for v in b):
            b = int(''.join(str(i) for i in b))
            sums.append(a + b)

    return sums


def kaprekarNumbersOp(p, q):
    new=[]
    for k in range(p, q + 1):
        num = str(k**2)
        d = len(str(k))   # number of digits
        r = num[-d:]
        l = num[:-d]
        if not l:
            l = '0'
        if int(r)+int(l) == k:
            new.append(k)
    if new:
        print(' '.join([str(k) for k in new]))
    else:
        print("INVALID RANGE")




if __name__ == '__main__':
    p = 1
    q = 100

    kaprekarNumbers(p, q)

