class Solution(object):
    def minCostConnectPoints(self, points):
        n = len(points)
        
        edg = []

        # строим все ребра
        for i in range(n):
            for j in range(i+1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                w = abs(x1 - x2) + abs(y1 - y2)
                edg.append((w, i, j))

        edg.sort()  # сортируем по весу

        parent = [i for i in range(n)]

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            parent[find(a)] = find(b)

        res = 0

        for w, u, v in edg:
            if find(u) != find(v):
                union(u, v)
                res += w

        return res
        