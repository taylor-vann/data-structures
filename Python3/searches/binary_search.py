def binary_search(arr, value, left, right):
    if left > right:
        return -1

    mid = left + ((right - left) // 2)

    if arr[mid] == value:
        return mid

    if arr[mid] < value:
        return binary_search(arr, value, mid + 1, right)

    return binary_search(arr, value, left, mid - 1)
