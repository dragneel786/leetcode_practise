class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        ans = 0
        prev_heights = []
        
        for row in range(rows):
            heights = []
            seen = [False] * cols
            
            for height, col in prev_heights:
                if(matrix[row][col] == 1):
                    heights.append((height + 1, col))
                    seen[col] = True
            
            for col in range(cols):
                if(not seen[col] and matrix[row][col] == 1):
                    heights.append((1, col))
            
            min_val = inf
            for i, (h, c) in enumerate(heights):
                min_val = min(min_val, h)
                ans = max(h * (i + 1), ans)
            
            prev_heights = heights
        
        return ans
            
            
            
            