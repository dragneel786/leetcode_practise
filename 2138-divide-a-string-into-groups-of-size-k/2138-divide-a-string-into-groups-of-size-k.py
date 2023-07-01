class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        ans = []
        n = len(s)
        for i in range(0, len(s), k):
            news = s[i: i + k]
            sz = len(news)
            if(sz < k):
                news += (fill * (k - sz))
            
            ans.append(news)
        
        return ans
                