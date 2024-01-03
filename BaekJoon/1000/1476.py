# 지구, 태양, 달을 통해 연도가 입력됨
# 1 ≤ E ≤ 15, 1 ≤ S ≤ 28, 1 ≤ M ≤ 19
E, S, M = map(int, input().split())
e,s,m = 0,0,0
year = 0
while True:
    e += 1
    s += 1
    m += 1
    year += 1
    if e == 16:
        e = 1
    if s == 29:
        s = 1
    if m == 20:
        m = 1
    if E==e and S==s and M==m:
        break

print(year)