class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
        tot_cell = n * n
        tot_con = maxWeight // w
        return tot_cell if tot_cell < tot_con else tot_con