class Solution:
    def pivotInteger(self, n: int) -> int:
        tot = sum(range(1, n + 1))
        curr_sum = 0
        for i in range(1, n + 1):
            curr_sum += i
            if(curr_sum > tot - curr_sum + i):
                break
            
            if(curr_sum == tot - curr_sum + i):
                return i
            
        return -1
            