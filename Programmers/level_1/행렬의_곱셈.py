def solution(arr1, arr2):
    answer = [[]]
    m = len(arr1)
    n = len(arr1[0])
    p = len(arr2[0])
    mp = [[0] * p for _ in range(m)]   
    
    new_arr2 = [] # 열을 행처럼 만들기 
    for j in range(len(arr2[0])):
        temp = []
        for i in range(len(arr2)):
            temp.append(arr2[i][j])
        new_arr2.append(temp)
    
    for i in range(m):
        num_list1 = arr1[i] # 한 행과
        for j in range(len(new_arr2)):
            num_list2 = new_arr2[j] # 한 열을 뽑고 
            num = 0
            for k in range(len(new_arr2[j])):
                num += num_list1[k] * num_list2[k]
            mp[i][j] = num
            
    return mp