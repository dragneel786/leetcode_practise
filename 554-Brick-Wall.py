class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        wall_break = Counter()
        for row in wall:
            tot = 0
            for val in row:
                tot += val
                wall_break[tot] += 1
        
        row_sum = sum(row)
        gaps = 0
        for k, v in wall_break.items():
            if k != row_sum:
                gaps = max(gaps, v)
        
        return len(wall) - gaps
            