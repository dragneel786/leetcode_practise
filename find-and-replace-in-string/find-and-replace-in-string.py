class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        
        op = {i : (s, t) for i, s, t in zip(indices, sources, targets)}
        for i in range(len(s) - 1, -1, -1):
            if(i in op):
                src, tar = op[i]
                if(s[i: i + len(src)] == src):
                    s = s[:i] + tar + s[i + len(src):]

        return s

            