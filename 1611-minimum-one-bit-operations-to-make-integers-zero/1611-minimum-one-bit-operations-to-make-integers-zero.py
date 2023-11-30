class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        fun = [0] * 31
        fun[0] = 1
        for i in range(1, 31):
            fun[i] = fun[i - 1] * 2 + 1
        
        ans = 0
        add = True
        for i in range(30, -1, -1):
            is_bit_set = (1 << i) & n
            
            if(is_bit_set):
                
                if(add):
                    ans += fun[i]
                else:
                    ans -= fun[i]
                
                add = not add
        
        return ans
            
            