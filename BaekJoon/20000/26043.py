from collections import deque
# 1로 시작하면 학생 번호, 좋아하는 메뉴
# 2로 시작하면 준비된 메뉴 
# 학생들은 순서대로 메뉴를 처리해야하며, 좋아하지 않는 메뉴를 먹는 경우도 있다.
import sys 
input = sys.stdin.readline
n = int(input())
like = []
unlike = []
not_yet = []
queue = deque()
for i in range(n):
    line = list(map(int, input().split()))
    student = 0
    menu = 0

    if line[0] == 1:
        student = line[1] 
        menu = line[2] 
        queue.append((student, menu))        
    else:
        menu = line[1]
        student, like_menu = queue.popleft()
        if like_menu == menu:
            like.append(student)
        else:
            unlike.append(student)

if not like:
    print('None')
else:
    print(*sorted(like))
if not unlike:
    print('None')
else:
    print(*sorted(unlike))
if not queue:
    print('None')
else:
    not_list = list(queue)
    not_yet = [i for i,j in not_list]
    print(*sorted(not_yet))