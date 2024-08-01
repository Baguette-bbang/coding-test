# 넓이를 어떻게 구할 것인가?
# 거북이가 간 (최상단+최하단) * (최좌단 + 최우단)
# 움직이고 -> 넓이 구하고

n = int(input())

move = [(0,-1), (1,0), (0,1),(-1,0)] # 기본 값 상, 하 이동
for i in range(n):
  current_loc = [0,0]
  current_dir = 0 # 시작 방향은 북쪽 (0, -1)
  left, right, top, bottom = 0, 0, 0, 0
  controlls = list(input())
  
  for controll in controlls:
    if controll == 'L':
      current_dir = (current_dir - 1) % 4
    elif controll == 'R':
      current_dir = (current_dir + 1) % 4
    elif controll == 'F':
      current_loc[0] += move[current_dir][0] * 1
      current_loc[1] += move[current_dir][1] * 1
    elif controll == 'B':
      current_loc[0] += move[current_dir][0] * -1
      current_loc[1] += move[current_dir][1] * -1
    
    left = min(left,  current_loc[0])
    right = max(right, current_loc[0])
    top = min(top,  current_loc[1])
    bottom = max(bottom,  current_loc[1])
    
  print((abs(left) + abs(right)) * (abs(top) + abs(bottom)))