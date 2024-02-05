import sys
input = sys.stdin.readline
n, l = map(int, input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

def check_road(line, n, l, visited):
    for i in range(n-1):
        if abs(line[i] - line[i+1]) >= 2: # 높이가 1 이상 차이나는 경우
            return False 
        if abs(line[i] - line[i + 1]) == 1: # 높이가 딱 1만 차이나는 경우
            if line[i] < line[i+1]: # 현재 위치가 다음 위치보다 더 낮은 경우
                # 충분한 범위가 있는가? 방문하지 않았는가?
                if i-l+1 >= 0:
                    for j in range(i, i-l, -1):
                        if line[j] != line[i] or visited[j]:
                            return False
                    for j in range(i, i-l, -1):
                        visited[j] = True
                else:
                    return False
            else:
                # 현재 위치가 다음 위치보다 높은 경우
                if i+l < n:
                    for j in range(i+1, i+l+1):
                        if line[j] != line[i+1] or visited[j]:
                            return False
                    for j in range(i+1, i+l+1):
                        visited[j] = True
                else:
                    return False
    return True
          
road = 0
for line in graph:
    visited = [False] * n
    if len(set(line)) == 1 or check_road(line, n, l, visited):
        road += 1
        
graph_transposed = list(zip(*graph))
for line in graph_transposed:
    visited = [False] * n
    if len(set(line)) == 1 or check_road(line, n, l, visited):
        road += 1
print(road)