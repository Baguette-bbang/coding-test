n = int(input())
length = 0
i = 1
while i <= n:
    length += n - i + 1
    i *= 10
print(length)
