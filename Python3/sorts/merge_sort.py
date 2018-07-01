"""
Brian Taylor Vann
https://github.com/taylor-vann
"""


def merge_sort(arr):
    if len(arr) < 2:
        return arr

    point = len(arr) // 2

    return merge(merge_sort(arr[:point]), merge_sort(arr[point:]))


def merge(left, right):
    result = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    return result + left[left_index:] + right[right_index:]


if __name__ == "__main__":
    unittest.main()
