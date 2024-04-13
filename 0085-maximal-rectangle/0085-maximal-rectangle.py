class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        
        def max_histo_area(histo):
            max_area = 0
            histo.append(0)
            st = deque()
            for i, h in enumerate(histo):
                while(st and histo[st[-1]] > h):
                    width = histo[st.pop()]
                    left_small = st[-1] if(st) else -1
                    temp_area = (i - left_small - 1) * width
                    max_area = max(max_area, temp_area)

                st.append(i)

            return max_area
        
        m, n = len(matrix), len(matrix[0])
        heights = [0] * n
        res = 0
        for i in range(m):
            for j in range(n):
                if(matrix[i][j] == '0'):
                    heights[j] = 0
                else:
                    heights[j] += 1
            
            res = max(res, max_histo_area(heights))
            
        
        return res
                