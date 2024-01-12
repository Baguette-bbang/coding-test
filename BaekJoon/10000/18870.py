n = int(input())
num_list = list(map(int,input().split()))
sorted_num_list = sorted(set(num_list)) 

for num in num_list:
    start = 0
    end = len(sorted_num_list)-1
    while True:
        mid = (start+end)//2
        if sorted_num_list[mid] == num:
            print(mid, end = ' ')
            break
        elif sorted_num_list[mid] < num:
            start = mid+1
        else:
            end = mid-1