class Solution:
    def differByOne(self, dict: List[str]) -> bool:
        for i in range(len(dict[0])):
            seen = set()
            for w in dict:
                s = w[:i] + "_" + w[i + 1:]
                if(s in seen):
                    return True
                seen.add(s)
        return False