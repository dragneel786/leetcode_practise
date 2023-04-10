class Solution:
    def isValid(self, s: str) -> bool:
        pmap = {"(":")","{":"}","[":"]"}
        stack = deque()
        for c in s:
            if(c == '(' or c == "{" or c == "["):
                stack.append(c)
                continue
            
            ele = stack.pop() if(stack) else "*"
            if(pmap.get(ele, "*") != c):
                return False
            
        
        return len(stack) == 0
    