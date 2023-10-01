import numpy as np
import sys

# input
N, M = map(int, sys.stdin.readline().split())
Nlist = list(map(int, sys.stdin.readline().split()))

# 누적합 리스트 초기화
cumulativeList = [0 for _ in range(N)]
cumulativeList[0] = Nlist[0]
for i in range(1, N):
    cumulativeList[i] = Nlist[i] + cumulativeList[i-1]

# 입력 M번만큼 반복
for _ in range(M):
    # 누적합을 통해 i~j사이의 값을 구함
    i, j = map(int, sys.stdin.readline().split())
    i -= 1 # 입력값을 배열처리
    j -= 1 # 입력값을 배열처리
    if i==0: # 예외처리 list[0]~list[j]의 합
        print(cumulativeList[j])
    else : # list[0]~list[j]의 합 - list[0]~list[i-1]의 합 
        print(cumulativeList[j]-cumulativeList[i-1])