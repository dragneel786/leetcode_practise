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
            search_res = []
            for c in bnum:
                cv = rev[c]
                if(cv in temp):
                    search_res.append('1')
                    temp = temp[cv]
                else:
                    search_res.append('0')
                    temp = temp[c]
            
            return int(''.join(search_res), 2)
                    
                
        rep = []
        trie = create_trie()
        max_res = 0
        for r in rep:
            val = search(r)
            if(val > max_res):
                max_res = val
        
        return max_res