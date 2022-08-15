class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        removed = set()
        
        def next_val(start):
            while(start in removed):
                start = (start + 1) % n
            return start
        
        start = 0
        while(len(removed) < n - 1):
            for _ in range(k - 1):
                start = next_val((start + 1) % n)
                
            removed.add(start)
            start = next_val(start)
        
        for i in range(n):
            if(i not in removed):
                return i + 1
        
        