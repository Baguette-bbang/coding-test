function solution(n) {
    var answer = Array.from({length : n}, () => new Array(n).fill(0));
    let up=0, left = 0;
    let down=n-1, right = n-1;
    // 상 -> 우 -> 하 -> 좌 순으로 반복됨.
    // 각각 한 번씩 할 때마다 해당 범위가 줄어들게 됨.
    // 종료조건? 다채워지면?
    let cur_num = 1;
    
    while (cur_num <= n*n) {
        for (let i = left; i <= right; i++) {
            answer[up][i] = cur_num;
            cur_num ++;
        }
        up++;
        
        for (let i = up; i <= down; i++) {
            answer[i][right] = cur_num;
            cur_num ++;
        }
        right--;
        for (let i = right; i >= left; i--) {
            answer[down][i] = cur_num;
            
            cur_num ++;
        }
        down--;
        
        for (let i = down; i >= up; i--) {
            answer[i][left] = cur_num;
            cur_num ++;
        }
        left++;
    }
    return answer;
}