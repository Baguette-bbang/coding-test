h, w = map(int, input().split())
block_hs = list(map(int, input().split()))
graph = [[0]*(w) for _ in range(h+1)]
graph[-1] = [1] * w # 바닥은 모조리 벽임.

for i in range(len(block_hs)):
    for j in range(h-1,h-block_hs[i]-1,-1):
        graph[j][i] = 1
        
cnt = 0
for i, floor in enumerate(graph[:-1]):
    # 첫 번째와 마지막 1의 위치 찾기
    idx1 = -1
    idx2 = -1
    for j, val in enumerate(floor):
        if val == 1:
            if idx1 == -1:
                idx1 = j  # 첫 번째 1의 위치
            idx2 = j  # 마지막 1의 위치 (계속 업데이트)

    # 1 사이의 0을 모두 2로 바꾸기
    if idx1 != -1 and idx2 != -1 and idx1 != idx2:
        for j in range(idx1, idx2 + 1):
            if floor[j] == 0:
                graph[i][j] = 2
                cnt += 1
print(cnt)