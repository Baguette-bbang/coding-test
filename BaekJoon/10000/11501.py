from collections import deque
import sys
input = sys.stdin.readline
# 1. 주식을 하나 사기
# 2. 원하는 만큼 가지고 있는 주식 팔기
# 3. 아무것도 하지 않기

# 싼 가격에 사서 비싼 가격에 팔아야한다.
# 때문에 가격이 떨어지기 전 보다 비싸다면 팔아야한다.
# 1, 1, 3, 1, 2
# 3->1로 가기 전에 팔아야한다. 는 의미

# 해당 날 이후로 비싸지지 않는다면 사면 안된다.

t = int(input())
for i in range(t):
    n = int(input())
    temp = list(map(int, input().split()))
    stocks = []
    for i in range(n):
        stocks.append((temp[i],i))
        
    profits = 0
    reverse_stocks = deque(sorted(stocks,reverse = True))
    buy_stocks = deque()
    
    expensive_stock = reverse_stocks.popleft()
    for stock, idx in stocks:
        # 현재 인덱스보다 가장 비싼 스톡의 인덱스가 작다면 계속 뽑음
        while reverse_stocks and expensive_stock[1] < idx:
            expensive_stock = reverse_stocks.popleft()
        # 가장 비싼 stock과 같은 가격이 됐다면
        if buy_stocks and expensive_stock[0] == stock:
            # 판매 진행
            while buy_stocks:
                profits += stock - buy_stocks.popleft()
        # 구매 진행
        elif expensive_stock[0] > stock:
            buy_stocks.append(stock)
    print(profits)