class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        counts = Counter(s)
        heap = []
        for k, v in counts.items():
            heappush(heap, (-ord(k), v))

        res = []
        while(len(heap) > 0):
            k, v = heappop(heap)

            k *= -1
            for _ in range(min(v, repeatLimit)):
                res.append(chr(k))

            if v > repeatLimit:
                if len(heap) == 0:
                    break

                tk, tv = heappop(heap)
                res.append(chr(tk * -1))
                if tv - 1 > 0:
                    heappush(heap, (tk, tv - 1))

                heappush(heap, (-k, v - repeatLimit))


        return "".join(res)