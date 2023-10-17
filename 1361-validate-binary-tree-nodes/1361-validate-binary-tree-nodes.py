class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        
        parent = {i:-1 for i in range(-1, n)}
        for i, (l, r) in enumerate(zip(leftChild, rightChild)):
            if(l != -1 and parent[l] != -1):
                return False
            
            if(r != -1 and parent[r] != -1):
                return False
            
            parent[l] = i
            parent[r] = i
            
        
        root = -1
        for node in range(n):
            if(parent[node] == -1):
                if(root != -1):
                    return False
                
                root = node
            
            
        def count(node):
            if(node == -1):
                return 0
            
            return 1 + count(leftChild[node]) + count(rightChild[node])
        return count(root) == n