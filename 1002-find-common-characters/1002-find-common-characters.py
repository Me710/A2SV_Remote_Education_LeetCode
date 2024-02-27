class Solution:
    def commonChars(self, words):
        result = [float('inf')] * 26
        for word in words:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')] += 1
            for i in range(26):
                result[i] = min(result[i], count[i])
        output = []
        for i in range(26):
            output.extend([chr(i + ord('a'))] * result[i])
        return output
