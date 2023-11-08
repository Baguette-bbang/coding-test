# 문자열 안에 특정 문자열이 몇 개나 포함되어 있는지
# 조건 : 중복되지 않게 몇 번 출력되는지 알아야 함.
# 문자열을 처음 등장하는 것을 찾고
# 문자열을 자르고 다시 찾고

import sys
input = sys.stdin.readline
doc = input().strip()
word = input().strip()

count = 0
word_len = len(word)

while 1:
    idx = doc.find(word)
    if idx == -1:
        break
    else:
        count += 1
        doc = doc[idx+word_len:]
print(count)