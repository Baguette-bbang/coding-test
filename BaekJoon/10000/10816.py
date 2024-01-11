from bisect import bisect_left, bisect_right
def count_num_bisect(a, x):
    return bisect_right(a,x) - bisect_left(a,x)
n = int(input())
num_list = list(map(int, input().split()))
num_list.sort()
m = int(input())
guess = list(map(int, input().split()))
for g in guess:
    print(count_num_bisect(num_list, g), end = ' ')
                