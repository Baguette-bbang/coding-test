from collections import deque
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
conveyor_belt = list(map(int, input().split()))

length = n*2
robots_loc = deque([False] * length) # 로봇의 위치
conveyor_belt_loc = deque([i for i in range(length)]) # 컨베이어 벨트 인덱스
stage = 0
while True:
    stage += 1
    # 1단계 회전
    conveyor_belt_loc.rotate()
    robots_loc.rotate()
    # 내리는 위치에 로봇이 도달하면 즉시 내려야함
    robots_loc[n-1] = False
    
    # 2단계 로봇 자체 회전
    for i in range(n-2, -1, -1):
        if robots_loc[i]: # 로봇이 들어있는 위치
            if not robots_loc[i+1] and conveyor_belt[conveyor_belt_loc[i+1]] >= 1: # 다음 칸에 로봇이 없고 내구도가 1 이상인가?
                # 로봇을 다음 칸으로 이동시킨다.
                robots_loc[i] ,robots_loc[i+1] = False, True
                # 다음칸의 내구도를 감소시킨다.
                conveyor_belt[conveyor_belt_loc[i+1]] -= 1
                # 이동한 칸이 내리는 칸인가?
                if i+1 == n-1:
                    robots_loc[i+1] = False
                    
    # 3단계 올리기
    if conveyor_belt[conveyor_belt_loc[0]] >= 1:
        robots_loc[0] = True
        conveyor_belt[conveyor_belt_loc[0]] -= 1
    
    # 4단계 0 확인하기
    if conveyor_belt.count(0) >= k:
        break
print(stage)