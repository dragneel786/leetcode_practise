class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        high = 2002
        low = 1
        n = len(arr)
        while(low <= high):
            mid = (low + (high - low) // 2)
            idx = bisect_right(arr, mid)
            if((idx == 0 or arr[idx - 1] != mid)\
               and mid - idx == k):
                return mid
            
            if(mid - idx >= k):
                high = mid - 1 - (arr[idx - 1] == mid - 1)
            else:
                low = mid + 1
        
        return low
    