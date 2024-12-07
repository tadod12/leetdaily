""" ASCENDING QUICK SORT
    Using last element as povit
"""

arr = [14, 25, 100, 14, 1, 17]


def quick_sort(left, right):
    if left >= right:
        return
    pivot = right
    l, r = left, pivot - 1

    while l <= r:
        if arr[l] <= arr[pivot]:
            l += 1
        elif arr[r] >= arr[pivot]:
            r -= 1
        else:
            arr[l], arr[r] = arr[r], arr[l]

    arr[pivot], arr[l] = arr[l], arr[pivot]
    quick_sort(left, pivot - 1)
    quick_sort(pivot + 1, right)

quick_sort(0, len(arr) - 1)
print(arr)