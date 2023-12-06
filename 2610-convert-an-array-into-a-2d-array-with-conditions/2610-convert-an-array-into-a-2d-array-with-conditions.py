class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        num_counts = Counter(nums)
        ans = []
        while(num_counts):
            li = []
            for k in list(num_counts.keys()):
                li.append(k)
                num_counts[k] -= 1
                if(num_counts[k] == 0):
                    del num_counts[k]
            
            ans.append(li)
            
        return ans
                