class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        self.getPath(0, graph, res)
        return res
    
    def getPath(self, source, graph, res, curr_path = [0]):
        if(source == len(graph) - 1):
            res.append(curr_path)

        for i in graph[source]:
            self.getPath(i, graph, res, curr_path + [i])
    