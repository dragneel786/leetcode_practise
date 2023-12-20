class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        
        def hashy(w):
            e = [0] * 26
            o = [0] * 26
            for i in range(len(w)):
                idx = ord(w[i]) - 97
                if(i % 2):
                    o[idx] += 1
                else:
                    e[idx] += 1
            
            es = ''.join(map(str, e))
            os = ''.join(map(str, o))
            return es + '|' + os
        
        g = Counter()
        for w in words:
            ha = hashy(w)
            g[ha] += 1
        
        return len(g)
                
            
                
                
                    