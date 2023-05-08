class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        
        def elements(num = 0, picked = set()):
            if(num >= 100):
                if(num % 2 == 0):
                    ans.add(num)
                return
            
            for i in range(len(digits)):
                if(i not in picked):
                    if(digits[i] or (not digits[i] and num)):
                        picked.add(i)
                        elements(num * 10 + digits[i])
                        picked.remove(i)
            
        
        ans = set()
        elements(0)
        return sorted(ans)