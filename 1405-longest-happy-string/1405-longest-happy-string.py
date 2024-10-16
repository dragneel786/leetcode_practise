class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = [(-a, 'a'), (-b, 'b'), (-c, 'c')]
        heapify(heap)
        res = []
        while(heap):
            count, ch = heappop(heap)
            count *= -1
            if len(res) < 2 or not (res[-1] == res[-2] == ch):
                if count - 1 >= 0:
                    res.append(ch)
                    heappush(heap, (-(count - 1), ch))
            
            elif len(heap) > 0:
                count2, ch2 = heappop(heap)
                count2 *= -1
                if count2 - 1 >= 0:
                    res.append(ch2)
                    heappush(heap, (-(count2 - 1), ch2))
                heappush(heap, (-(count), ch))
            
            else:
                break
                
            
            
            # print(heap, res)
        
        
        return ''.join(res)