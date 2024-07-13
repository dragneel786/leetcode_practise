class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        robot_spec = [(p, i, h, d) for i, (p, h, d) in enumerate(zip(positions, healths, directions))]
        robot_spec.sort()
        
        left_stack = deque()
        res = [0] * len(positions)
        for p, i, h, d in robot_spec:
            if d == 'L':
                while left_stack and left_stack[-1][2] < h:
                    left_stack.pop()
                    h -= 1
                
                if len(left_stack) == 0:
                    res[i] = h
                
                else:
                    if left_stack[-1][2] == h:
                        left_stack.pop()

                    else:
                        left_stack[-1][2] -= 1
            
            else:
                left_stack.append([i, p, h])
        
        while left_stack:
            i, p, h = left_stack.pop()
            res[i] = h
        
        return [r for r in res if r]
            
            
        