class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        freq_map = Counter(nums)
        hypo_map = Counter()
        
        for num in nums:
            if(freq_map[num]):
                if(hypo_map[num]):
                    hypo_map[num] -= 1
                    hypo_map[num + 1] += 1
                    
                elif(freq_map[num + 1] and freq_map[num + 2]):
                    freq_map[num + 1] -= 1
                    freq_map[num + 2] -= 1
                    
                    hypo_map[num + 3] += 1
                
                else:
                    return False
                
                freq_map[num] -= 1
                    
        return True
                    
                