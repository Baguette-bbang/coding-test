n = int(input())
trophies = []
for _ in range(n):
  trophies.append(int(input()))

biggest = 0
left = 0 
for tropy in trophies:
  if tropy > biggest:
    left += 1
    biggest = tropy

biggest = 0
right = 0
for tropy in trophies[::-1]:
  if tropy > biggest:
    right += 1
    biggest = tropy

print(left)
print(right)