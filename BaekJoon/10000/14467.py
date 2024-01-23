cows = {}
n = int(input())
cross_cnt = 0
for i in range(n):
    cow_num, loc  = map(int, input().split())
    if cow_num not in cows:
        cows[cow_num] = loc
    else:
        if cows[cow_num] != loc:
            cows[cow_num] = loc
            cross_cnt += 1
print(cross_cnt)