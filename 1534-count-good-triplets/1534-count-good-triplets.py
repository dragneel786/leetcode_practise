class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        n = len(arr)
        check = lambda iv, jv, kv: abs(iv - jv) <= a\
        and abs(jv - kv) <= b and abs(iv - kv) <= c
        return sum([check(arr[i], arr[j], arr[k]) for i in range(n)\
                    for j in range(i + 1, n) for k in range(j + 1, n)])