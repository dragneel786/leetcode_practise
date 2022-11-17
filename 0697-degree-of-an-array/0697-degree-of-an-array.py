class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        max_freq = 0
        subarr = len(nums)
        sublen = 0
        index_freq = dict()

        for i, num in enumerate(nums):
            index_freq.setdefault(num, [i, 0])
            index_freq[num][1] += 1

            max_freq = max(max_freq, index_freq[num][1])



            if(max_freq == index_freq[num][1]):
                lc = (i - index_freq[num][0] + 1)
                if(subarr > lc or sublen < max_freq):
                    subarr = lc
                    sublen = max_freq

        return subarr
