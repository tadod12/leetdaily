# Using Python3
class Solution:
    def maxLength(self, nums: List[int]) -> int:
        sub_len, nums_len = len(nums), len(nums)
        while sub_len > 0:
            start = 0
            while start <= nums_len - sub_len:
                if math.prod(nums[start: start + sub_len]) == math.gcd(*nums[start: start + sub_len]) * math.lcm(*nums[start: start + sub_len]):
                    print(nums[start: start + sub_len])
                    return sub_len
                start += 1
            sub_len -= 1
        return 1

# 38.04%
