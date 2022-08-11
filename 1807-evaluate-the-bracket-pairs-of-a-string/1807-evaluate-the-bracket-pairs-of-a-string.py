class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        
        def create_knowledge_map(knowledge):
            mapped = defaultdict(lambda:'?', {key:value for key, value in knowledge})
            return mapped
        
        kmap = create_knowledge_map(knowledge)
        is_open = False
        res = temp = ""
        for c in s:
            if(c == '('): is_open = True
                
            elif(c == ')'):
                is_open = False
                res += kmap[temp]
                temp = ""
                
            elif(is_open): temp += c
                
            else: res += c
        return res
            
        