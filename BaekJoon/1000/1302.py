# 백준 1302번 베스트셀러 - 실버 4
# 가장 많이 팔린 제목을 출력하는 것
# 힙 자료구조를 사용해야 함.
from heapq import heapify, heappop, heappush
from collections import defaultdict
n = int(input())
heap = []
heap_dict = defaultdict(int)
for _ in range(n):
    heap_dict[input()] += 1
# print(heap_dict)

for item in heap_dict.items():
    heappush(heap, (-item[1], item[0]))
print(heappop(heap)[1])