class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if(not arr):
            return []
        li = [(a, i) for i,a in enumerate(arr)]
        li.sort(key=lambda x:x[0])
        arr[li[0][1]] = 1
        for i in range(1, len(li)):
            r = arr[li[i - 1][1]]
            if(li[i][0] > li[i - 1][0]):
                r += 1
            arr[li[i][1]] = r
        return arr
            
            
        