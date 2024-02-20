def solution(phone_book):
    answer = True
    # 10분 시작 -> 14분 끝 (4분 소요)
    # 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 한다.
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    return answer