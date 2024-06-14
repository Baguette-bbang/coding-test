from collections import deque

n, m, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

def rotate_layer_anticlockwise(graph, n, m, rotations):
    layers = min(n, m) // 2
    for layer in range(layers):
        top = layer
        left = layer
        bottom = n - 1 - layer
        right = m - 1 - layer

        current_layer = deque()

        # 왼쪽 열 (위에서 아래로)
        for row in range(top, bottom + 1):
            current_layer.append(graph[row][left])
        
        # 아랫 행 (왼쪽에서 오른쪽으로)
        for col in range(left + 1, right + 1):
            current_layer.append(graph[bottom][col])
        
        # 오른쪽 열 (아래에서 위로)
        for row in range(bottom - 1, top - 1, -1):
            current_layer.append(graph[row][right])
        
        # 윗 행 (오른쪽에서 왼쪽으로)
        for col in range(right - 1, left, -1):
            current_layer.append(graph[top][col])
        
        # 회전 적용 (반시계 방향으로 회전)
        current_layer.rotate(rotations)
        
        idx = 0

        # 회전된 값 다시 행렬에 대입
        # 왼쪽 열 (위에서 아래로)
        for row in range(top, bottom + 1):
            graph[row][left] = current_layer[idx]
            idx += 1
        
        # 아랫 행 (왼쪽에서 오른쪽으로)
        for col in range(left + 1, right + 1):
            graph[bottom][col] = current_layer[idx]
            idx += 1
        
        # 오른쪽 열 (아래에서 위로)
        for row in range(bottom - 1, top - 1, -1):
            graph[row][right] = current_layer[idx]
            idx += 1
        
        # 윗 행 (오른쪽에서 왼쪽으로)
        for col in range(right - 1, left, -1):
            graph[top][col] = current_layer[idx]
            idx += 1

rotate_layer_anticlockwise(graph, n, m, r)

for row in graph:
    print(" ".join(map(str, row)))