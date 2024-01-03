def solution(sizes):
    answer = 0
    new_sizes = []
    for x, y in sizes:
        # 사이즈를 회전 시키는 경우도 고려해야함.
        if x>y:
            new_sizes.append([x,y])
        else:
            new_sizes.append([y,x])
            
    max_x, max_y = 0,0
    for x, y in new_sizes:
        if max_x < x :
            max_x = x
        if max_y < y :
            max_y = y
            
    answer = max_x*max_y
    return answer
##########람다를 활용한 풀이###########
def solution(sizes):
    new_sizes = [sorted(size) for size in sizes]
    max_x = max(size[1] for size in new_sizes)  
    max_y = max(size[0] for size in new_sizes)  
    return max_x * max_y
