from heapq import heappop, heappush, heapify

n, m = map(int, input().split())
num_list = list(map(int, input().split()))

heapify(num_list)
for i in range(m):
    a = heappop(num_list)
    b = heappop(num_list)
    
    heappush(num_list, a+b)
    heappush(num_list, a+b)
print(sum(num_list))