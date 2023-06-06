class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        v = arr[1] - arr[0]
        for i in range(1, len(arr) - 1):
            if(arr[i] + v != arr[i + 1]):
                return False
        
        return True
    