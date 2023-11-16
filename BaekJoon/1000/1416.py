import sys
input = sys.stdin.readline
n, m = map(int, input().split())
books = list(map(int, input().split()))
books.append(0)
books.sort()

max_val = abs(books[-1])
min_val = abs(books[0])

# 최대 절대값의 index
far_val = max(min_val, max_val)

if far_val is max_val: 
    books.reverse()
distance = abs(books[0])

for _ in range(m):
    if books[0] == 0:
        break
    books.pop(0)
    
while(len(books)>1):
    if abs(books[0]) >= abs(books[-1]):
        distance += abs(books[0])*2
        for i in range(m):
            if books[0] == 0:
                break
            books.pop(0)
            
    else:
        distance += abs(books[-1])*2
        for i in range(len(books)-1,len(books)-m-1, -1):
            if books[-1] == 0:
                break
            books.pop()

print(distance)