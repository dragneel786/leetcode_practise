class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        
        def score(val):
            nonlocal n
            ones = 0
            while(val):
                ones += (val & 1)
                val >>= 1
            return n - ones
        
        def bit_mapped(values):
            temp = []
            for bits in values:
                val = 0
                for b in bits:
                    val = (val << 1) + b
                
                temp.append(val)
            
            return temp
        
        @lru_cache(None)
        def pick(stu_mask, men_mask, choosed):
            nonlocal m
            if(choosed == m):
                return 0
            
            ret = 0
            for i, st in enumerate(students):
                if((1 << i) & stu_mask):
                    continue
                    
                for j, mt in enumerate(mentors):
                    if((1 << j) & men_mask):
                        continue
                    
                    ret = max(ret, score(st ^ mt)\
                               + pick((1 << i) | stu_mask,\
                                      (1 << j) | men_mask, \
                                      choosed + 1))
            return ret
                                           
        m, n = len(students), len(students[0])
        students = bit_mapped(students)[:]
        mentors = bit_mapped(mentors)[:]
        return pick(0, 0, 0)
        
        