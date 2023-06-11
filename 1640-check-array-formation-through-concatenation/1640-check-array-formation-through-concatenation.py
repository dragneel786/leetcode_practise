class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        
        def formed(i = 0):
            if(len(arr) <= i):
                return len(arr) == i
            
            for p in pieces:
                if(p == arr[i:i + len(p)] and\
                   formed(i + len(p))):
                        return True
            
            return False
        
        return formed()