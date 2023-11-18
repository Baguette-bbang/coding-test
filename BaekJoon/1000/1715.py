# 시간을 어떻게 줄여야 하는가?
# haep(우선순위 큐)를 이용해서 진행해야 함.
# heap자료구조는 min_heap형식으로 진행됨.
# 여기서 그러면 모든 원소를 일단 담고 입력받는대로
# 입력 받은 원소들 루트 노드를 두번씩 뽑고
# 더한 다음 다시 넣기 
# 언제까지? len(h)-1까지 
import heapq
import sys
input = sys.stdin.readline
def heapsort(iterable):
    h = []
    result = 0
    for value in iterable:
        heapq.heappush(h, value) # 모든 원소를 힙에 넣고
    
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for _ in range(len(h)-1):
        num1 = heapq.heappop(h)
        # print("num1:",num1)
        num2 = heapq.heappop(h)
        # print("num2:",num2)
        heapq.heappush(h, num1+num2)
        result += num1+num2
        # print("h:",h)
        # print("result:",result)
    return result

n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))
res = heapsort(arr)
print(res)