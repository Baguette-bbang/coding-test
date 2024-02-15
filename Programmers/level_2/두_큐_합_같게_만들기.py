from collections import deque
def solution(queue1, queue2):
    # 둘의 합이 같아야함.
    # 시작 둘 큐의 길이는 같다.
    # 하지만 끝에서 둘 큐의 길이는 같지 않아도 된다.
    
    # 한 큐에서 빼서 다른 큐로 넣는 과정을 반복
    # a->b로 가는 경우와 b->a로 가는 경우
    
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    q1_sum = sum(queue1)
    q2_sum = sum(queue2)
    cnt = 0
    total_half = (q1_sum + q2_sum)//2
    flag = True
    max_cnt = len(queue1) + len(queue2) * 2  # 최대 이동 횟수 설정
    if (q1_sum+q2_sum)%2 == 0:
        while cnt <= max_cnt:
            # q1이 작은경우 q2에서 받아오기
            if q1_sum == q2_sum:
                flag = False
                break
            elif q1_sum < total_half:
                cnt += 1
                q2 = queue2.popleft()
                queue1.append(q2)
                q1_sum += q2
                q2_sum -= q2
            elif q2_sum < total_half:
                cnt += 1
                q1 = queue1.popleft()
                queue2.append(q1)
                q2_sum += q1
                q1_sum -= q1
    if flag:
        return -1
    return cnt