class Solution:
    def reorganizeString(self, s: str) -> str:
        C = Counter(s)
        
        heap = [(-C[key], key) for key in C.keys()] #a:2, b:2, c:4
        heapify(heap)
        
        res = ""
        while(heap):
            count1, ch1 = heappop(heap)
            count1 *= -1
            res += ch1
            
            if(not heap):
                if(count1 > 1):
                    return ""
            else:
                count2, ch2 = heappop(heap)
                count2 *= -1
                res += ch2
                
                if(count1 > 1):
                    heappush(heap, (-(count1 - 1), ch1))
                if(count2 > 1):
                    heappush(heap, (-(count2 - 1), ch2))
        
        return res
                
            
            