class Solution:
    def dailyTemperatures(self, tempt: List[int]) -> List[int]:
        mst = deque()
        ans = [0] * len(tempt)
        for i, t in enumerate(tempt):
            while(mst and mst[-1][0] < t):
                _, j = mst.pop()
                ans[j] = (i - j)
            
            mst.append((t, i))
        
        return ans
        
                
                