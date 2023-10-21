class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = ""
        max_val = -1
        curr_val = ""
        for c in num:
            if(not curr_val or curr_val[-1] == c):
                curr_val += c
            else:
                curr_val = c
            
            if(len(curr_val) == 3 and int(curr_val) > max_val):
                res = curr_val
                max_val = int(res)
                curr_val = ""
        
        return res
            
        