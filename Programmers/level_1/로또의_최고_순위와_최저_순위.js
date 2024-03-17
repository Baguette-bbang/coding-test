function solution(lottos, win_nums) {
    // 몇 개를 맞추었는지
    // 몇 개를 모르는지
    let win_cnt = 0;
    let missing_cnt = 0;
    for (let i = 0; i < 6; i++) {
        if (win_nums.includes(lottos[i])) {
            win_cnt ++;
        } else if (lottos[i] == 0) {
            missing_cnt ++;
        }
    }
    // console.log(win_cnt, missing_cnt)
    let rank = [6,6,5,4,3,2,1];
    return [rank[win_cnt + missing_cnt],rank[win_cnt]];
}