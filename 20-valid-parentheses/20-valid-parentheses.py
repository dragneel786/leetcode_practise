from queue import LifoQueue
class Solution:
    def isValid(self, s: str) -> bool:
        stack = LifoQueue()
        for i in s:
            if(i == "(" or i == "[" or i == "{"):
                stack.put(i)
            else:
                if(stack.empty()):
                    return False
                
                top = stack.get()
                if(top == "(" and i != ")"):
                    return False

                if(top == "{" and i != "}"):
                    return False

                if(top == "[" and i != "]"):
                    return False

        return True if(stack.empty()) else False