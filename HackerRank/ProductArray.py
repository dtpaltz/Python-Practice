def productArray(arr, n):
    # Allocate memory for temporary arrays left[] and right[]
    left = [0] * n
    right = [0] * n

    # Allocate memory for the product array
    prod = [0] * n

    # Left most element of left array is always 1
    left[0] = 1

    # Rightmost most element of right array is always 1
    right[n - 1] = 1

    # Construct the left array
    for i in range(1, n):
        left[i] = arr[i - 1] * left[i - 1]

    print(left)

    # Construct the right array
    for j in range(n - 2, -1, -1):
        right[j] = arr[j + 1] * right[j + 1]

    print(right)

    # Construct the product array using
    #   left[] and right[]
    for i in range(n):
        prod[i] = left[i] * right[i]

    # print the constructed prod array
    for i in range(n):
        print(prod[i], end=' ')

    # Driver code


arr = [1, 2, 3, 4]
n = len(arr)
print("The product array is:")
productArray(arr, n)