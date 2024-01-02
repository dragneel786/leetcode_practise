class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        num_counter = Counter(nums)
        res = []
        while(num_counter):
            curr = []
            for k in list(num_counter.keys()):
                curr.append(k)
                num_counter[k] -= 1
                if(not num_counter[k]):
                    del num_counter[k]
            
            res.append(curr)
    
        return res
                
        
        
                