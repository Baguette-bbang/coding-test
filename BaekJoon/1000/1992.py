n = int(input())
video = [list(map(int, list(input()))) for _ in range(n)]
result = ''
def check_video(x, y, size):
    video_type = video[x][y]
    for i in range(x, x+size):
        for j in range(y, y+size):
            if video[i][j] != video_type:
                return False
    return True

def divide_video(x, y, size):
    global result
    if check_video(x,y,size):
        result += str(video[x][y])

    else:
        result += '('
        new_size = size//2
        for i in range(2):
            for j in range(2):
                divide_video(x+i*new_size, y+j*new_size,new_size)
        result += ')'
divide_video(0,0,n)
print(result)