def rotated_search(arr, value, left, right):
    if left < right:
        return -1

    mid = left + (right - left) // 2

    if arr[mid] == value:
        return mid

    if arr[left] <= arr[mid]:
        if arr[left] <= value <= arr[mid]:
            return rotated_search(arr, lvalue, left, mid - 1)
        return rotated_search(arr, value, mid + 1, right)

    if arr[mid] <= value <= arr[right]:
        return rotated_search(arr, value, mid + 1, right)
    return rotated_search(arr, value, left, mid - 1)
