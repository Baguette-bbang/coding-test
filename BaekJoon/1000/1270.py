from collections import Counter
import sys 
input = sys.stdin.readline
# 카운터로 접근
# 1. 리스트를 받고 길이를 구함.
# 2. 카운터를 취함
# 3. 카운터를 내림차순 정렬
# 4. 맨 앞의 수가 절반 초과의 숫자라면 출력 아니라면 SYJKGW
    # 가장 많은 땅을 점령한 군대의 종류
n = int(input())
for i in range(n):
    land_state = list(map(int, input().split()))
    length = land_state[0]
    land_state = Counter(land_state[1:])
    land_state = sorted(land_state.items(), key=lambda x : -x[1])
    
    best_army = land_state[0]
    if best_army[1] > length//2 :
        print(best_army[0])
    else:
        print('SYJKGW')