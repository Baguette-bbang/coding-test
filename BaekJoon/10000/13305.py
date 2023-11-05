import sys
input = sys.stdin.readline
N = int(input())
distance = list(map(int, input().split()))
cities = list(map(int, input().split()))

min_city = cities[0]
cost = min_city * distance[0]
for i in range(1, N-1):
    if cities[i] < min_city:
        min_city = cities[i]
    cost += min_city * distance[i]
print(cost)