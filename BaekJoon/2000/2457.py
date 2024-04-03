import sys
input = sys.stdin.readline

n = int(input())
flowers = [list(map(int, input().split())) for _ in range(n)]
flowers.sort(key=lambda x: (x[0], x[1]))  # 꽃이 피는 날짜 기준으로 정렬

answer = 0
latest = [3, 1]  # 시작 날짜
idx = 0  # 최적의 꽃을 찾기 시작할 인덱스
final = False  # 기간을 충족하는지 여부

# 3월 1일 이전에 피는 꽃 중 가장 늦게 지는 꽃 찾기
for i in range(n):
    if flowers[i][0] > 3 or (flowers[i][0] == 3 and flowers[i][1] > 1):
        break
    # 피는 날짜가 더 늦어도 먼저 질 수도 있음. 무조건 확인해야함.
    if flowers[i][2] > latest[0] or (flowers[i][2] == latest[0] and flowers[i][3] >= latest[1]):
        latest = flowers[i][2:4]
        idx = i + 1

if latest == [3, 1]:  # 시작할 꽃이 없는 경우
    print(0)
    exit(0)
if latest[0] == 12:
    print(1)
    exit(0)
    
answer += 1

# 범위 안의 일이라면
while idx < n:
    temp = [0, 0] # temp는 현재 고려 중인 꽃이 지는 날짜를 임시로 저장
    for i in range(idx, n):
        # 현재 꽃의 피는 월이 이전 꽃의 지는 월보다 먼저 피거나 월이 같다면 날짜가 먼저여야 한다.
        if (flowers[i][0] < latest[0]) or (flowers[i][0] == latest[0] and flowers[i][1] <= latest[1]):
            # temp는 현재 단계에서 선택 가능한 꽃들 중 가장 늦게 지는 꽃을 찾는 데 사용
            if (flowers[i][2] > temp[0]) or (flowers[i][2] == temp[0] and flowers[i][3] > temp[1]):
                temp = flowers[i][2:4]
                idx = i + 1
    if temp == [0, 0]:  # 연결되는 꽃이 없는 경우
        break
    latest = temp
    answer += 1
    if latest[0] == 12 :  # 12월 1일을 넘는 경우
        final = True
        break

if final:
    print(answer)
else:
    print(0)
