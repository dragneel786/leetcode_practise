class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        flatten = []
        for g in grid:
            for a in g:
                flatten.append(a)
        
        flatten.sort()
        final_num = flatten[len(flatten) // 2]
        res = 0
        for i in range(len(flatten)):
            if flatten[i] % x != final_num % x:
                return -1
            
            res += abs(final_num - flatten[i]) // x
        
        return res
        


