class Node:
    def __init__(self, val = None, B = None):
        self.val = val
        self.B = set()
        if B:
            self.B.add(B)

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        if len(edges) == 0:
            return True
        self.n = n
        nodes = {}
        for edge in edges:
            A, B = edge[0], edge[1]
            if A not in nodes:
                nodes[A] = Node(val=A)
            if B not in nodes:
                nodes[B] = Node(val=B)
            nodes[A].B.add(nodes[B])
            nodes[B].B.add(nodes[A])
        self.visited = set()
        def dfs(node):
            if node in self.visited:
                return
            self.n-=1
            self.visited.add(node)
            for nd in node.B:
                dfs(nd)
        dfs(nodes[edges[0][0]])
        return self.n==0

                    