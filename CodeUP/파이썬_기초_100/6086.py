n = int(input())
sum = 0
cnt = 1
while True:
   sum += cnt
   cnt += 1
   if sum >= n:
       break
print(sum)