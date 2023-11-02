from collections import deque

N, M, V = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for i in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
    graph[x].sort() # 정점 번호가 작은 것부터 방문하므로 정렬 필요
    graph[y].sort()

visited1 = [False] * (N + 1)
visited2 = [False] * (N + 1)

def DFS(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            DFS(graph, i, visited)

def BFS(graph, v, visited):
    queue = deque([v])
    visited[v] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

DFS(graph, V, visited1)
print()
BFS(graph, V, visited2)