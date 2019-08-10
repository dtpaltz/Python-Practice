
def binary_search(arr, x):
    return binary_search_recursive(arr, 0, len(arr) - 1, x)


# Returns index of x in arr if present, else -1
def binary_search_recursive(arr, left, right, x):
    # Check base case
    if right >= left:
        mid = left + (right - left) // 2
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
        # If element is smaller than mid, then it can only be present in left subarray
        elif arr[mid] > x:
            return binary_search_recursive(arr, left, mid - 1, x)
            # Else the element can only be present in right subarray
        else:
            return binary_search_recursive(arr, mid + 1, right, x)
    else:
        # Element is not present in the array
        return -1











# Test array
t_arr = [2, 3, 4, 10, 16, 18, 22, 28, 35, 40]
f = 28

# Function call
result = binary_search(t_arr, f)

if result != -1:
    print("Element is present at index % d" % result)
else:
    print("Element is not present in array")

