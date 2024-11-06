class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        
        def bits_count(val):
            counts = 0
            while(val):
                counts += val & 1
                val >>= 1
            
            return counts
                
        
        values = []
        sets = bits_count(nums[0])
        count = 0
        for i, num in enumerate(nums + [(nums[-1] << 1) + 1]):
            curr_set = bits_count(num)
            if curr_set != sets:
                values.extend(sorted(nums[i - count: i]))
                sets = curr_set
                count = 0
            
            count += 1
        
        # print(values)
        for i in range(1, len(values)):
            if values[i - 1] > values[i]:
                return False
        
        return True
        
        
                
                
            