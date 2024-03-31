class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[List[int]]
        :rtype: str
        """
        n = len(s)
        shifts_sum = [0] * (n + 1)

        for start, end, direction in shifts:
            if direction == 0:
                shifts_sum[start] -= 1
                shifts_sum[end + 1] += 1
            else:
                shifts_sum[start] += 1
                shifts_sum[end + 1] -= 1

        total_shift = 0
        result = []
        for i in range(n):
            total_shift += shifts_sum[i]
            new_char = chr(ord('a') + (ord(s[i]) - ord('a') + total_shift) % 26)
            result.append(new_char)

        return ''.join(result)