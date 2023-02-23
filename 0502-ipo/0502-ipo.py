class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        
        min_cap_heap = [(c, i) for i, c in enumerate(capital)]
        max_pro_heap = []
        heapify(min_cap_heap)
        
        curr_cap = w
        for _ in range(k):
            while(min_cap_heap and min_cap_heap[0][0] <= curr_cap):
                _, i = heappop(min_cap_heap)
                heappush(max_pro_heap, -profits[i])
            
            if(not max_pro_heap):
                break
            
            pro = -heappop(max_pro_heap)
            curr_cap += pro
        return curr_cap
            
                
        