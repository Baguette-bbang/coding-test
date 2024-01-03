heights = [int(input()) for _ in range(9)]
heights.sort()
def dfs_heights(idx, selected, heights):
    if len(selected) == 7 and sum(selected) == 100:
        return selected
    if idx>=9:
        return
    
    # 현재 인덱스의 숫자를 선택하는 경우
    result_with = dfs_heights(idx + 1, selected + [heights[idx]], heights)
    if result_with:
        return result_with

    # 현재 인덱스의 숫자를 선택하지 않는 경우
    result_without = dfs_heights(idx + 1, selected, heights)
    if result_without:
        return result_without
dwarfs = dfs_heights(0,[], heights)
for dwarf in dwarfs:
    print(dwarf)