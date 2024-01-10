def solution(s):
    min_compress = float('inf')
    # 패턴이 길이가 1인것부터 패턴이 의미가 있는 len(s)//2+1까지만 접근
    # 문자열은 제일 앞부터 정해진 길이만큼 잘라야한다.
    if len(s) == 1:
        return 1
    else:
        for length in range(1, len(s)//2+1):
            count = 1 # 패턴의 연속적 출현빈도
            compress_s_length = 0 # 특정 길이로 압축한 결과
            for i in range(0,len(s),length): # 앞에서부터 특정 길이만큼 자르면서 진행
                if s[i:i+length] == s[i+length:i+length+length]: # 패턴이 나왔다면
                    count += 1
                else: # 더 이상 패턴이 출현하지 않는다면
                    if count > 1: # 패턴이 출현했었다면 더해주고 
                        compress_s_length+=len(str(count)+s[i:i+length])
                    else: # 패턴이 출현하지 않았다면 길이만큼 더해준다.
                        compress_s_length+=length
                    count = 1 # 특정 패턴의 count 초기화
            if len(s)%length!=0: # 길이를 더하는데 마지막은 남은 길이는 length보다 짧을 수 있기에 딱 그만큼만 더해줘야 한다.
                compress_s_length = compress_s_length - length + len(s)%length

            min_compress = min(min_compress,compress_s_length)
        return min_compress
