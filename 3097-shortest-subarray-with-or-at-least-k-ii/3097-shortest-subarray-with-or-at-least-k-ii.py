class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        
        def get_val():
            nonlocal bit_counts
            val = 0
            for i, b in enumerate(bit_counts):
                if b > 0:
                    val |= (1 << i)

            return val

        def pad_in(bnum, inc):
            bidx = 0
            while(bnum):
                if bnum & 1:
                    bit_counts[bidx] += inc

                bnum >>= 1
                bidx += 1


        start = 0
        bit_counts = [0] * 30
        min_size = inf
        for i, num in enumerate(nums):
            pad_in(num, 1)
            while(start <= i and get_val() >= k):
                pad_in(nums[start], -1)
                min_size = min(i - start + 1, min_size)
                start += 1


        return min_size if min_size != inf else -1
            
            
            
        
                