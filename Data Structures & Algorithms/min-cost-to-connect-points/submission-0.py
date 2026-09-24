class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        def manhattanDistance(point1, point2):
            x1, y1 = point1
            x2, y2 = point2
            return abs(x1-x2) + abs(y1-y2)

        # first compute the distances from each point to every other point, then sort the edges:
        edges = []
        for i in range(len(points)):
            for j in range(len(points)):
                if points[i] != points[j]:
                    distance = manhattanDistance(points[i], points[j])
                    edges.append([i,j, distance])
        
        edges.sort(key = lambda x: x[2])
        
        parent = [i for i in range(len(points))] 
        rank = [0] * len(points)

        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]

        
        def union(i, j):

            root_i, root_j = find(i), find(j)
            if root_i == root_j: # same parent already in same group
               return False

            if rank[root_i] < rank[root_j]:
                parent[root_i] = root_j
            elif rank[root_j] < rank[root_i]:
                parent[root_j] = i
            else:
                parent[root_i] = j
                rank[root_j] += 1
            return True

        size = 0
        minCost = 0
        for u, v, w in edges:
            if union(u, v):
                minCost += w
                size+=1

            if size == len(points)-1: # MST found when V-1 edges in graph where V is num nodes = len(points)
               return minCost
        return minCost

        
        
            








        