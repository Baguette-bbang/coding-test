from heapq import heapify, heappop, heappush

n = int(input())
heap = []
for i in range(n):
  line = list(map(int, input().split()))
  if i > 0:
    for number in line:
      pop_num = heappop(heap)
      if pop_num > number:
        number = pop_num
      heappush(heap, number)
  else:
    for number in line:
      heappush(heap, number)

print(sorted(heap)[0])
