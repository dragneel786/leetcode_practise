from sortedcontainers import SortedList
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        def find(sums, k):
            nonlocal cols
            temp_res = -inf
            prefix_sum = 0
            prefix_list = [inf]

            for s in sums:
                insort(prefix_list, prefix_sum)
                prefix_sum += s
                idx = bisect_left(prefix_list, prefix_sum - k)
                temp_res = max(temp_res, prefix_sum - prefix_list[idx])
                prefix_list.append(prefix_sum)

            return temp_res


        rows, cols = len(matrix), len(matrix[0])
        for r in range(rows):
            for c in range(cols - 1):
                matrix[r][c + 1] += matrix[r][c]

        res = -inf
        for i in range(cols):
            for c in range(i, cols):
                sums = [matrix[r][c] - (matrix[r][i - 1]\
                                        if(i > 0) else 0) for r in range(rows)]
                res = max(res, find(sums, k))

        return res

