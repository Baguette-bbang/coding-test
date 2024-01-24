n = int(input())
stocks = list(map(int, input().split()))
jun_money = n
jun_stock_num = 0
sung_money = n
sung_stock_num = 0
for i in range(len(stocks)):
    # 주식을 살 수 있다면 전량 매수 준현
    if jun_money >= stocks[i]:
        jun_stock_num += jun_money//stocks[i]
        jun_money %= stocks[i]
    if i >=3: # 성민
        # 3일 연속 가격이 상승한다면
        if stocks[i-1]>stocks[i-2]>stocks[i-3] and sung_stock_num > 0:
            # 전량 매도
            sung_money += sung_stock_num * stocks[i]
            sung_stock_num = 0
        # 3일 연속 가격이 하락한다면
        elif stocks[i-1]<stocks[i-2]<stocks[i-3] and sung_money >= stocks[i]:
            # 전량 매수
            sung_stock_num += sung_money//stocks[i]
            sung_money %= stocks[i]
            
# 현금 + 1월 14일의 주가 × 주식 수)
sung_money += stocks[-1]*sung_stock_num
jun_money += stocks[-1]*jun_stock_num
if sung_money==jun_money:
    print("SAMESAME")
elif sung_money > jun_money:
    print("TIMING")
else:
    print("BNP")