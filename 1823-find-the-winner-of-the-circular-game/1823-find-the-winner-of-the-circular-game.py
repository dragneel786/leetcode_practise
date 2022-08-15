class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        removed = set()
        people = set([i for i in range(n)])
        
        def next_val(start):
            while(start in removed):
                start = (start + 1) % n
            return start
        
        start = 0
        while(len(removed) < n - 1):
            for _ in range(k - 1):
                start = next_val((start + 1) % n)
                
            removed.add(start)
            people.discard(start)
            start = next_val(start)
        
        return people.pop() + 1
        
        