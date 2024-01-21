n = int(input())
d = [i for i in range(n+1)]
squares = [i*i for i in range(n+1)]
for i in range(n+1):
    for square in squares:
        if square > i:
            break
        if d[i-square] + 1 < d[i]:
            d[i] = d[i-square] + 1
print(d[n])