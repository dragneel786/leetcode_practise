class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        c = defaultdict(lambda:0)
        for a in arr:
            c[a] += 1

        count = 0
        for i in range(101):
            for j in range(i, 101):
                k = target - i - j
                if(k < 0 or k > 100): continue
                if(i == j and j == k):
                    count += c[i] * (c[i] - 1) * (c[i] - 2) // 6
                if(i == j and j != k):
                    count += (c[i] * (c[i] - 1) // 2) * c[k]
                elif(j < k):
                    count += c[i] * c[j] * c[k]

        return count % (pow(10, 9) + 7)
            