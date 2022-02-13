class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
    
        def getSubset(inp, op = []):
            if(not inp):
                res.append(op)
                return

            getSubset(inp[1:], op)
            getSubset(inp[1:], op + [inp[0]])
            
        
        getSubset(nums)
        return res