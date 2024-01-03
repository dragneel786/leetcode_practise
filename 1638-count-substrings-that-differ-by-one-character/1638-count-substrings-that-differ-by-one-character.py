class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        
        def create_trie(string):
            trie = {}
            n = len(string)
            for i in range(n):
                for j in range(i, n):
                    temp = trie
                    for c in string[i:j + 1]:
                        temp[c] = temp.get(c, {})
                        temp = temp[c]
                    
                    temp['$'] = temp.get('$', 0) + 1
                    
            return trie
        
        
        def find(string, temp):
            for c in string:
                if(c not in temp):
                    return 0
                
                temp = temp[c]
            
            return temp.get("$", 0)
            
            
        def change_and_check(string, temp):
            counts = 0
            for i in range(len(string)):
                char = string[i]
                for k in temp.keys():
                    if(char == k):
                        continue
                        
                    string[i] = k
                    counts += find(string, temp)
                    
                
                string[i] = char
            
            return counts
                        
            
        trie = create_trie(t)
        n = len(s)
        ans = 0
        for i in range(n):
            for j in range(i, n):
                ans += change_and_check(list(s[i:j + 1]), trie)
        
        return ans
        
            
            
            
            
            
            
            
        
        
        
        