class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        """Fastest solution but i want some divide and conquer"""
        # return sorted(nums, reverse=True)[k - 1]

        sorted_nums = [0] * len(nums)

        def divide(left, right):
            if left == right:
                return
            mid = (left + right) // 2  
            divide(left, mid)
            divide(mid + 1, right)
            conquer(left, mid, right)

        def conquer(left, mid, right):
            tmp_l, tmp_r = left, mid + 1
            for i in range(left, right + 1):
                if tmp_l <= mid and tmp_r <= right:
                    if nums[tmp_l] >= nums[tmp_r]:
                        sorted_nums[i] = nums[tmp_l]  
                        tmp_l += 1
                    else: 
                        sorted_nums[i] = nums[tmp_r]
                        tmp_r += 1
                else:
                    if tmp_l <= mid:
                        sorted_nums[i] = nums[tmp_l]
                        tmp_l += 1
                    elif tmp_r <= right:
                        sorted_nums[i] = nums[tmp_r]
                        tmp_r += 1
            nums[left:right+1] = sorted_nums[left:right+1]


        divide(0, len(nums) - 1)
        return sorted_nums[k - 1]