class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        
#         def get_min_moves(se, st):
#             if(sum(se.values()) == 0):
#                 return 0
            
#             val = inf
#             for a in se:
#                 for b in st:
#                     if(se[a] and st[b]):
#                         se[a] -= 1
#                         st[b] -= 1
#                         val = min(val, abs(a - b) +\
#                                  get_min_moves(se, st))

#                         se[a] += 1
#                         st[b] += 1
                    
#             return val
        
#         return get_min_moves(Counter(seats), Counter(students))
        
        seats.sort()
        students.sort()
        return sum([abs(a - b) for a, b in zip(seats, students)])