class Solution:
    def smallestNumber(self, num: int) -> int:
        def great_it(val):
            heap = []
            while(val):
                heap.append(val % 10)
                val //= 10
                print(val)

            res = 0
            for v in sorted(heap, reverse=True):
                res = (res * 10) + v 

            return -1 * res

        def lower_it(val):
            heap = []
            zeros = 0
            while(val):
                rem = val % 10
                if rem == 0:
                    zeros += 1

                else:
                    heap.append(rem)

                val //= 10

            res = 0
            heapify(heap)
            if heap:
                res = heappop(heap)
                for _ in range(zeros):
                    res = (res * 10)

            while(heap):
                res = (res * 10) + heappop(heap)

            return res



        if num < 0:
            return great_it(abs(num))
        else:
            return lower_it(num)