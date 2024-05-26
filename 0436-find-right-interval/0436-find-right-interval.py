class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        starts = {}
        for i, (start, end) in enumerate(intervals):
            starts[start] = i
        
        starts = sorted(starts.items())
        
        res = []
        for start, end in intervals:
            idx = bisect_right(starts, (end,))
            res.append(starts[idx][1] if idx < len(starts) else -1)
        
        return res
