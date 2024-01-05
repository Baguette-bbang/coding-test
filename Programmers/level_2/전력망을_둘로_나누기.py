from collections import deque
from copy import deepcopy

def bfs(visited, n, graph, start, cnt):
    queue = deque([start])
    cnt = 0
    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                cnt+=1
    return cnt
    
def solution(n, wires):
    answer = -1
    # 인접노드 형태로 이루어진 전력망
    # 네트워크를 둘로 나누어 최대한 비슷한 전력망이 되도록 만들기
    # 간선이 끊어지는 것을 어떻게 표현하는지...
    # wires에 있는 하나의 리스트를 삭제하기만 하면 됨.
    # bfs로 탐색
    min_n = float('inf')
    for wire in wires:
        visited = [False] * (n+1)
        new_wire = deepcopy(wires)
        new_wire.remove(wire)
        print(new_wire)
        graph = [[] for _ in range(n+1)]
        for n1, n2 in new_wire:
            graph[n1].append(n2)
            graph[n2].append(n1)
        n1 = bfs(visited, n, graph, 1, 0)
        n2 = n - n1
        min_n = min(min_n, abs(n1-n2))
    return min_n