
# # 1번째 시도 -> 시간초과
# def solution(sequence, k):
#     answer = []
#     cur_length = 0
#     past_length = float('inf')
#     temp_k = k
    
#     if k in sequence:
#         answer = [sequence.index(k),sequence.index(k)]
        
#     else:
#         for start in range(len(sequence)):
#             for end in range(start, len(sequence)):
#                 cur_length += 1
#                 temp_k -= sequence[end]
#                 if temp_k < 0:
#                     break
#                 if temp_k == 0 and cur_length < past_length:
#                     answer = [start, end]
#                     past_length = cur_length
#                     break
#             cur_length = 0
#             temp_k = k

#     return answer

def solution(sequence, k):
    answer = []
    start, end = 0, 0
    cur_length = 0
    result = 0
    past_length = float('inf')
    index = next((i for i, num in enumerate(sequence) if num > k), None)
    # 시간 단축을 위해 해당 숫자가 있다면 바로 answer에 입력
    if k in sequence:
        answer = [sequence.index(k),sequence.index(k)]

    else: # 종료조건? 더이상 증가할 곳이 없을경우
        while (end < index) : # 끝점이 배열의 끝(6)에 오면 종료
            result = sum(sequence[start:end])
            print(sequence[start:end])
            print("result : ", result)
            print("start : ", start)
            print("end : ", end)

            cur_length = end - start + 1
            if cur_length < past_length and result == k : # 부분수열의 길이가 기존 길이보다 작고 k값과 같다면 answer이다.
                answer = [start, end-1]
                past_length = cur_length
            elif result <= k : # 부분수열의 합이 k값보다 작거나 같다면 끝점을 늘린다.
                end += 1
            elif result > k :
                start += 1
            
    return answer

print(solution([1,2,3,3,4,5,6,9], 8))