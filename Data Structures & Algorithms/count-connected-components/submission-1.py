from collections import defaultdict
from collections import deque
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        nodes = defaultdict(list)
        for A,B in edges:
            nodes[A].append(B)
            nodes[B].append(A)
        print(nodes)
        visited = set()
        count = 0
        for node, neighbors in nodes.items():
            if node not in visited:
                print(node)
                count+=1
                queue = deque([node])
                visited.add(node)
                while queue:
                    nextNode = queue.popleft()
                    print("currentNode: ", nextNode)
                    for nd in nodes.get(nextNode):
                        if nd not in visited:
                            queue.append(nd)
                            visited.add(nd)
        return count + n - len(nodes)



        
        
        