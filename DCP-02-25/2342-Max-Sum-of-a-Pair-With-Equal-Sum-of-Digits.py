class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        indexs = defaultdict(list)
        for i, num in enumerate(nums):
            temp, tot = num, 0
            while(temp):
                tot += (temp % 10)
                temp //= 10

            indexs[tot].append(num)
        
        max_val = -1
        for vals in indexs.values():
            if len(vals) > 1:
                vals.sort()
                max_val = max(max_val, vals[-1] + vals[-2])
        
        return max_val


            

        
