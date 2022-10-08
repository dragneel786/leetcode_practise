class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        reverse = {'0':'0', '1':'1', '8':'8',\
                   '9':'6', '6':'9'}
        
        def gen_strob(l):
            nonlocal n
            if(not l):
                return ['']
            
            if(l == 1):
                return ['0', '1', '8']
            
            ret = []
            
            for num in gen_strob(l - 2):
                for k, v in reverse.items():
                    if(l == n and k == '0'):
                        continue
                    
                    new_num = k + num + v
                    ret.append(new_num)
            
            return ret
    
        return gen_strob(n)