class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        j = rounds[0]
        visited = [0 if(i != j) else 1 for i in range(n + 1)]
        ans = [j]
        maxv = 1
        for i in range(1, len(rounds)):
            while(j != rounds[i]):
                j = j % n + 1
                visited[j] += 1
            
                if(maxv < visited[j]):
                    ans = [j]
                    maxv = visited[j]
            
                elif(maxv == visited[j]):
                    ans.append(j)
        
        return sorted(ans)