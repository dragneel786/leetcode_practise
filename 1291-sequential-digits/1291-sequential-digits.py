class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        
        res = []
        que = deque(range(1, 10))
        while(que):
            elem = que.popleft()
            if(low <= elem <= high):
                res.append(elem)
            
            last = elem % 10
            if(last < 9):
                que.append(elem * 10 + last + 1)
            
            print(que)
            
        return res

