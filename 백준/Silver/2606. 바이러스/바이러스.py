from collections import deque
N = int(input())
M = int(input())

# graph 리스트 만드는 함수 정의
def make_graph(a, b):
  graph[a].append(b)
  graph[b].append(a)
  graph[a].sort()
  graph[b].sort()

# graph 만들기
graph = [[] for _ in range(N+1)]
for i in range(M):
  a, b = map(int, input().split())
  make_graph(a, b)

# visited, answer 리스트 만들기
visited = [False] * (N+1)
answer = []
# DFS 함수 정의
def dfs(graph, v, visited):
  # 탐색한 노드의 방문처리
  visited[v] = True
  answer.append(v)
  # 인접한 노드를 재귀적으로 방문
  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)

dfs(graph, 1, visited)
print(len(answer)-1)