class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        
        def construct_trie():
            t = dict()
            for num in arr2:
                num_str = str(num)
                temp = t
                for c in num_str:
                    temp.setdefault(c, {})
                    temp = temp[c]
        
            return t
        
        def query(num_str):
            nonlocal trie
            temp = trie
            size = 0
            for c in num_str:
                if c not in temp:
                    break
                
                temp = temp[c]
                size += 1
        
            return size
        
        trie = construct_trie()
        max_len = 0
        for num in arr1:
            max_len = max(max_len, query(str(num)))
        
        return max_len