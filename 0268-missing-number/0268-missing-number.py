class Solution(object):
    def missingNumber(self, nums):
        nums.sort()
        return next((i for i, v in enumerate(nums) if i != v), len(nums))
