class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        cols = [0] * len(strs[0])
        prev = ['a'] * len(strs[0])
        for word in strs:
            for i, c in enumerate(word):
                if cols[i] == 0:
                    if prev[i] > c:
                        cols[i] = 1
                
                prev[i] = c
        
        print(cols)
        return sum(cols)
