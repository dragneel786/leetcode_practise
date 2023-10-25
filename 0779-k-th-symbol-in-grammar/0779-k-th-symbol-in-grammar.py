class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        ladder = [k]
        while(k > 1):
            k = (k + 1) // 2
            ladder.append(k)
        
        
        curr = '0'
        t = {'0': '01', '1':'10'}
        for l in reversed(ladder):
            curr = t[curr][(l - 1) % 2]
        
        return int(curr)
            