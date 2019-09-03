import time


def convert_to_binary(num):
    bitFill = (num // 256 + 1) * 8
    return bin(num)[2:].zfill(bitFill)


# Function to get count of set bits in binary representation of positive integer n
def countSetBits(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count


start = time.time()

for i in range(1000):
    print(countSetBits(i))

end = time.time()
print(end - start)
