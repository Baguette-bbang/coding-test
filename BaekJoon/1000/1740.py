# 백준 1740번 거듭제곱 - 실버 4

# 문제는 3의 제곱수만으로 범위가 작다.
# 1개 이상의 다른 0제곱부터 n제곱수 까지의 조합을 통해서 오름차순 정렬을 하라.
# 1 3 9 27 
# 1 3 4 9 10

# 힌트는 비트마스킹?
# 3진법으로 접근?
import sys 
input = sys.stdin.readline
n = int(input())

num = 1
cnt = 0

## 풀이 1번 (시간초과)
# while True:
#     temp = num
#     flag = True
#     samjin = ''    
#     while temp :
        
#         b = temp % 3
        
#         if b > 1:
#             flag = False
#             break
        
#         samjin = str(b) + samjin
#         temp = temp // 3
    
#     if flag:
#         cnt += 1
#         if n == cnt:
#             print(num)
#             break
#     num += 1

## 풀이 2번 (시간초과)
# while True:
#     temp = num
#     flag = True
#     while temp :
#         b = temp % 3
#         if b > 1:
#             flag = False
#             break        
#         temp = temp // 3
    
#     if flag:
#         cnt += 1
#         if n == cnt:
#             print(num)
#             break
#     num += 1

## 풀이 3번
# 어차피 2진수만 사용함. 그렇다면 N을 2진수로 변환 후
# 각 자리수에 맞게 3의 거듭제곱을 한다면?
# 0100 (4) -> 9

# n = bin(n)[2:]
answer = 0
p = 0
while n > 0:
    if n % 2 == 1:
        answer += 3 ** p
    p += 1
    n //= 2
print(answer)