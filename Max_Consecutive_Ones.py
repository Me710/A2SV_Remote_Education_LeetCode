class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        max_ones, cur_ones = 0, 0
        for n in nums:
            if n:
                cur_ones += 1
            else:
                max_ones = max(max_ones, cur_ones)
                cur_ones = 0
        return max(max_ones, cur_ones)