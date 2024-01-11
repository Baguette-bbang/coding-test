def recursion_binary_search(num_list, start, mid, end, target):
    if num_list[mid] == target:
        return 1
    elif start > end:
        return 0
    elif num_list[mid] > target:
        end = mid - 1
        mid = (end+start)//2
        return recursion_binary_search(num_list, start, mid, end, target)
    else:
        start = mid+1
        mid = (end+start)//2
        return recursion_binary_search(num_list, start, mid, end, target)
n = int(input())
num_list = list(map(int, input().split()))
m = int(input())
guess = list(map(int, input().split()))
num_list.sort()
start = 0
end = len(num_list)-1
mid = end//2
for target in guess:
    print(recursion_binary_search(num_list, start, mid, end, target))
    