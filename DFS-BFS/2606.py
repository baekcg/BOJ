from collections import deque

def bfs(graph, idx, visited):
    visited[idx] = True
    result = -1
    queue = deque([idx])
    while queue:
        v = queue.popleft()
        result += 1
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True
    return result


n = int(input())
m = int(input())

graph = [[] * (n+1) for _ in range(n+1)]
visited = [False for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n+1):
    graph[i].sort()


print(bfs(graph, 1, visited))

