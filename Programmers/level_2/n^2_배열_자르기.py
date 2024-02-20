def solution(n, left, right):    
    # 규칙1. i번째 행에는 i+1숫자가 i+1개만큼 있다. 나머지 칸은 보다 큰 숫자가 순차적으로 
    # 규칙2. 시작 행은 left // n, 끝 행은 right // n
    # 규칙3. 시작 열은 left % n, 끝 열은 right % n
    start_row = left//n
    end_row = right//n
    start_col = left%n
    end_col = right%n
    
    arr = []
    for i in range(start_row, end_row+1):
        temp = [i+1] * (i+1)
        for j in range(i+2, n+1):
            temp.append(j)
        arr += temp
        
    return arr[start_col:(end_row-start_row)*n+end_col+1]