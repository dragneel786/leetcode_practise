class Solution:
    def kthCharacter(self, k: int) -> str:
        stack = ['a']
        while(len(stack) < k):
            for c in stack[:]:
                next_char = chr(ord(c) + 1)
                if c == 'z':
                    next_char = 'a'
                
                stack.append(next_char)
        
        return stack[k - 1]
