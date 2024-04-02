# 실버4 게임을 만든 동준이
# 시작 27분 종료 39분 총 12분 소요
# 맨 뒤부터 탐색. 
# 앞으로 이동하면서 뒤의 수보다 1만큼만 작으면 됨.
import sys 
input = sys.stdin.readline
n = int(input())
numbers = list(int(input()) for _ in range(n))
numbers.reverse()
answer = 0
for i in range(1, n):
    if numbers[i-1] <= numbers[i]:
        answer += numbers[i] - numbers[i-1] + 1
        numbers[i] = numbers[i-1] - 1

print(answer)