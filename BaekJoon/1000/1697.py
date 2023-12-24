from collections import deque
import sys
input = sys.stdin.readline
N, K = map(int, input().split())
# 인접 그래프 생성
# 한 정점당 세가지 길이 있음.
# 넉넉하게 동생 위치의 두배까지 만듦

def find_shortest_bfs(g, start, end):
    # 초기화
    visited = set()
    queue = deque([(start,0)])
    
    while queue : # 일단 큐가 빌때까지 반복
        node, distance = queue.popleft()
        if node == end:
            return distance
        if node not in visited: # 방문되지 않은 노드라면 기존 path에 새로 경로를 하나씩 추가하여 다시 넣기
            visited.add(node)
            for location in g[node]:
                if location not in visited:
                    queue.append((location, distance+1))
    return 0

if K <= N:
    print(N-K)
else : 
    g = [[]for _ in range(K+10)]
    g[0].append(1)    
    # 인접행렬 채우기
    for i in range(1, len(g)):
        g[i].append(i-1)
        if i+1 < len(g):
            g[i].append(i+1)
        # 같은 것이 있다면 추가X, 인접행렬의 크기보다 크다면 추가X 
        if i*2 < len(g) and i*2 not in g[i]:
            g[i].append(i*2)

    shortest_path = find_shortest_bfs(g, N, K)
    print(shortest_path)

# 시간 줄이는 방법은??