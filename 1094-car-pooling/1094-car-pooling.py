class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
            """
        locations = [0] * 1001

        for trip in trips:
            numPassengers, start, end = trip
            locations[start] += numPassengers
            locations[end] -= numPassengers

        currentPassengers = 0
        for passengers in locations:
            currentPassengers += passengers
            if currentPassengers > capacity:
                return False

        return True
