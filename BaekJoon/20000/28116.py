from collections import defaultdict
import sys
# 28116번 실버3 선택 정렬의 이동 거리 정렬 문제
# 1. 최소 인덱스를 찾는다.
# 2. 제일 왼쪽의 인덱스 위치 차이를 구하고 변경한다.
input = sys.stdin.readline
n = int(input())
num_list = list(map(int, input().split()))
distances = defaultdict(int)
locations = dict()

for i, num in enumerate(num_list):
    locations[num] = i
    
# 가장 최소의 수를 계속 왼쪽에 배치
for i, num in enumerate(sorted(num_list)):
    idx = locations[num]
    locations[num_list[i]] = idx 
    locations[num_list[idx]] = i
    num_list[i], num_list[idx] = num_list[idx], num_list[i]
    distances[num_list[i]] += idx-i
    distances[num_list[idx]] += idx-i

for key, value in sorted(distances.items(), key= lambda x : x[0]):
    print(value, end = ' ')
