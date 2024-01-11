# A집합에는 속하지만 B집합에는 속하지 않는 원소를 구하여라
a, b = map(int,input().split())
a_nums = set(map(int, input().split()))
b_nums = set(map(int, input().split()))
complement = a_nums-b_nums
complement = sorted(complement)
if len(complement)>0:
    print(len(complement))
    for c in complement:
        print(c,end=' ')
else :
    print(0)