class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums_counts = Counter(nums)
        sorted_keys = sorted(nums_counts.keys(), reverse=True)
        operations = 0
        for i in range(1, len(sorted_keys)):
            operations += nums_counts[sorted_keys[i - 1]]
            nums_counts[sorted_keys[i]] += nums_counts[sorted_keys[i - 1]]
        
        return operations
            