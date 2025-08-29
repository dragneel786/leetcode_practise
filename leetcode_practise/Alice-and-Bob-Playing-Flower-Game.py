class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        return (n * (m // 2)) + ((n // 2) * ((m % 2) == 1))
        # res = 0
        # for i in range(1, n + 1):
        #     res += m // 2
        #     if i % 2 == 0:
        #         res += (m % 2) == 1

        # return res

    # 1, 2, 3, 4, 5
    # n = 5, (n // 2)
