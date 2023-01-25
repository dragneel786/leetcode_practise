class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        if(node1 == node2):
            return node1
        
        commons = {(node1, 1), (node2, -1)}
        q = deque([(node1, 1), (node2, -1)])
        ans = inf
        while(q):
            for _ in range(len(q)):
                node, sign = q.popleft()
                if((edges[node], -1 * sign) in commons):
                    ans = min(ans, edges[node])

                # print(edges[node])
                elif(edges[node] != -1 and (edges[node], sign) not in commons):
                    commons.add((edges[node], sign))
                    q.append((edges[node], sign))


            if(ans != inf):
                return ans

        return -1
                    
                    