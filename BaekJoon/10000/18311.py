# N개의 코스를 끝까지 도달 후 다시 출발 지점으로 돌아와야한다.
# 이동 거리가 K일때, 현재 지나고 있는 코스의 번호를 출력하라
# 이동 거리가 K가 두 코스 사이에 위치한 경우에는 ‘지나야 할’ 코스의 번호를 출력

# 이동거리를 가중합해서 하나의 코스로 만든다?
# 순차적으로 가지고 있는거리에서 빼면된다.
# 그리고 거리가 아직 남아있다면 리버스하면 된다.

n, k = map(int, input().split())
course = list(map(int, input().split()))

for i in range(len(course)):
    k -= course[i]
    if k <= 0:
        if k==0:
            print(i+1+1)
        else:
            print(i+1)
        break
    
reverse_course = course[::-1]
if k>0:
    for i in range(len(course)):
        k -= reverse_course[i]
        if k <= 0:
            if k==0: 
                print(n-i-1)
            else:
                print(n-i)
            break