n1, n2, n3 = map(int, input().split())
minValue = n1 if n1<n2 else n2
minValue = minValue if minValue<n3 else n3
print(minValue)