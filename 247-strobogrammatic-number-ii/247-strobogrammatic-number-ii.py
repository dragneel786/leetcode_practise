class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        combos = {'0':'0', '1':'1', '8':'8', '6':'9', '9': '6'}
        final_length = n
        
        def create_storo(n):
            nonlocal final_length
            if(not n):
                return ['']
            
            if(n == 1):
                return ['0', '1', '8']
            
            prev_combo = create_storo(n - 2)
            curr_combo = []
            
            for p in prev_combo:
                for i, j in combos.items():
                    if(i != '0' or n != final_length):
                        curr_combo.append(i + p + j)
            
            return curr_combo
        
        return create_storo(n)