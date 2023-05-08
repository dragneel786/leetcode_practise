class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        
        n = len(digits)
        ans = set()
        for i in range(n):
            if(digits[i] == 0):
                continue
                
            for j in range(n):
                if(i == j):
                    continue
                    
                for k in range(n):
                    if(k == i or k == j\
                       or digits[k] % 2 != 0):
                        continue
                        
                    ans.add(digits[i] * 100\
                            + digits[j] * 10\
                            + digits[k])

        return sorted(ans)
        