from collections import deque, Counter
# bfs 로 접근해야하는 문제 가장 레벨이 높아야한다.
# 1. 입력값을 통해서 지도를 만들기(인접행렬그래프)
# 2. bfs를 통한 탐색

# 조건 1. 출발지로부터 거리를 알아야 한다.
# 조건 2. 같은 거리를 갖는 것들을 알아야 한다.
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _  in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
# print(graph)

queue = deque([(1,0)])
visited = [False for _ in range(n+1)]
# print(visited)
visited[1] = True
answer = []
while queue:
    p_node, cnt = queue.popleft()
    for c_node in graph[p_node]:
        if not visited[c_node]:
            queue.append((c_node, cnt+1))
            answer.append((c_node, cnt+1))
            visited[c_node] = True
hide = sorted(answer, key = lambda x : (-x[1],x[0]))[0]
print(hide[0], end = ' ')
print(hide[1], end = ' ')
count_num = Counter(list(zip(*answer))[1])
print(count_num[hide[1]])