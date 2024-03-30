class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        n = len(cardPoints)
        window_size = n - k
        total_sum = sum(cardPoints)
        min_sum = float('inf')
        current_sum = 0

        for i in range(n):
            current_sum += cardPoints[i]
            if i >= window_size:
                current_sum -= cardPoints[i - window_size]
            if i >= window_size - 1:
                min_sum = min(min_sum, current_sum)

        return total_sum - min_sum
