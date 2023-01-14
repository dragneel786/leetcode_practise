class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff = inf
        ans = []
        for i in range(1, len(arr)):
            diff = abs(arr[i - 1] - arr[i])
            if(min_diff > diff):
                ans = [[arr[i - 1], arr[i]]]
                min_diff = diff
            
            elif(min_diff == diff):
                ans.append([arr[i - 1], arr[i]])
            
        return ans 
            