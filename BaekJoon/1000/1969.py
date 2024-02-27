n, m = map(int, input().split())
dna_list = [input() for _ in range(n)]
from collections import Counter
new_dna_list = list(zip(*dna_list))
final_dna = ''
for i in range(m):
    # 빈도가 높은 순으로 정렬하고, 빈도가 같으면 알파벳 순으로 정렬
    counter = sorted(Counter(new_dna_list[i]).most_common(), key=lambda x: (-x[1], x[0]))
    final_dna += counter[0][0]
distance = 0
for dna in dna_list:
    for i in range(m):
        if dna[i] != final_dna[i]:
            distance += 1
print(final_dna)
print(distance)