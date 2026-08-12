from collections import deque
from collections import defaultdict
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = range(len(edges)+1)
        parent = list(n) # connected graph with 1 cycle has n edges == n nodes
        rank = [0 for node in n]

        def find(node):
            if parent[node] == node:
                return node
            parent[node] = find(parent[node])

            return parent[node]
        
        def union(node1, node2):
            root1 = find(node1)
            root2 = find(node2)

            if root1 == root2:
                return False # => node1 and node2 are in the same component
            if rank[root1] < rank[node2]:
                parent[root1] = root2
            elif rank[root1] > rank[root2]:
                parent[root2] = root1
            else:
                parent[root1] = root2
                rank[root2] += 1
            
            return True

        for u, v in edges:
            result = union(u,v)
            if not result:
                return [u,v]

        

        

                    
        
        