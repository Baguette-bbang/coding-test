from itertools import combinations

while True:
    num_list = list(map(int, input().split()))
    
    if num_list[0] == 0:
        break
    
    for combi in combinations(num_list[1:], 6):
        print(*combi)
    print()