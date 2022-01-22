def bfs(start, graph):
    visited = set()
    q = []

    q.append(start)
    visited.add(start)

    while len(q) > 0:
        cur = q.pop(0)
        for n in graph.get(cur, []):
            if not n in visited:
                q.append(n)
                visited.add(n)

    return visited


def dijkstra(graph, start, end):
    Q = set()
    dist = {}
    prev = {}

    for pos in graph.keys():
        dist[pos] = float("inf")
        prev[pos] = None
        Q.add(pos)
    dist[start] = 0.0

    while len(Q) > 0:
        u = _get_min_dist(Q, dist)
        Q.remove(u)

        for neighbour in graph[u]:
            alt = dist[u] + 1.0
            if alt < dist.get(neighbour, float("inf")):
                dist[neighbour] = alt
                prev[neighbour] = u

    path = []
    u = end
    if u in prev or u == start:
        while u:
            path.insert(0, u)
            u = prev.get(u)

    return path, dist, prev


def _get_min_dist(Q, dist):
    min = float("inf")
    for v in Q:
        if dist[v] <= min:
            min = dist[v]
            min_node = v
    return min_node
