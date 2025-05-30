class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        def pop_dis(start):
            nonlocal n
            dis = [-1] * n
            steps = 0
            while(start != -1 and dis[start] == -1):
                dis[start] = steps
                start = edges[start]
                steps += 1
            
            return dis
        
        n = len(edges)
        dis1 = pop_dis(node1)
        dis2 = pop_dis(node2)
        min_dis = inf
        res = -1
        for i in range(n):
            if dis1[i] != -1 and dis2[i] != -1:
                max_dis = max(dis1[i], dis2[i])
                if max_dis < min_dis:
                    min_dis = max_dis
                    res = i
        
        return res





