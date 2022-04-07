class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapify(stones)
        while(len(stones) > 1):
            val1 = -heappop(stones)
            val2 = -heappop(stones)
            heappush(stones, -(val1 - val2))

        return -stones[0]