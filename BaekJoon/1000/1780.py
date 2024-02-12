def check_paper(x,y,size):
    value_type = paper[x][y]
    for i in range(x, x+size):
        for j in range(y, y+size):
            if value_type != paper[i][j]:
                return False
    return True
def divide_paper(x,y,size):
    if check_paper(x, y, size):
        result[paper[x][y]] += 1
    else:
        new_size = size//3
        for i in range(3):
            for j in range(3):
                divide_paper(x+i*new_size,y+j*new_size,new_size)
result = {-1:0,0:0,1:0}
n = int(input())
paper = [list(map(int,input().split())) for _ in range(n)]
divide_paper(0, 0, n)
print(result[-1], result[0], result[1])