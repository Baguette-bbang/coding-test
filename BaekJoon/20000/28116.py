from collections import defaultdict
import sys
# 28116번 실버3 선택 정렬의 이동 거리 정렬 문제
# 1. 최소 인덱스를 찾는다.
# 2. 제일 왼쪽의 인덱스 위치 차이를 구하고 변경한다.
input = sys.stdin.readline
n = int(input())
num_list = list(map(int, input().split())) # 입력 배열
distances = defaultdict(int) # 요소마다의 총 이동거리
locations = dict() # 요소의 현 위치

for i, num in enumerate(num_list): # 각 요소마다의 초기 위치 설정
    locations[num] = i
print(locations)
# 가장 최소의 수를 계속 왼쪽에 배치 (1~5 수를 순차적으로 정렬)
for i, num in enumerate(sorted(num_list)):
    # i의 의미는 내가 현재 정렬하고자 하는 위치
    # idx 현재 정렬하고자하는 최솟값의 위치를 파악
    idx = locations[num]
    # 위치를 스왑
    locations[num_list[i]] = idx 
    locations[num_list[idx]] = i
    # 실제 값을 스왑
    num_list[i], num_list[idx] = num_list[idx], num_list[i]
    print(locations)
    distances[num_list[i]] += idx-i
    distances[num_list[idx]] += idx-i

for key, value in sorted(distances.items(), key= lambda x : x[0]):
    print(value, end = ' ')

# 1. 이중 for문을 사용하지 않는 것
# 2. 현재 정렬하고자 하는 최솟값을 파악하는 것