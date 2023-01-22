class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def part_it(start = 0, parts = []):
            if(start >= len(s)):
                ans.append([''.join(ss) for ss in parts])
                return
            
            temp = []
            for i in range(start, len(s)):
                temp.append(s[i])
                if(temp == temp[::-1]):
                    part_it(i + 1, parts + [temp])
        
        
        ans = []
        part_it()
        return ans
        
                