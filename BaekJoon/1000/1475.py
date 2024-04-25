# 백준 1475번 방 번호 - 실버5
# 0~9번까지 숫자가 하나씩 들어있다. 이게 한 세트이다.
# 플라스틱 숫자를 한 세트로 판다.

# 1. 9와 6 숫자를 구하고 반으로 나눈 후 올림처리
# 2. 6과 9를 제외한 숫자 구하기
# 3. 더 큰 값이 답임

from collections import Counter
import math

n = list(input())
n = Counter(n)
nine_six = math.ceil((n.get('9',0) + n.get('6',0))/2)
if n['9']:
    n.pop('9')
if n['6']:    
    n.pop('6')

max_n = 0
if n:
    max_n = max(list(n.values()))
max_num = max(max_n, nine_six)
print(max_num)