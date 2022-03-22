def lengthOfLongestSubstring(s: str) -> int:
    lookup = dict()
    first = 0
    leng, maxLen = 0, 0
    n = len(s)
    # print(s[0])
    for i in range(n):
        if s[i] not in lookup or lookup[s[i]] == 0:
            lookup[s[i]] = 1
            leng += 1
            continue
        
        maxLen = max(maxLen, leng)
        while(s[first] != s[i]):
            lookup[s[first]] -= 1
            first += 1
            leng -= 1
        # print("leng = ",leng)
        first += 1   
    
    return max(maxLen, leng)





print(lengthOfLongestSubstring(""))