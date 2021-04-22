from collections import deque
n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]
depth = [-1] * (n+1)
for i in range(1, m+1):
    a, b = map(int, input().split())
    graph[a].append(b)
depth[x] = 0

def bfs(graph, cnt, idx, depth):
    queue = deque([idx])

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if depth[i] == -1:
                depth[i] = depth[v] + 1
                queue.append(i)


bfs(graph, 0, x, depth)


result = []
for i in range(len(depth)):
    if depth[i] == k:
        result.append(i)

if len(result)==0:
    print(-1)
else:
    for i in result:
        print(i)
