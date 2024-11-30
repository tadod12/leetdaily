nums = [20, 13, 1, 3]
res = [0] * len(nums)

def merge(left, right, mid):
    l, r, k = left, mid + 1, 0
    while l <= mid and r <= right:
        if nums[l] <= nums[r]:
            res[k] = nums[l]
            l += 1
        else:
            res[k] = nums[r]
            r += 1
        k += 1

    while l <= mid:
        res[k] = nums[l]
        k, l = k + 1, l + 1
    while r <= right:
        res[k] = nums[r]
        k, r = k + 1, r + 1

    for i in range(0, k):
        nums[left + i] = res[i]
 

def merge_sort(left, right):
    if left >= right:
        return
    mid = (left + right) // 2
    merge_sort(left, mid)
    merge_sort(mid + 1, right)
    merge(left, right, mid)


merge_sort(0, len(nums) - 1)
print(nums)