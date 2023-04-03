class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        
        
        heap = [(-a, 'a'), (-b, 'b'), (-c, 'c')]
        heapify(heap)
        ans = []
        while(heap):
            aco, ach = heappop(heap)
            if(aco and (len(ans) < 2 or ans[-2] + ans[-1] + ach != (ach * 3))):
                aco += 1
                ans.append(ach)
            elif(len(heap)):

                bco, bch = heappop(heap)
                if(bco and (len(ans) < 2 or ans[-2] + ans[-1] + bch != (bch * 3))):
                    bco += 1
                    ans.append(bch)
                    heappush(heap, (bco, bch))
            else:
                break


            if(aco):
                heappush(heap, (aco, ach))


        return ''.join(ans)
