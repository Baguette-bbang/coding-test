import sys

def input():
    return sys.stdin.readline()
gears = [[0]* 8 for _ in range(4)]
for i in range(4):
    gears[i] = list(map(int, input().strip()))
K = int(input())

def rotate(lst, direction):
    # 반시계방향 회전
    if direction == -1:
        temp = lst[0]
        for i in range(len(lst)-1):
            lst[i] = lst[i+1]
        lst[-1] = temp
    else:
    # 시계방향회전
        temp = lst[-1]
        for i in range(len(lst)-1, 0, -1):
            lst[i] = lst[i-1]
        lst[0] = temp
    return lst

for _ in range(K):
    gearNum, direction = map(int, input().split())
    # 기어별 극점 
    pole = [gears[0][2], gears[1][6], gears[1][2], gears[2][6], gears[2][2], gears[3][6]]
    
    if gearNum==1:
        gears[0] = rotate(gears[0], direction)
        if pole[0]!=pole[1]:
            gears[1] = rotate(gears[1], -direction)
            if pole[2] != pole[3]:
                    gears[2] = rotate(gears[2], direction)
                    if pole[4] != pole[5]:
                        gears[3] = rotate(gears[3], -direction)
                        
    elif gearNum==2:
        gears[1] = rotate(gears[1], direction)
        if pole[2]!=pole[3]:
            gears[2] = rotate(gears[2], -direction)
            if pole[4] != pole[5]:
                gears[3] = rotate(gears[3], direction)
        if pole[1]!=pole[0]:
            gears[0] = rotate(gears[0], -direction)
            
    elif gearNum==3:
        gears[2] = rotate(gears[2], direction)
        if pole[3]!=pole[2]:
            gears[1] = rotate(gears[1], -direction)
            if pole[0] != pole[1]:
                    gears[0] = rotate(gears[0], direction)
        if pole[4]!=pole[5]:
            gears[3] = rotate(gears[3], -direction)
            
    elif gearNum==4:
        gears[3] = rotate(gears[3], direction)
        if pole[5]!=pole[4]:
            gears[2] = rotate(gears[2], -direction)
            if pole[2] != pole[3]:
                    gears[1] = rotate(gears[1], direction)
                    if pole[0] != pole[1]:
                        gears[0] = rotate(gears[0], -direction)
                        
# 1번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 1점
# 2번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 2점
# 3번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 4점
# 4번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 8점
answer = sum(gears[i][0] * (2 ** i) for i in range(4))
print(answer)
