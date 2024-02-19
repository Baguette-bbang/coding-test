from collections import Counter
def solution(k, tangerine):
    answer = 0
    tangerines = sorted(Counter(tangerine).values(), reverse = True)
    for num in tangerines:
        answer += 1
        k -= num
        if k <= 0:
            return answer