n = int(input())
left = 1
right = n

while left < right:
    mid = (left + right) // 2
    if mid * (mid + 1) // 2 >= n:
        right = mid
    else:
        left = mid + 1

print(left)