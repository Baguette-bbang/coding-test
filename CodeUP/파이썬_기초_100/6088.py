a, d, n= map(int, input().split())
answer = a
for i in range(1, n):
    answer += d
print(answer)