class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        hmap = defaultdict(lambda:math.inf)
        hmap[0] = -1
        sums = 0
        for i in range(n):
            sums += arr[i]
            hmap[sums] = i

        sums = 0
        lsize, ans = n + 1, n + 1
        for i in range(n):
            sums += arr[i]
            if(hmap[sums - target] != math.inf):
                lsize = min(lsize, i - hmap[sums - target])

            if(hmap[sums + target] != math.inf and lsize < n + 1):
                ans = min(ans, lsize + (hmap[sums + target] - i))

        return ans if(ans < n + 1) else -1
        