import sys
input = sys.stdin.readline
n = int(input())
lines = [list(map(int, input().split())) for _ in range(n)]

lines.sort()
start = lines[0][0]
end = lines[0][1]
length = end - start

for i in range(1, n):
    # 겹쳤는가?
    if end >= lines[i][0]:
        add_length = lines[i][1] - end
        length += max(add_length, 0)
        end = max(end, lines[i][1])
    # 겹치지 않았는가?
    else:
        start = lines[i][0]
        end = lines[i][1]
        length += end - start
        
print(length)