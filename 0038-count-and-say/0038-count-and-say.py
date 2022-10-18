class Solution:
    def countAndSay(self, n: int) -> str:
        
        ans = "1-"
        for _ in range(n - 1):
            count = 1
            ret = ""
            
            for i in range(1, len(ans)):
                if(ans[i - 1] != ans[i]):
                    ret += (str(count) + ans[i - 1])
                    count = 0
                count += 1
                
            ans = ret + '-'
            
        return ans[:-1]
            