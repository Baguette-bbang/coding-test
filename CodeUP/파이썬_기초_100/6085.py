w, h, b = map(int, input().split())
f = w * h * b / 8 / 1024 / 1024
print("{:.2f} MB".format(f))