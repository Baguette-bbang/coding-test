def kaing(m,n,x,y):
    # x와 y는 M과 N의 주기에 따라 1부터 시작하므로,
    # 주어진 x와 y에서 1을 빼서 0부터 시작하는 것으로 조정
    x -= 1
    y -= 1

    while x < m * n:
        # x를 N으로 나눈 나머지가 y와 같은지 확인
        if x % n == y:
            return x + 1  # 1을 더해 원래 문제의 조건에 맞추기
        x += m
    
    # 조건을 만족하는 연도를 찾지 못한 경우
    return -1
t = int(input())
for _ in range(t):
    m, n, x, y = map(int,input().split())
    year = kaing(m,n,x,y)
    print(year)