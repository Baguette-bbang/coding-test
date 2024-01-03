from collections import deque

def can_reach_festival(hx, hy, cs, fx, fy):
    queue = deque([(hx, hy, 20)])  # (x, y, remaining_beers)
    visited = set([(hx, hy)])

    while queue:
        x, y, beers = queue.popleft()

        # 페스티벌에 도착할 수 있다면
        if abs(x - fx) + abs(y - fy) <= beers * 50:
            return "happy"

        for cx, cy in cs:
            if (cx, cy) not in visited and abs(x - cx) + abs(y - cy) <= beers * 50:
                queue.append((cx, cy, 20))  # 편의점에서 맥주를 새로 채움
                visited.add((cx, cy))

    return "sad"

t = int(input())
for _ in range(t):
    n = int(input())
    hx, hy = map(int, input().split())
    cs = [tuple(map(int, input().split())) for _ in range(n)]
    fx, fy = map(int, input().split())

    result = can_reach_festival(hx, hy, cs, fx, fy)
    print(result)