def binary_search_loof(num_list, target):
    start = 0
    end = len(num_list)-1
    mid = end // 2
    while start<=end:
        if target == num_list[mid]:
            return 1
        else:
            if target > num_list[mid]:
                start = mid + 1
                mid = (end + start) // 2
            else:
                end = mid - 1
                mid = (end + start) // 2
    return 0

n = int(input())
num_list = list(map(int, input().split()))
num_list.sort()
m = int(input())
guess = list(map(int, input().split()))

for g in guess:
    print(binary_search_loof(num_list, g), end = ' ')        