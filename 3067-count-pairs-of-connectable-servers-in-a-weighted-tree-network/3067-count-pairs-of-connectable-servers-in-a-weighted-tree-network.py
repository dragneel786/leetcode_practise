from typing import List

class Solution:
    def __init__(self):
        self.adj = None
        self.mod = 0

    def dfs(self, par, n, s):
        ans = 0
        if s % self.mod == 0:
            ans += 1
        for i in self.adj[n]:
            if i[0] == par:
                continue
            ans += self.dfs(n, i[0], s + i[1])
        return ans

    def cal(self, n):
        prev = 0
        ans = 0
        for i in self.adj[n]:
            k = self.dfs(n, i[0], i[1])
            ans += prev * k
            prev += k
        return ans

    def countPairsOfConnectableServers(self, v: List[List[int]], k: int) -> List[int]:
        n = len(v)
        self.adj = [[] for _ in range(n + 1)]

        for edge in v:
            self.adj[edge[0]].append([edge[1], edge[2]])
            self.adj[edge[1]].append([edge[0], edge[2]])

        self.mod = k
        ans = []
        for i in range(n + 1):
            m = len(self.adj[i])
            s = self.cal(i)
            ans.append(s)

        return ans