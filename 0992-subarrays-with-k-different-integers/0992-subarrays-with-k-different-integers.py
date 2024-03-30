class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        def find_sub(arr, size):
            counts = Counter()
            ans = start = 0
            for end in range(len(arr)):
                counts[arr[end]] += 1
                while(len(counts) > size):
                    counts[arr[start]] -= 1
                    if(counts[arr[start]] == 0):
                        del counts[arr[start]]
                    start += 1
                
                ans += end - start + 1
            
            return ans
        
        
        return find_sub(nums, k) - find_sub(nums, k - 1)
                
                
                
            