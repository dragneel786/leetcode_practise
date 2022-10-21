class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        num_map = {'1':'1', '0':'0', '6':'9',\
                   '9':'6', '8':'8'}
        stro_num = ''
        for c in num[::-1]:
            if(c not in num_map):
                return False
            
            stro_num += num_map[c]
        
        return stro_num == num
            