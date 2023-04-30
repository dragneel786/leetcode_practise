class Solution:
    def minMaxDifference(self, num: int) -> int:
        min_digit = -1
        max_digit = -1
        max_val = 0
        min_val = 0
        for v in str(num):
            v = int(v)
            max_val *= 10
            
            if(v != 9 and \
               (v == max_digit or max_digit == -1)):
                max_digit = v
                max_val += 9
            else:
                max_val += v
        
            min_val *= 10
            if(v != 0 and\
              (v == min_digit or min_digit == -1)):
                min_digit = v
                min_val += 0
            else:
                min_val += v
            
        return max_val - min_val
    
            
                