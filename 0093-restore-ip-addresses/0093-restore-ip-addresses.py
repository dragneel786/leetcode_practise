class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        def construct_ips(i, curr_val = '', ip = []):
            if((curr_val and int(curr_val) > 255)\
               or len(ip) > 3):
                return 
            
            if(i >= len(s)):
                if(curr_val and len(ip) == 3):
                    ip.append(curr_val)
                    ans.append('.'.join(ip))
                return
            
            if(curr_val != '0'):
                construct_ips(i + 1, curr_val + s[i], ip)
            
            if(curr_val):
                construct_ips(i + 1, s[i], ip + [curr_val])
            
            
        
        ans = []
        construct_ips(0)
        return ans
                
                
            