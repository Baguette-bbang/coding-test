n, m, r = map(int,input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
a_list = list(map(int,input().split()))

def a1(graph): # 상하좌우
    return graph[::-1]

def a2(graph,n,m): # 좌우반전
    for i in range(m//2): # 열의 수 m
        for j in range(n): # 행의 수 n
            graph[j][i], graph[j][m-1-i] = graph[j][m-1-i] ,graph[j][i]
    return graph

def a3(graph,n,m):
    # 1열 -> 1행
    # 2열 -> 2행
    graph = graph[::-1]
    temp_graph = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            temp_graph[j][i] = graph[i][j]
    return temp_graph

def a4(graph, n,m): # 좌우 반전에 오른쪽 회전 -> 왼쪽 회전
    graph = a2(graph, n,m)
    temp_graph = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            temp_graph[j][i] = graph[i][j]
    return temp_graph

def a5(graph,n,m):
    # 네 등분으로 쪼개야함.
    # 1번 : 0번행~n//2행, 0번열~m//2열
    # 2번 : 0번행~n//2행, m//2번열~m열
    # 3번 : n//2번행~n행, m//2번열~m열
    # 4번 : n//2번행~n행, 0번열~m//2열
    temp_graph = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if i < n//2 and j<m//2: # 1 <- 4
                temp_graph[i][j] = graph[i+n//2][j]
            elif i<n//2 and j<m//2: # 2 <- 1
                # 0번열이 4번열로
                temp_graph[i][j] = graph[i][j+m//2]
            elif i>=n//2 and j>=m//2: # 3 <- 2
                # 0번열이 3번열로
                temp_graph[i][j] = graph[i-n//2][j]
            else:
                temp_graph[i][j] = graph[i][j-m//2]
    return temp_graph

def a6(graph, n,m):
    return a2(a5(a2(graph, n,m),n,m),n,m)

# n과 m은 짝수이다.
for a in a_list:
    n = len(graph)
    m = len(graph[0])
    if a == 1:
        graph = a1(graph)
    elif a == 2:
        graph = a2(graph, n,m)
    elif a == 3:
        graph = a3(graph,n,m)
    elif a == 4:
        graph = a4(graph, n,m)
    elif a == 5:
        graph = a5(graph,n,m)
    elif a == 6:
        graph = a6(graph, n,m)
        
for i in range(len(graph)):
    print(*graph[i])