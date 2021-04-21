from collections import deque

n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# ↑ → ↓ ←
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

cnt=0
def bfs(graph, hcnt, x, y):
    graph[x][y] = 0
    global cnt
    cnt += 1
    queue = deque()
    queue.append(x)
    queue.append(y)

    while queue:
        x = queue.popleft()
        y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or ny < 0 or nx>=n or ny>=n:
                continue
            else:
                if graph[nx][ny] == 1:
                    hcnt += 1
                    graph[nx][ny] = 0
                    queue.append(nx)
                    queue.append(ny)

    return hcnt

home = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            home.append(bfs(graph, 1, i, j))
home.sort()
print(cnt)
for i in home:
    print(i)
