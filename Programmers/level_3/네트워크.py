from collections import deque
def bfs(graph, visited, start, n):
    queue = deque([start])
    while queue:
        computer = queue.popleft()
        visited[computer] = True
        for net_com in graph[computer]:
            if 0 <= net_com < n and not visited[net_com]:
                visited[net_com] = True
                queue.append(net_com)
                
def solution(n, computers):
    answer = 0
    # i 위치에 있는 컴퓨터와 연결된 것
    # computers[i]에 j위치에 1로서 표현이 된다.
    # 인접 행렬 생성
    graph = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                graph[i].append(j)
                
    # 방문 표시 컴퓨터의 개수만큼 존재
    visited = [False] * n
    
    # 인접행렬을 돌면서 
    for com in range(n):
        if not visited[com]:
            bfs(graph, visited, com, n)
            answer +=1
            
    return answer
