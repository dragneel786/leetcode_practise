class Solution:
    def confusingNumber(self, n: int) -> bool:
        if(not n):
            return False
        
        rnums = {'0':'0', '1':'1', '6':'9',\
                 '8':'8', '9':'6'}
        val = n
        rotated = ''
        while(val):
            tnum = str(val % 10)
            val //= 10
            if(tnum not in rnums):
                return False
            
            rotated += rnums[tnum]
        
        return int(rotated) != n