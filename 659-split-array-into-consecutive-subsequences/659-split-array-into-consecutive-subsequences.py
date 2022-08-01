class Node:
    def __init__(self, start = -1, end = -1):
        self.start = start
        self.end = end
        
    def __lt__(self, other):
        return other.end > self.end or\
    (other.end == self.end and (other.end - other.start + 1)\
     > (self.end - self.start + 1))
        


class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        heap = []
        # print(heap[0].start, heap[0].end)
        for n in nums:
            while(heap and heap[0].end + 1 < n):
                node = heappop(heap)
                start, end = node.start, node.end
                if((end - start + 1) < 3): return False
            
            if(not heap or heap[0].end == n):
                heappush(heap, Node(n, n))
            elif(heap[0].end + 1 == n):
                node = heappop(heap)
                heappush(heap, Node(node.start, n))
        
        for h in heap:
            if((h.end - h.start + 1) < 3):
                return False
        return True
            
                
            
            
            
                