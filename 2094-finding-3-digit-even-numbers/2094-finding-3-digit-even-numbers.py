class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        
        n = len(digits)
        ans = set()
        for i in range(n):
            if(digits[i] != 0):
                for j in range(n):
                    if(i != j):
                        for k in range(n):
                            if(k != i and k != j\
                               and digits[k] % 2 == 0):
                                ans.add(digits[i] * 100\
                                        + digits[j] * 10\
                                        + digits[k])
        
#         def elements(num = 0, picked = set()):
#             if(num >= 100):
# [1,8,7,7,1,1,5,4,0,0,7,5,1,7,9]
#                 if(num % 2 == 0):
#                     ans.add(num)
#                 return
            
#             for i in range(len(digits)):
#                 if(i not in picked):
#                     if(digits[i] or (not digits[i] and num)):
#                         picked.add(i)
#                         elements(num * 10 + digits[i])
#                         picked.remove(i)
            
        
#         ans = set()
#         elements(0)
        return sorted(ans)
        