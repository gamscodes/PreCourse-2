# Python code to implement iterative Binary Search.
# It returns location of x in given array arr
# if present, else returns -1


# Time Complexity: O(log n) bcz serach space is halved with each step
# Space Complexity: O(1) as there is no additional DS getting used which grows with the input size
def binarySearch(arr, l, r, x):

    # write your code here
    while l <= r:
        mid = (l + r) // 2

        if arr[mid] == x:  # check if x is at the mid index
            return mid
        elif arr[mid] > x:  # if x is smaller then search on the left side
            r = mid - 1
        else:  # if x is larger then search on the right side
            l = mid + 1
    return -1  # if x is not in the array


# Test array
arr = [2, 3, 4, 10, 40]
x = 10

# Function call
result = binarySearch(arr, 0, len(arr) - 1, x)

if result != -1:
    print(f"Element is present at index {result}")
else:
    print("Element is not present in array")
