import math
# 시간제한이 짧다.
# A미터 올라가고 B미터 떨어진다.

a, b, v = map(int, input().split())
# n일만에 올라갓다는 것
# 2 1 5 
# 1. 2 -> 1 (+2 -1)
# 2. 3 -> 2 (+2 -1)
# 3. 4 -> 3 (+2 -1)
# 4. 5 (+2)
# (a-b) * (n-1) + a >= v
# an - a - bn+b +a >= v
# an-bn +b >= v
# (a-b)n +b >= v
# (a-b)n >= v-b
# n >= (v-b)/(a-b)



print(math.ceil((v-b)/(a-b)))