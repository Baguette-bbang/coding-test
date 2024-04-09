def solution(arrayA, arrayB):
    answer = 0
    # 영희것만 나눌 수 있는 양수
    # 철수것만 나눌 수 있는 양수
    # 두 조건 중 하나만 만족해도 됨.
    # 각 두 배열에서 가장 작은 수 보다는 커야함. 최대 공약수.
    
    # 1. 각 배열의 최대 공약수 구하기
    # 2. 각 두 배열에서 가장 작은 수 구하기
    # 3. 한 쪽만 해당되는 수 구하기
    
    # 1. 최대 공약수
    def gcd(a, b):
        while b:
            a, b = b, a%b
        return a
    if len(arrayA) >= 2:
        gcdA = gcd(arrayA[0], arrayA[1])
        gcdB = gcd(arrayB[0], arrayB[1])
    else:
        gcdA = arrayA[0]
        gcdB = arrayB[0]
    for i in range(1, len(arrayA)):
        gcdA = gcd(gcdA, arrayA[i])
        gcdB = gcd(gcdB, arrayB[i])
    
    # 2. 정렬 
    arrayA.sort()
    arrayB.sort()
    
    flagA, flagB = True, True
    for i in arrayA:
        if i%gcdB == 0:
            flagA = False
            break
    
    for i in arrayB:
        if i%gcdA == 0:
            flagB = False
            break
    
    if flagA and flagB:
        answer = max(gcdA, gcdB)
    elif flagA and gcdB != 1:
        answer = gcdB
    elif flagB and gcdA != 1:
        answer = gcdA
        
    return answer