# 경우의 수 출력임.
# 각 열에는 각 색에 해당하는 경우의 수가 0~N까지 주어지게 됨.

r,g,b = map(int, input().split())
for i in range(r):
    for j in range(g):
        for k in range(b):
            print(i, j ,k)
print(r*g*b)