class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        n = len(arr)
        low = 0
        high = n - 1
        
        while(low <= high):
            mid = ((high - low) >> 1) + low
            print(mid)
            if(arr[mid - 1] < arr[mid] > arr[mid + 1]):
                return mid
            
            if(arr[mid - 1] < arr[mid] < arr[mid + 1]):
                low = mid + 1
            else:
                high = mid - 1
            
        
        return low + 1
            