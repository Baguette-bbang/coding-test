# 모든 로프를 사용해야 할 필요는 없으며, 임의로 몇 개의 로프를 골라서 사용해도 된다.
n = int(input())
ropes = []
for _ in range(n):
  ropes.append(int(input()))


ropes.sort()
max_weight = 0
for i in range(n):
  weight = ropes[i] * (n-i)
  if max_weight < weight:
    max_weight = weight

print(max_weight)