def solution(numbers):
    answer = []
    # 홀수인 경우
    for num in numbers:
        if num%2==0:
            answer.append(num+1)
        else:
            num = bin(num)[2:]
            num = list('0' + num)
            for i in range(len(num)-1, -1, -1):
                if num[i] == '0':
                    num[i] = '1'
                    num[i+1] = '0'
                    break
            num = ''.join(num)
            answer.append(int(num,2))
    return answer