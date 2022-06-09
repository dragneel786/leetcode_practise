class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        i = 0
        j = n - 1
        while(i < j):
            val = numbers[i] + numbers[j]
            if(val == target):
                return [i + 1, j + 1]
            
            if(val > target):
                j -= 1
            else:
                i += 1
        
            
            