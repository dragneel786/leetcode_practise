class Solution:
    def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:
        s_split = Counter()
        t_split = Counter()
        split = len(s) // k
        for i in range(0, len(s), split):
            s_split[s[i: i + split]] += 1
            t_split[t[i: i + split]] += 1

        print(s_split, t_split)
        for key, val in s_split.items():
            if val != t_split[key]:
                return False

        return True

 


 