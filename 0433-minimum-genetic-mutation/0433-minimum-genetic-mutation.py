class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        
        def bfs(gene):
            gene_list = list(gene)
            for i, c in enumerate(gene_list):
                char_set = {'A', 'C', 'G', 'T'}
                char_set.remove(c)
                
                for newc in char_set:
                    gene_list[i] = newc
                    new_gene = "".join(gene_list)
                    if(new_gene in bank_set):
                        bank_set.remove(new_gene)
                        queue.append(new_gene)
                
                gene_list[i] = c
                        
        
        bank_set = set(bank)
        queue = deque([start])
        steps = 0
        
        while(queue):
            for _ in range(len(queue)):
                gene = queue.popleft()
                if(gene == end):
                    return steps
                
                bfs(gene)
            
            steps += 1
        
        return -1
                
            
        
        
        