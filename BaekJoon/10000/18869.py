import sys
input = sys.stdin.readline
m, n = map(int, input().split()) # 우주의 개수 입력받기
universes = [list(map(int, input().split())) for _ in range(m)]
def compress_coordinates(universe):
    unique_sorted_values = sorted(set(universe))
    print(unique_sorted_values)
    value_to_index = {value: index for index, value in enumerate(unique_sorted_values)}
    return tuple(value_to_index[value] for value in universe)

# 각 우주를 좌표 압축
compressed_universes = [compress_coordinates(universe) for universe in universes]
compressed_universes = sorted(compressed_universes)
print(compressed_universes)
from bisect import bisect_left, bisect_right
uni_dict = {}
for cu in compressed_universes:
    if cu not in uni_dict:
        left = bisect_left(compressed_universes, cu)
        right = bisect_right(compressed_universes, cu)
        count = right - left
        uni_dict[cu] = count
answer = 0
for count in uni_dict.values():  
    answer += count * (count - 1) // 2
print(answer)