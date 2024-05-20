n = int(input())
a = list(map(int, input().split()))

# 값과 인덱스로 매핑
mapping_list = []
for i in range(n):
    mapping_list.append((a[i], i))
    
sorted_list = sorted(mapping_list)

# print(sorted_list)
# 정렬된 리스트에서 원래 인덱스를 통해서 값을 채운다.
p = [0] * n
for i in range(n):
    #print(sorted_list[i][1])
    p[sorted_list[i][1]] = i

for i in range(n):
    print(p[i], end = ' ')