class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def create_bits_key(word):
            imap = [0] * 26
            for c in word:
                imap[ord(c) - 97] += 1
            print(imap)
            return "|".join(map(str, imap))
        
        
        vmap = dict()
        for word in strs:
            key = create_bits_key(word)
            print(key)
            vmap[key] = vmap.get(key, [])
            vmap[key].append(word)
        
        return vmap.values()
            