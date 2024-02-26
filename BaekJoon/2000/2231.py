n = int(input())
for i in range(n):
    temp = i
    num = i
    while temp:
        num += temp%10
        temp //= 10
    if num == n:
        print(i)
        break
else:
    print(0)