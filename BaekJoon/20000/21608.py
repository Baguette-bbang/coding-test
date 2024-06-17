import sys
input = sys.stdin.readline
# 1. 좋아하는 학생이 상하좌우에 가장 많은 -> 후보 리스트 뽑기 (위치)
# 2. 인접 칸 중 비어있는 칸이 가장 많은 칸 중 열의 번호가 가장 작은 칸 
# 3. 점수 계산
n = int(input())
classroom = [[0] * n for _ in range(n)]
student_like_dict = dict()
student_turn = []
for i in range(n*n):
    student = list(map(int, input().split()))
    student_turn.append(student[0])
    student_like_dict[student[0]] = student[1:]
# print(student_like_dict)

# 첫번째는 배치 고려가 필요없다.
classroom[1][1] = student_turn[0]

def adjacent_check(classroom, like_students):
    moves = [(1,0),(0,1),(-1,0), (0,-1)]
    max_like_num = 0
    loc = []
    for i in range(n):
        for j in range(n):
            if classroom[i][j] == 0: # 학생을 배치하고자 하는 위치에 학생이 먼저 배치되어 있으면 안된다
                like_num = 0
                for di, dj in moves:
                    ni, nj = i+di, j+dj
                    if 0<=ni<n and 0<=nj<n and classroom[ni][nj] in like_students:
                        like_num += 1 # 학생을 배치하고자 하는 위치에 내가 좋아하는 학생의 수를 구하기
                if max_like_num < like_num:
                    max_like_num = like_num
                    loc = [(i,j)]
                elif max_like_num == like_num:
                    loc.append((i,j))
            # 범위 안이면서 좋아하는 학생이 있는 칸
    print("loc", loc)
    return loc
                
def check_empty(classroom, loc):
    # 위치들을 받아서 가장 많은 인접 빈 칸이 있으면서 가장 열이 작은 곳 찾기
    moves = [(1,0),(0,1),(-1,0), (0,-1)]
    max_empty_num = 0
    final_loc = [loc[0][0], loc[0][1]]
    for i, j in loc:
        empty_num = 0
        for di, dj in moves:
            ni, nj = i+di, j+dj
            if 0<=ni<n and 0<=nj<n and classroom[ni][nj] == 0:
                empty_num += 1
        if max_empty_num < empty_num: # 문제 조건 3번
            max_empty_num = empty_num
            final_loc = [i,j]
    return final_loc

def calc_score(classroom, student_like_dict):
    moves = [(1,0),(0,1),(-1,0), (0,-1)]
    answer = 0
    for i in range(n):
        for j in range(n):
            like_students = student_like_dict[classroom[i][j]]
            like_num = 0
            for di, dj in moves:
                ni, nj = i+di, j+dj
                if 0<=ni<n and 0<=nj<n and classroom[ni][nj] in like_students:
                    like_num += 1
            if like_num == 2:
                like_num = 10
            elif like_num == 3:
                like_num = 100
            elif like_num == 4:
                like_num = 1000
            answer += like_num
    return answer
for i in range(1, n*n):
    student = student_turn[i] # 현재 배치 해야하는 학생
    loc_list = adjacent_check(classroom, student_like_dict[student])
    final_loc = check_empty(classroom, loc_list)
    print("final_loc", final_loc)
    classroom[final_loc[0]][final_loc[1]] = student
    
print("classroom", classroom)
print(calc_score(classroom, student_like_dict))