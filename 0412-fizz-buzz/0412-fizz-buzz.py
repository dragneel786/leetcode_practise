class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        
        ans = []
        for i in range(1, n + 1):
            res = ''
            hit3, hit5 = (i % 3) == 0, (i % 5) == 0
            if(hit3):
                res += "Fizz"
            
            if(hit5):
                res += "Buzz"
            
            if(not hit3 and not hit5):
                res += str(i)
            
            ans.append(res)
        
        return ans