# 18111번 마인크래프트 - 실버2 문제
# 6시 정각 시작
# 6시 40분 종료
# 블럭을 모두 같은 높이로 맞추어야 하는 것이 핵심이다.
# 땅의 높이는 256블록을 초과할 수 없으며, 음수가 될 수 없다
# 제거는 2초 할당은 1초
# 답이 여러개라면 땅의 높이가 높은 것이 정답이다.
# 가장 낮은 것에 맞춰 할당
# 가장 높은 것에 맞춰 할당
# 둘 사이에 정답이 있다.
import sys
input = sys.stdin.readline
# 입력
n, m, b = map(int, input().split())

area = []
for _ in range(n):
    area.append(list(map(int, input().split())))

# 1. 가장 낮은 것부터 가장 높은 수까지 기준을 잡아가며 할당 (0~256)
# 2. 인벤 블록의 수가 없다면 break
# 3. 현재 구한 최솟값보다 크다면 break

min_time = float('inf')
final_height = 0

for height in range(257):
    time = 0 # height 당 소모 시간
    block = b
    # 맵 탐색
    for i in range(n):
        for j in range(m):
            # 블록 할당
            if area[i][j] <= height:
                diff = height - area[i][j]
                time += diff 
                block -= diff
            else:
                diff = area[i][j] - height
                time += diff * 2
                block += diff
        if min_time < time:
            time = float('inf')
            break
    if block >= 0 and min_time >= time:
        min_time = time
        final_height = height
print(min_time, final_height)