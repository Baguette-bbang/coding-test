from heapq import heappush, heappop
import sys
input = sys.stdin.readline

n = int(input())
schedule = [list(map(int, input().split())) for _ in range(n)]
schedule = sorted(schedule)
room = []

for start, end in schedule:
    if room and start >= room[0]:
        heappop(room)
    heappush(room, end)
    
print(len(room))