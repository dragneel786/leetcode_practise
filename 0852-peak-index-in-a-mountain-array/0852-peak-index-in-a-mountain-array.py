class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        low = 0
        high = n - 1
        while(low <= high):
            mid = ((high - low) // 2) + low
            
            if(arr[mid - 1] < arr[mid] > arr[mid + 1]):
                return mid
            
            elif(arr[mid - 1] > arr[mid] > arr[mid + 1]):
                high = mid - 1
            
            else:
                low = mid + 1
        