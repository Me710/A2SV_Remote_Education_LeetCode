class Solution(object):
    def matchPlayersAndTrainers(self, players, trainers):
        """
        :type players: List[int]
        :type trainers: List[int]
        :rtype: int
        """
        players.sort()  
        trainers.sort()

        n, m = len(players), len(trainers)
        i, j = 0, 0
        match_count = 0

        while i < n and j < m:
            if players[i] <= trainers[j]:
                match_count += 1
                i += 1
                j += 1
            else:
                j += 1

        return match_count