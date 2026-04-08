class Solution(object):
    def networkDelayTime(self, times, n, k):
        gr = {}
        for u, v, w in times:
            if u not in gr:
                gr[u] = []
            gr[u].append((v, w))

        dist = {}
        for i in range(1, n+1):
            dist[i] = float('inf')
        dist[k] = 0

        Q = set()
        for i in range(1, n+1):
            Q.add(i)

        # пока есть вершины
        while Q:
            # ищем вершину с минимальным расстоянием
            u = None
            for x in Q:
                if u is None or dist[x] < dist[u]:
                    u = x

            Q.remove(u)

            # смотрим соседей
            if u in gr:
                for v, w in gr[u]:
                    if dist[v] > dist[u] + w:
                        dist[v] = dist[u] + w

        # проверяем
        res = 0
        for i in dist:
            if dist[i] == float('inf'):
                return -1
            if dist[i] > res:
                res = dist[i]

        return res
        