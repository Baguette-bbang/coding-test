from collections import deque
import sys
input = sys.stdin.readline
# 이동할 때마다 윗 면에 쓰여 있는 수를 출력
# 바깥으로 이동하는 명령은 무시 & 출력 금지
n, m, r, c, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
order = list(map(int, input().split())) # 동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4
moves = {1:(0,1), 2:(0,-1), 3:(-1,0), 4:(1,0)} # 명령에 따른 움직임 설정
dice_value = {"top":0,"forward":0,"right":0,"left":0,"backward":0,"bottom":0}
orders = deque(order)

while orders:
    order = orders.popleft()
    #print("order : ",order)
    # 명령을 기반으로 새로운 위치로 업데이트해야함.
    dr = moves[order][0]
    dc = moves[order][1]
    
    nr, nc = dr+r, dc+c
    
    if 0<=nr<n and 0<=nc<m: # 이동할 수 있다면
        bottom, top, right,left,backward,forward = dice_value["bottom"], dice_value["top"],dice_value["right"],dice_value["left"],dice_value["backward"],dice_value["forward"]
        
        if order == 1: # 동쪽 이동
            top = dice_value["left"]
            right = dice_value["top"]
            left = dice_value["bottom"]
            bottom = dice_value["right"]
            
        elif order == 2: # 서쪽 이동
            top = dice_value["right"]
            left = dice_value["top"]
            right = dice_value["bottom"]
            bottom = dice_value["left"]
    
        elif order == 3: # 북쪽으로 이동
            forward = dice_value["top"]
            backward = dice_value["bottom"]
            top = dice_value["backward"]
            bottom = dice_value["forward"]
            
        elif order == 4: # 남쪽으로 이동
            top = dice_value["forward"]
            backward = dice_value["top"]
            forward = dice_value["bottom"]
            bottom = dice_value["backward"]
            
        if graph[nr][nc] == 0: # 주사위를 굴렸을 때, 이동한 칸에 쓰여 있는 수가 0이면, 주사위의 바닥면에 쓰여 있는 수가 칸에 복사
            graph[nr][nc] = bottom 
        else: #  0이 아닌 경우에는 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사
            bottom = graph[nr][nc]
            graph[nr][nc] = 0 # 칸에 쓰여 있는 수는 0이 된다.
            
        dice_value["bottom"] = bottom    
        dice_value["top"] = top
        dice_value["right"] = right
        dice_value["left"] = left
        dice_value["forward"] = forward
        dice_value["backward"] = backward
        
        print(dice_value["top"])
        r, c = nr, nc