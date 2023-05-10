class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        def create_trie():
            t = dict()
            for num in nums:
                bnum = bin(num)[2:]
                bnum = '0' * (32 - len(bnum)) + bnum
                rep.append(bnum)
                temp = t
                for c in bnum:
                    temp[c] = temp.get(c, {})
                    temp = temp[c]
                temp['$'] = None
            return t
        
        
        def search(bnum):
            temp = trie
            rev = {'0':'1', '1':'0'}
            res = 0
            for c in bnum:
                cv = rev[c]
                res <<= 1
                if(cv in temp):
                    res += 1 
                    c = cv
                temp = temp[c]
            return res
                    
                
        rep = []
        trie = create_trie()
        max_res = 0
        for r in rep:
            val = search(r)
            if(val > max_res):
                max_res = val
        
        return max_res