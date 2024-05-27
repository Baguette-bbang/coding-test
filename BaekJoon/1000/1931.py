# 회의실 배정 문제
# 1. 종료 시간 기준 정렬
# 2. 다음 회의 시작 시간은 이전 회의 종료 시간 이후여야 함.

n = int(input())
times = []
for _ in range(n):
    times.append(list(map(int,input().split())))
times = sorted(times, key=lambda x : (x[1], x[0]))

answer = 0
em = 0
for start, end in times:
    if start >= em:
        em = end
        answer+=1

print(answer)