class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        delete_col = set()
        prev = strs[0]
        for curr in strs[1:]:
            for i, (a, b) in enumerate(zip(prev, curr)):
                if(a > b):
                    delete_col.add(i)
            if(len(delete_col) == len(strs[0])):
                break
            
            prev = curr
        
        return len(delete_col)
            
        