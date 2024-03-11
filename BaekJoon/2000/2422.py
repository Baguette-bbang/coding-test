# 모든 아이스크림은 1부터 N까지 번호가 매겨져
# 아이스크림을 3가지 선택
# 하지만 기피해야하는 조합이 있다.
import sys 
input = sys.stdin.readline
from itertools import combinations
n, m = map(int, input().split())
not_combis = [list(map(int, input().split())) for _ in range(m)]
combis = list(combinations([i for i in range(1, n+1)], 3))
length = len(list(combis))
real_not_combi = set()
for not_combi in not_combis:
    temp = [i for i in range(1, n+1)]
    temp.remove(not_combi[0])
    temp.remove(not_combi[1])
    for t in temp:
        temp_real = tuple(sorted(not_combi+[t]))
        real_not_combi.add(temp_real)
print(length - len(real_not_combi))
print(length)