from collections import deque
import sys
f = sys.stdin.readline

n, m, k, x = map(int, f().split())
graph = [[] for _ in range(n+1)]
distance = [0] * (n+1)
visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int, f().split())
    graph[a].append(b)

def bfs(graph, x, visited):
    visited[x] = True
    queue = deque([x])
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                distance[i] = distance[v] + 1
    if k not in distance:
        print(-1)
    else: 
        for j in range(len(distance)):
            if distance[j] == k:
                print(j)
                
bfs(graph, x, visited)
