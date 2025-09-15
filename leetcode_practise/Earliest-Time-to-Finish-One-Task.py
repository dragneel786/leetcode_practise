class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        earliest = inf
        for s, t in tasks:
            earliest = min(earliest, s + t)

        return earliest