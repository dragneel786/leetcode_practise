class Solution:
    def minimumPushes(self, word: str) -> int:
        pushes = 0
        degree = 1
        for i, c in enumerate(word):
            pushes += ((i // 8) + 1)
        
        return pushes
        
        
            
            
        