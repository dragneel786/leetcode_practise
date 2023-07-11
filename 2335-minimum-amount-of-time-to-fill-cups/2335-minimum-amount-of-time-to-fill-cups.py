class Solution:
    def fillCups(self, A: List[int]) -> int:
        return max(max(A), (sum(A) + 1) // 2)
#         heapify(amount)
#         ans = 0
#         while(len(amount) > 1):
#             print(amount)
#             a, b = heappop(amount), heappop(amount)
#             if(a != 1):
#                 heappush(amount, a - 1)
            
#             if(b != 1):
#                 heappush(amount, b - 1)
            
#             ans += 1
#             print(amount)
#         return ans + heappop(amount)