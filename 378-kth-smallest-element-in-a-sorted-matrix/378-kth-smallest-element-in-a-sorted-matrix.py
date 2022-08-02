class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        def count_less_equal(mid):
            row, col = rows - 1, 0
            small, large = matrix[0][0], matrix[rows - 1][cols - 1]
            counts = 0
            while(row > -1 and col < cols):
                if(matrix[row][col] > mid):
                    large = min(large, matrix[row][col])
                    row -= 1
                else:
                    counts += row + 1
                    small = max(small, matrix[row][col])
                    col += 1
            return counts, small, large
        
        rows, cols = len(matrix), len(matrix[0])
        start, end = matrix[0][0], matrix[rows - 1][cols - 1]
        while(start < end):
            mid = ((end - start) >> 1) + start
            count, smaller, larger = count_less_equal(mid)
            
            if(count == k):
                return smaller
            
            if(count < k):
                start = larger
            else:
                end = smaller
        return start