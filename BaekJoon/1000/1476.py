# 준규가 사는 나라는 우리가 사용하는 연도와 다른 방식임.
# 수 3개를 이용해 연도를 표현(지구, 태양, 달)
# 1 ≤ 지구(E) ≤ 15, 1 ≤ 태양(S) ≤ 28, 1 ≤ 달(M) ≤ 19
# brute하게 1 1 1부터 15 28 19까지 나타내는 수를 
# 어차피 표시 가능한 수는 7980개밖에 안됨.
# 문제 상황: 1부터 다 구하면 시간초과가 나올 확률이 큼
E, S, M = map(int, input().split())

our_year = 1
temp_E = 1
temp_S = 1
temp_M = 1
for _ in range(1, 7981):
    if temp_E == E and temp_S == S and temp_M == M:
        print(our_year)
        break
    
    if temp_E <15 and temp_S < 28 and temp_M < 19:
        pass
        
    else:
        if temp_E == 15:
            temp_E = 0
        if temp_S == 28:
            temp_S = 0
        if temp_M == 19:
            temp_M = 0
        
    temp_M += 1
    temp_S += 1
    temp_E += 1
    our_year += 1
    