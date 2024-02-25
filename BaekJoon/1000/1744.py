from heapq import heappop, heappush, heapify

# 수열의 두 수를 묶는다. 위치에 상관없이(같은위치는 불가능)
# 묶은 수는 서로 곱한 뒤 더한다.
# 수열의 모든 수는 단 한번만 묶거나 묶지 않아야한다.

# 묶는 경우 : 기존 수들의 합보다 커지는 경우
# 묶지 않는 경우 : 기존 수들의 합보다 커지지 않는 경우
# max() 활용 문제임
# 짝수인 경우, 홀수인 경우

answer = 0
n = int(input())
num_list1 = [] # 음수
num_list2 = [] # 양수

for i in range(n):
    num = int(input())
    if num <= 0:
        num_list1.append(num)
    else:
        num_list2.append(-num)

def cal(num_list, flag, answer):
    heapify(num_list)
    while num_list:
        a = heappop(num_list) * flag
        if len(num_list) >= 1:
            b = heappop(num_list) * flag
            if a*b <= a+b:
                heappush(num_list, b*flag)
                answer += a
            else:
                answer += a*b
        else:
            answer += a
    return answer
            
answer = cal(num_list1, 1, answer)
answer =  cal(num_list2, -1, answer)
print(answer)
        
    