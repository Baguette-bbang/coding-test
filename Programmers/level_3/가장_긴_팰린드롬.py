def solution(s):
    answer = 0
    # 각 자리에서 홀수로 팰린드롬이 되는가
    # 각 자리에서 짝수로 팰린드롬이 되는가 -> 동시에 같은 문자가 출현했을때만이다.
    # 하나를 잡고 전과 후의 문자열을 하나씩 늘려간다.
    # 만약 둘 중 하나라도 범위에 어긋나거나 팰린드롬이 아니게 된다면 break
    # 다음 자리로 넘어간다.
    
    if len(s) ==1:
        return 1
    
    for i in range(len(s)-1):
        if s[i] == s[i+1]: # 연속된 문자가 출현한다면 짝수 시작 팰린드롬 검사하기
            cnt = 2
            for j in range(min(len(s[:i]), len(s[i+2:]))):
                left = s[i-1-j:i]
                right = s[i+2:j+i+3]
                # print("짝수",left,s[i:i+2], right)
                if left == right[::-1]:
                    cnt+=2
                else:
                    break
            answer = max(answer, cnt)
         # 연속된 문자가 출현하지 않는다면 홀수 시작 팰린드롬 검사하기
        cnt = 1
        for j in range(min(len(s[:i]), len(s[i+1:]))):
            left = s[i-1-j:i]
            right = s[i+1:j+i+2]
            # print("홀수",left,s[i], right)
            if left == right[::-1]:
                cnt += 2
            else:
                break
        answer = max(answer, cnt)
    return answer