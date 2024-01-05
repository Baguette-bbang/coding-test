import sys
input = sys.stdin.readline
# 입력
n = int(input())
consulting = [list(map(int, input().split())) for _ in range(n)]

# 두가지 현재 날짜를 컨설팅 하냐 안하냐
def consulting_plan(n,idx,total_p, consulting):
    # 재귀 종료조건
    if idx>=n:
        return total_p
    # 퇴사일 안에 상담이 끝나야함
    if idx + consulting[idx][0] <= n:
        p_with_consulting = consulting_plan(n,idx+consulting[idx][0], total_p+consulting[idx][1], consulting)
    else :
        p_with_consulting = total_p
    p_without_consulting = consulting_plan(n,idx+1, total_p, consulting)
        
    return max(p_with_consulting, p_without_consulting)
print(consulting_plan(n,0,0, consulting))
