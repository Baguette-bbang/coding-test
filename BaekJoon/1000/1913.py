# 좌 하 우 상 순서로 채워야함.
# 종료조건은 49라는 수를 다 쓰는 경우
n = int(input())
target = int(input())
graph = [[0] * n for _ in range(n)]

cur_num = n*n
top, bottom = 0, n-1 
left, right = 0, n-1

while cur_num >= 1:
    # 좌측 
    for i in range(top, bottom+1):
        graph[i][left] = cur_num
        cur_num-=1
    left+=1
    
    # 하측
    for i in range(left, right+1):
        graph[bottom][i] = cur_num
        cur_num-=1
    bottom-=1
    
    # 우측
    for i in range(bottom, top-1, -1):
        graph[i][right] = cur_num
        cur_num-=1
    right -= 1
    
    # 상측
    for i in range(right, left-1, -1):
        graph[top][i] = cur_num
        cur_num -= 1
    top += 1
    
target_coordinate = ()
for i in range(n):
    for j in range(n):
        print(graph[i][j], end =' ')
        if graph[i][j]==target:
            target_coordinate = (i+1,j+1)
    print()
print(target_coordinate[0],target_coordinate[1])