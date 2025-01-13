t = int(input())
bridge_cases = [[0 for _ in range(31)] for _ in range(31)]

def init_bridges(bridge_cases) :
  for i in range(1, 31):
    for j in range(1, 31):
      if i == 1:
        bridge_cases[i][j] = j
      elif i == j :
        bridge_cases[i][j] = 1
      elif i < j:
        bridge_cases[i][j] = bridge_cases[i][j-1] + bridge_cases[i-1][j-1]

init_bridges(bridge_cases)
for i in range(t) :
  n, m = map(int, input().split())
  print(bridge_cases[n][m])