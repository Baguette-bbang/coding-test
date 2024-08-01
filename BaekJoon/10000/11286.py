from heapq import heapify, heappop, heappush
import sys
input = sys.stdin.readline
heap = []
for i in range(int(input())):
  n = int(input())
  if n != 0:
    heappush(heap, (abs(n), n))
  else:
    if (heap): 
      print(heappop(heap)[1])
    else:
      print(0)