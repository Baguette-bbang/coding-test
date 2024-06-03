# 11399번 ATM 그리디 문제

n = int(input())
times = sorted(list(map(int, input().split())))

# 도착시간은 다 동일하다고 가정된 상황
# 1. 오름차순 정렬 
# 2. 돈을 인출하는데 걸리는 시간 : 앞 사람들의 시간들의 합 + 본인의 인출 시간
# 3 + 3+1 + 3+1+4 + 3+1+4+3
# 1 2 3 3 4
# 1 + 1+2 + 1+2+3 + 1+2+3+3 + 1+2+3+3+4
time_sum = times[0]
for i in range(1, len(times)):
    time_sum += sum(times[:i]) + times[i]
print(time_sum)