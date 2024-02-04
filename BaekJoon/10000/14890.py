import sys
input = sys.stdin.readline
n, l = map(int, input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
road = 0

def check_decline(line, visited, l, r):
    n = len(line)
    for i in range(n - 1):
        if abs(line[i] - line[i + 1]) >= 2:
            return False

        if abs(line[i] - line[i + 1]) == 1:
            if line[i] > line[i + 1]:  # 현재 땅보다 다음 땅이 낮은 경우
                if i + l < n:  # 경사로 설치 가능 범위 체크
                    for j in range(i + 1, i + l + 1):
                        # 높이가 달라지거나 이미 경사로가 설치된 경우
                        if line[j] != line[i + 1] or visited[r][j]:
                            return False
                    # 경사로 설치
                    for j in range(i + 1, i + l + 1):
                        visited[r][j] = True
                else:
                    return False
                        
            else:  # 현재 땅보다 다음 땅이 높은 경우
                if i - l >= -1:
                    for j in range(i, i - l, -1):
                        # 높이가 달라지거나 이미 경사로가 설치된 경우
                        if line[j] != line[i] or visited[r][j]:
                            return False
                    # 경사로 설치
                    for j in range(i, i - l, -1):
                        visited[r][j] = True
                else:
                    return False
    return True


# 행 검사
for i in range(n):
    temp_visited = visited[i].copy()
    if len(set(graph[i])) == 1 or check_decline(graph[i], visited, l, i):
        road += 1
    else:
        visited[i] = temp_visited

# graph 전치
graph_transposed = list(map(list, zip(*graph)))
visited = [[False] * n for _ in range(n)]
for i in range(n):
    temp_visited = visited[i].copy()
    if len(set(graph_transposed[i])) == 1 or check_decline(graph_transposed[i], visited, l, i):
        road += 1
    else:
        visited[i] = temp_visited
print(road)