n, m = map(int, input().split())
output = []
for i in range(1, n+1):
    for j in range(1, m+1):
        output.append(f"{i} {j}")
print("\n".join(output))