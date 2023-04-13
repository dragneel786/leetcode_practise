class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = deque()
        j = 0
        for pus in pushed:
            stack.append(pus)
            while(stack and stack[-1] == popped[j]):
                stack.pop()
                j += 1
            
        return j == len(popped)
            