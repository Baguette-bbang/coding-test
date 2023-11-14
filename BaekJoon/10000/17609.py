# 문자를 양쪽부터 검사 
# 오른쪽 검사 왼쪽 검사
# 홀수 가운데 빼고 같다면 회문
# 오른쪽 틀린부분 제거 후 같다면
# 유사회문
# 왼쪽 틀린 부분 제거 후 같다면
# 유사회문
# 아니면 그냥 회문이오
import sys
input = sys.stdin.readline

n = int(input())
palindromes = []
for _ in range(n):
    palindrome = input().strip()
    palindromes.append(palindrome)
    
def is_palindrome(palindrome):
    return palindrome == palindrome[::-1]

def check_palindrome(palindrome):
    left = 0 # 문자열 시작부터 시작
    right = len(palindrome) - 1 # 문자열 끝부터 시작
    while left < right:
        if palindrome[left] != palindrome[right]:
            # 같지 않다면 오른쪽 문자나 왼쪽 문자 제거 후 팔린드롬 확인
            # 둘 중 하나를 제거했을 때 true라면? 팔린드롬.
            if is_palindrome(palindrome[left:right]) or is_palindrome(palindrome[left+1:right+1]):
                return 1
            # 둘 중 하나를 제거했는데도 false라면 그냥 문자열임.
            return 2
        # 범위 좁히기
        left += 1
        right -= 1
    return 0
for palindrome in palindromes:
    print(check_palindrome(palindrome))