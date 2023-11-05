class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        curr = arr[0]
        win = 0
        for i in range(1, len(arr)):
            if(arr[i] > curr):
                win = 0
                curr = arr[i] 
            win += 1
            if(win == k): return curr
        
        return curr
            
        
        