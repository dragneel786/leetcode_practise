class Solution:
    def isPossible(self, target: List[int]) -> bool:
        # use target as heap
        # add all elements to heap and find sum.
        # val = (maxElement - (sum - maxElement)) and push into the queue
        # update sum with sum + val
        # do this while the first element is not equal 1 else return false
        if(len(target) == 1):
            return target[0] == 1
        heap = []
        sums = 0
        for t in target:
            heap.append(-t)
            sums += t
        
        heapify(heap)
        while(-heap[0] > 1):
            top = -heappop(heap)
            if(sums - top == 1):
                val = top - (top - 1)
            else:
                val = top % (sums - top)
            if(not val or val == top):
                return False
            sums += val - top
            heappush(heap, -val)
        return True