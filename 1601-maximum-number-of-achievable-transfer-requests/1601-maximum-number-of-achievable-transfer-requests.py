class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        
        
        def backtrack(i, count = 0):
            if(i >= len(requests)):
                if(any(values)):
                    return -inf
                return count
            
            a, b = requests[i]
            
            values[a] -= 1
            values[b] += 1
            ret = backtrack(i + 1, count + 1)
            values[a] += 1
            values[b] -= 1
            ret = max(ret, backtrack(i + 1, count))
            return ret
        
        values = [0] * n
        return backtrack(0)