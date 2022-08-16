# class Node:
#     def __init__(self, num = ""):
#         self.num = num
#         self.size = len(num)
        
#     def __lt__(self, other):
#         return self.size < other.size or \
#     (self.size == other.size and self.compare_two(self.num, other.num))
    
#     def compare_two(self, num1, num2):
#         for s1, s2 in zip(num1, num2):
#             v1, v2 = int(s1), int(s2)
#             if(v1 == v2): continue
                
#             if(v1 < v2):
#                 return True
#             else:
#                 return False
            
#         return False
    
class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        return str(nlargest(k, [int(num) for num in nums])[-1])
        