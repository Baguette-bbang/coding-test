function solution(lines) {
    let answer = 0;    
    lines = lines.sort((a,b) => a[0] - b[0])
    for (let i = lines[0][0]; i < lines[2][1]; i++) {
        let cnt = 0;
        if (lines[0][0] <= i && lines[0][1] >= i+1) {
            cnt += 1;
        }
        if (lines[1][0] <= i && lines[1][1] >= i+1) {
            cnt += 1;
        }
        if (lines[2][0] <= i && lines[2][1] >= i+1) {
            cnt += 1;
        }
        if (cnt >= 2) {
            answer += 1;
        }
    }
    return answer;
}
