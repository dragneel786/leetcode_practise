class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        
        def form_arr(i = 0, val = 0):
            if i == 3:
                if val % 2 == 0:
                    res.append(val)
                return
            
            ranges = range(0, 10, 2)
            if i == 0:
                ranges = range(1, 10)
            
            if i == 1:
                ranges = range(0, 10)
            
            for v in ranges:
                if counts[v]:
                    counts[v] -= 1
                    form_arr(i + 1, val * 10 + v)
                    counts[v] += 1
 
        res = []
        counts = Counter(digits)
        form_arr()
        return res
