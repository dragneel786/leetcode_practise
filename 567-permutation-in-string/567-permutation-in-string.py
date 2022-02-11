class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        lookup = [0] * 26
        for i in s1:
            lookup[ord(i) - 97] += 1
        len_s1 = len(s1)
        
        def check(freq):
            for i in freq:
                if i > 0:
                    return False
            return True
        
        for i in range(len(s2) - len_s1 + 1):
            if(lookup[ord(s2[i]) - 97]):
                temp = lookup[:]
                j = i
                while(j - i < len_s1):
                    temp[ord(s2[j]) - 97] -= 1
                    j += 1

                if(check(temp)):
                    return True

        return False