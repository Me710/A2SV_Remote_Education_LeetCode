class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        left = max(weights)
        right = sum(weights)

        while left < right:
            mid = (left + right) // 2
            total_days = 1
            current_weight = 0

            for weight in weights:
                if current_weight + weight > mid:
                    total_days += 1
                    current_weight = weight
                else:
                    current_weight += weight

            if total_days > days:
                left = mid + 1
            else:
                right = mid

        return left