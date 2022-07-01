class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def encode(w):
            w += "-"
            res = []
            count = 1
            for i in range(1, len(w)):
                if(w[i] != w[i - 1]):
                    res.append((w[i - 1], count))
                    count = 1
                else:
                    count += 1
            return res
        
        def compare(w1, w2):
            for i in range(len(w1)):
                a, b = w1[i], w2[i]
                if(a[0] == b[0] and (a[1] == b[1] or\
                                     (a[1] > b[1] and a[1] > 2))):
                    continue
                return False
            return True
        
        s = encode(s)
        ans = 0
        for wo in words:
            v = encode(wo)
            if(len(v) == len(s) and compare(s, v)):
                ans += 1
        return ans
                
                