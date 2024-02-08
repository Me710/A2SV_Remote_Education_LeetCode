class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        good_pairs = 0
        for num_count in count.values():
            good_pairs += num_count * (num_count - 1) // 2
        
        return good_pairs