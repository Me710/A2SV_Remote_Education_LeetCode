class Solution(object):
    def shuffle(self, nums, n):
        x = nums[:n]
        y = nums[n:]
        
        result = []
        
        for i in range(n):
            result.append(x[i])
            result.append(y[i])
        
        return result
