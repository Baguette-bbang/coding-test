from itertools import product
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
nums = [1,2,3]
k_cnt = 0
combis = []
for i in range(1, 12):
    for j in product(nums, repeat=i):
        if sum(j) == n:
            k_cnt += 1
            combis.append(j)

if len(combis) >= k:
    print('+'.join(map(str,sorted(combis)[k-1])))
else:
    print(-1)