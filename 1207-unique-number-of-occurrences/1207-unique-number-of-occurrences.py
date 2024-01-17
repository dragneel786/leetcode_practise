class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        index = [0] * 2001
        cmap = [0] * 1001
        for a in arr: index[a + 1000] += 1
        for v in index:
            if(v and cmap[v] > 0):
                return False
            cmap[v] += 1
        
        
        return True
        