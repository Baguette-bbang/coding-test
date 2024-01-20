n = int(input())
cards = [0]+ list(map(int, input().split()))
for i in range(2,n+1):
    j = 1
    while j <= i:
        cards[i] = max(cards[i], cards[j] + cards[i-j])
        j += 1

print(cards[-1])