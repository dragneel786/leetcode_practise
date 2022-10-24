class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        def get_new_mask(idx, mask):
            new_mask = mask
            for c in arr[idx]:
                bit_on = 1 << (ord(c) - 97)
                if(new_mask & bit_on):
                    return 0
                new_mask |= bit_on
            
            return new_mask
        
        
        def bit_len(val):
            count = 0
            while(val):
                val &= (val - 1)
                count += 1
            return count
    
                
        def find_max_len(idx = 0, mask = 0):
            slen = bit_len(mask)
            if(idx == len(arr)\
               or slen == 26):
                return slen
            
            
            new_mask = get_new_mask(idx, mask)
            ret = 0
            
            if(new_mask):
                ret = find_max_len(idx + 1, new_mask)
                
            ret = max(ret, find_max_len(idx + 1, mask))
            
            return ret
            
        
        return find_max_len()
        