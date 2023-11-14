import sys
input = sys.stdin.readline
n = int(input())
chains = list(map(int, input().split()))
chains.sort()
answer = 0

while(1):
    if len(chains) <= 1 :
        # print(chains)
        break
    chains.pop()
    # print(chains)
    chains[0] -= 1
    if chains[0]== 0:
        chains.pop(0)
    answer +=1

print(answer)