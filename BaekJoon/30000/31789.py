# 4인조
# 1번째 줄 상점 무기의 수
# 2번째 줄에 가용가능한 돈, 후안 공격력
# 3번째 줄부터 ~ 끝까지 무기의 값, 무기의 공격력

# 가용가능한 돈보다 작거나 같으며 후안의 공격력보다 큰 무기가 하나라도 있다면 YES

n = int(input())
w_num, h_power = map(int, input().split())

w_shop = []
for _ in range(n):
  w_shop.append((map(int, input().split())))

for w_price, w_power in w_shop:
  if w_price <= w_num and w_power > h_power:
    print('YES')
    exit(0)
print('NO')