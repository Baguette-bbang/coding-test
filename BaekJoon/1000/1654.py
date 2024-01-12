k, n = map(int, input().split())
lan_cables = []
for _ in range(k):
    lan_cables.append(int(input()))
lan_cables.sort()
start = 1
end = end = lan_cables[-1]

max_length = 0
# 즉 후보지를 순차적으로 탐색하지말고 결과를 보고 탐색하자
while start <=end:
    mid = (start + end) // 2
    count = 0
    for cable in lan_cables:
        count += cable // mid
    if count >= n: # n개 이상 만드는 경우
        max_length = max(mid, max_length)
        start = mid + 1
    else : # n개를 만들 수 없는 경우
        end = mid -1
print(max_length)