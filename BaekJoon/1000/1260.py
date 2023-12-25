from collections import deque
import sys
input = sys.stdin.readline

N, M, V = map(int, input().split())
graph = [[]for _ in range(N+1)]
for _ in range(M):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node1].sort()
    graph[node2].append(node1)
    graph[node2].sort()

visited = [False for _ in range(N+1)]
def dfs(visited, graph, start, path):
    queue = deque([start])
    
    while queue:
        node = queue.pop()
        if not visited[node]:
            visited[node] = True
            path.append(node)
            for i in reversed(graph[node]):
                if not visited[i]:
                    queue.append(i)
    return path

dfs_path = dfs(visited, graph, V, [])
for i in dfs_path:
    print(i, end=' ')
print()

visited = [False for _ in range(N+1)]
def bfs(visited, graph, start, path):
    queue = deque()
    queue.append(start)
    
    while queue:
        node = queue.popleft()
        path.append(node)
        visited[node] = True
        for i in graph[node]:
            if not visited[i] and i not in queue:
                queue.append(i)
    return path

bfs_path = bfs(visited, graph, V, [])
for i in bfs_path:
    print(i, end=' ')
print()