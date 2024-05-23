n = int(input())
num_list = sorted(list(set(map(int, input().split()))))
print(*num_list)