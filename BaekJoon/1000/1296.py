yeondu = input()
y_L, y_O, y_V, y_E = 0,0,0,0
for i in yeondu:
  if i == 'L':
    y_L += 1
  elif i == 'O':
    y_O += 1
  elif i == 'V':
    y_V += 1
  elif i == 'E':
    y_E += 1
    
n = int(input())
team_names = {}

for _ in range(n):
  team_name = input()
  for i in team_name:
    t_L, t_O, t_V, t_E = 0, 0, 0, 0

    for i in team_name:
        if i == 'L':
            t_L += 1
        elif i == 'O':
            t_O += 1
        elif i == 'V':
            t_V += 1
        elif i == 'E':
            t_E += 1

    L = y_L + t_L
    O = y_O + t_O
    V = y_V + t_V
    E = y_E + t_E
  
  team_names[team_name] = ((L + O) * (L + V) * (L + E) * (O + V) * (O + E) * (V + E)) % 100
sorted_team_names = sorted(team_names.items(), key = lambda x : (-x[1], x[0])) 
print(sorted_team_names[0][0])

# print(sorted_team_names)