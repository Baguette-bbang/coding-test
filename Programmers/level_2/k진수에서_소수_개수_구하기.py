from math import sqrt
def solution(n, k):
    answer = 0
    # 30분 시작
    # 특정 수를 k진수로 바꾸는법은?
    # 진법 변환의 원리는 주어진 수를 새로운 기수(진법)로 나누고, 그 결과를 다시 나누는 과정을 반복
    k_jinsu = ''
    while n :
        k_jinsu+=str(n%k)
        n //= k
    k_jinsu = k_jinsu[::-1]
    # 소수란? 자기자신과 1로만 나눴을때 딱 떨어지는 수
    # P는 각 자릿수에 0을 포함하지 않는 소수
    # 가장 기본적인 방법은 2부터 그 수의 제곱근까지 모든 정수로 나누어 보는 것
    for i in k_jinsu.split('0'):
        if i != '' and i !='1':
            i = int(i)
            for j in range(2, int(sqrt(i))+1):
                if i % j == 0:
                    break
            else:
                answer += 1
    return answer