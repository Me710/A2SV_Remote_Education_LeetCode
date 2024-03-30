from collections import defaultdict

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        tMap = {}
        sMap = {}
        for char in t:
            tMap[char] = tMap.get(char, 0) + 1

        left = 0
        right = 0
        requiredChars = len(tMap)
        foundChars = 0
        minLength = float('inf')
        start = 0

        while right < len(s):
            sMap[s[right]] = sMap.get(s[right], 0) + 1
            if s[right] in tMap and sMap[s[right]] == tMap[s[right]]:
                foundChars += 1

            while foundChars == requiredChars:
                if right - left + 1 < minLength:
                    minLength = right - left + 1
                    start = left

                sMap[s[left]] -= 1
                if s[left] in tMap and sMap[s[left]] < tMap[s[left]]:
                    foundChars -= 1

                left += 1

            right += 1

        if minLength == float('inf'):
            return ""
        else:
            return s[start:start + minLength]
