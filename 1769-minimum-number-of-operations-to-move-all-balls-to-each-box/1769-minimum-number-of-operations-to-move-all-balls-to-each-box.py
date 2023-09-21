class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        ans = [0] * n
        for i in range(n):
            
            for j in range(i - 1, -1, -1):
                if(boxes[j] == '1'):
                    ans[i] += abs(i - j)
            
            for j in range(i + 1, n):
                if(boxes[j] == '1'):
                    ans[i] += abs(i - j)
        
        return ans
            
            
            