function solution(s) {
    var answer = [];
    // 자신보다 앞에 나왔으면서 자신과 가장 가까운 곳에 있는 글자 찾기
    for (let i = 0; i < s.length; i++) {
        if (s.substring(0, i).includes(s[i])){
            let cnt = 0;
            for (let j = i-1; j >= 0; j--) {
                cnt += 1;
                if (s[j] === s[i]) {
                    answer.push(cnt);
                    break;
                }
            }
        } else {
            answer.push(-1);
        }
    }
    return answer;
}