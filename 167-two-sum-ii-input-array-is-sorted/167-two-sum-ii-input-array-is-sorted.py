class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            low = i + 1
            high = len(numbers) - 1
            val = target - numbers[i]
            while(low <= high):
                mid = low + (high - low) // 2
                if(numbers[mid] == val):
                    return [i + 1, mid + 1]
                
                if(numbers[mid] > val):
                    high = mid - 1
                else:
                    low = mid + 1