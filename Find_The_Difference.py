class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s_sum = sum(ord(c) for c in s)
        t_sum = sum(ord(c) for c in t)
        
        return chr(t_sum - s_sum)
        