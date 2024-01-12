import sys 
input = sys.stdin.readline
n, m = map(int, input().split())
trees = list(map(int, input().split()))
# H를 1부터 len(trees[-1])까지 설정
# 필요길이보다 나오지 않을때까지 반복
start = 1
end = max(trees)
max_h = 0
while start <= end:
    h = (start + end) // 2
    num = 0
    for tree in trees:
        if tree > h :
            num += tree-h
        if num > m:
            break
    if num >= m: # 잘라야하는 양보다 같거나 많이 잘랐다면
        max_h = h # 최대 높이
        start = h+1 # 높이를 더 올려야 함.
    else:
        end = h-1 # 높이를 더 낮춰야 함.
print(max_h)