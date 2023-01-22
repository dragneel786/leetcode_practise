class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def part_it(start = 0, parts = []):
            if(start >= len(s)):
                ans.append(parts)
                return
            
            for end in range(start + 1, len(s) + 1):
                substr = s[start: end]
                if(substr == substr[::-1]):
                    part_it(end, parts + [substr])
        
        
        ans = []
        part_it()
        return ans
        
                