class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        index_map = defaultdict(deque)
        for i, c in enumerate(t):
            index_map[c].append(i)
        
        curr_idx = -1
        for c in s:
            while(index_map[c] and \
                  curr_idx > index_map[c][0]):
                index_map[c].popleft()
            
            if(index_map[c]):
                curr_idx = index_map[c].popleft()
            else:
                return False
            
        return True
                
            
            
        
        