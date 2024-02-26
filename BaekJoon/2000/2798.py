n, m = map(int, input().split())
cards = list(map(int, input().split()))

from itertools import combinations
max_com = 0
for com in combinations(cards, 3):
    sum_com = sum(com)
    if sum_com == m:
        max_com = sum_com
        break
    else:
        if sum_com < m:
            max_com = max(max_com, sum_com)
print(max_com)