class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        result = ''
        i, j = 0, 0
        m, n = len(word1), len(word2)
        
        while i < m and j < n:
            result += word1[i]
            result += word2[j]
            i += 1
            j += 1
        
        result += word1[i:]
        result += word2[j:]

        return result
        