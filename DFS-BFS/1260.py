from collections import deque

def dfs(graph, idx, visited):
    visited[idx] = True
    print(idx, end=' ')
    for i in graph[idx]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, idx, visited):
    visited[idx] = True
    queue = deque([idx])
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True


n, m, v = map(int, input().split())
graph = [[] * (n+1) for i in range(n+1)]
visited = [False for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n+1):
    graph[i].sort()


dfs(graph, v, visited)
visited = [False for _ in range(n+1)]
print()
bfs(graph, v, visited)
