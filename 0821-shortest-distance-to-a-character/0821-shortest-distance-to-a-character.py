class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        answer = [10002] * len(s)
        occur = 10002
        for i, a in enumerate(s):
            if(a == c):
                occur = 0
            
            answer[i] = occur
            occur += 1
        
        for i in range(len(s) - 1, -1, -1):
            if(not answer[i]):
                occur = 0
            
            answer[i] = min(answer[i], occur)
            occur += 1
        
        return answer
        
        