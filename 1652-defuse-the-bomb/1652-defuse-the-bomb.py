class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        
        n = len(code)
        ans = [0] * n
        if(k > 0):
            tot = sum(code[1:k + 1])
            for i in range(1, n):
                ans[i - 1] = tot
                idx = (k + i) % n
                tot += (code[idx] - code[i])
            ans[-1] = tot
        
        elif(k < 0):
            tot = sum(code[k:])
            sub = n + k - 1
            for i in range(1, n):
                ans[i - 1] = tot
                idx = (sub + i) % n
                tot += (-code[idx] + code[i - 1])
            ans[-1] = tot
        
        return ans
                
        
            
    