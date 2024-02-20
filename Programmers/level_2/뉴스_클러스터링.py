from collections import Counter
def solution(str1, str2):
    answer = 0
    # 정각 시작 38분 끝 (38분 소요)
    # 자카드 유사도 J(A, B)는 두 집합의 교집합 크기를 두 집합의 합집합 크기로 나눈 값이다.
    a = [str1[i:i+2].upper() for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
    b = [str2[i:i+2].upper() for i in range(len(str2)-1) if str2[i:i+2].isalpha()]
    if len(a) == 0 and len(b) == 0: # 공집합 처리
        return 65536
    
    A = Counter(a)
    B = Counter(b)
    
    unique = list(set(a+b))
    union = 0
    intersection = 0
    
    for i in range(len(unique)):
        a_num, b_num = 0,0
        if unique[i] in A:
            a_num = A[unique[i]]
        if unique[i] in B:
            b_num = B[unique[i]]
        intersection += (min(a_num, b_num))
        union += (max(a_num, b_num))
        
    return int(intersection/union * 65536)