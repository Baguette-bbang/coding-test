m, n = map(int, input().split())
lengths = list(map(int,input().split()))
lengths.sort()
start = 1
end = lengths[-1]
max_length = 0
while start <= end:
    mid = (start + end) // 2
    num = 0 # 과자의 개수
    num = sum(length//mid for length in lengths)
    if num >= m : # 과자의 개수가 조카의 수를 넘거나 같다면
        start = mid + 1
        max_length = mid
    else:
        end = mid - 1
print(max_length)