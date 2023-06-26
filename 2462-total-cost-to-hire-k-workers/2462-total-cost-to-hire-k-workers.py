class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        heap = []
        n = len(costs)
        # print(n, )
        for i in range(min(candidates, ceil(n/2))):
            heap.append([costs[i], i, 0])
            if(i == n - i - 1):
                break
            heap.append([costs[n - i - 1], n - i - 1, 1])
            
            
        heapify(heap)
        i = candidates
        j = n - candidates - 1
        tot = 0
        for _ in range(k):
            cost, idx, back = heappop(heap)
            tot += cost
            if(back and j >= i):
                heappush(heap, [costs[j], j, 1])
                j -= 1
            
            elif(i < j):
                heappush(heap,[costs[i], i, 0])
                i += 1
            # print(cost, heap)
        return tot
                
                
        